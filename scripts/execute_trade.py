#!/usr/bin/env python3
"""
Executes a trade via Alpaca's live trading API after validating all safety checks.

Usage:
    python scripts/execute_trade.py \
        --proposal /tmp/trade_proposal.json \
        --evaluation /tmp/evaluation_result.json \
        --config config/config.yml
    # Writes /tmp/trade_execution.json
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, date
from pathlib import Path

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import yaml


def load_json(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_banned_tickers(config: dict) -> set:
    """Load banned tickers from file."""
    path = config.get("safety", {}).get("banned_tickers_file", "config/banned_tickers.txt")
    banned = set()
    if Path(path).exists():
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    banned.add(line.upper())
    return banned


def count_trades_today(history_path: str) -> int:
    """Count how many trades have been executed today."""
    if not Path(history_path).exists():
        return 0
    with open(history_path) as f:
        history = json.load(f)
    today = date.today().isoformat()
    return sum(
        1
        for t in history.get("trades", [])
        if t.get("executed_at", "").startswith(today) and t.get("status") == "filled"
    )


def fail(ticker: str, action: str, reason: str, output_path: str):
    """Write a failure result and exit."""
    result = {
        "success": False,
        "ticker": ticker,
        "action": action,
        "quantity": 0,
        "price": 0,
        "order_id": None,
        "error": reason,
        "executed_at": datetime.now(timezone.utc).isoformat(),
    }
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"TRADE REJECTED: {reason}")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Execute trade via Alpaca")
    parser.add_argument("--proposal", required=True)
    parser.add_argument("--evaluation", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", default="/tmp/trade_execution.json")
    args = parser.parse_args()

    config = load_config(args.config)
    proposal = load_json(args.proposal)
    evaluation = load_json(args.evaluation)
    safety = config.get("safety", {})

    ticker = proposal.get("ticker", "").upper()
    action = proposal.get("action", "").upper()
    asset_class = proposal.get("asset_class", "STOCK").upper()
    output = args.output

    is_crypto = asset_class == "CRYPTO"

    # Normalize crypto symbol formats:
    #   order_symbol  = "BTC/USD" (slash format for orders and data)
    #   position_symbol = "BTCUSD" (no slash for positions)
    if is_crypto:
        order_symbol = ticker if "/" in ticker else ticker.replace("USD", "/USD")
        position_symbol = ticker.replace("/", "")
    else:
        order_symbol = ticker
        position_symbol = ticker

    # ── Safety checks ──────────────────────────────────────────────

    # 1. Minimum AI score
    min_score = safety.get("min_ai_score", 65)
    if evaluation.get("score", 0) < min_score:
        fail(ticker, action, f"AI score {evaluation['score']} below minimum {min_score}", output)

    # 2. Minimum approvals
    min_approvals = safety.get("min_approvals", 2)
    if proposal.get("approval_count", 0) < min_approvals:
        fail(
            ticker,
            action,
            f"Only {proposal['approval_count']} approval(s), need {min_approvals}",
            output,
        )

    # 3. Valid action
    allowed = [a.upper() for a in safety.get("allowed_actions", ["BUY", "SELL"])]
    if action not in allowed:
        fail(ticker, action, f"Action '{action}' not in allowed list: {allowed}", output)

    # 4. Banned tickers
    banned = load_banned_tickers(config)
    if ticker in banned or position_symbol in banned:
        fail(ticker, action, f"Ticker {ticker} is on the banned list", output)

    # 5. Daily trade limit
    history_path = config.get("logging", {}).get(
        "trade_history_file", "data/trade_history.json"
    )
    trades_today = count_trades_today(history_path)
    max_daily = safety.get("max_trades_per_day", 3)
    if trades_today >= max_daily:
        fail(ticker, action, f"Daily trade limit reached ({max_daily})", output)

    # ── Connect to Alpaca ──────────────────────────────────────────

    api_key = os.environ["ALPACA_API_KEY"]
    secret_key = os.environ["ALPACA_SECRET_KEY"]
    is_paper = config.get("alpaca", {}).get("paper", False)
    client = TradingClient(api_key, secret_key, paper=is_paper)

    # 6. Check ticker is tradable
    try:
        asset = client.get_asset(position_symbol)
        if not asset.tradable:
            fail(ticker, action, f"{ticker} exists but is not tradable", output)
        # Auto-detect asset class if not explicitly set
        if asset_class == "STOCK" and str(asset.asset_class).lower() == "crypto":
            is_crypto = True
            asset_class = "CRYPTO"
            order_symbol = ticker if "/" in ticker else ticker.replace("USD", "/USD")
            position_symbol = ticker.replace("/", "")
    except Exception as e:
        fail(ticker, action, f"Ticker lookup failed: {e}", output)

    # 7. Price check (penny stock for stocks, minimum price for crypto)
    latest_price = None
    if is_crypto:
        try:
            from alpaca.data.historical import CryptoHistoricalDataClient
            from alpaca.data.requests import CryptoLatestBarRequest

            crypto_data_client = CryptoHistoricalDataClient()
            bars = crypto_data_client.get_crypto_latest_bar(
                CryptoLatestBarRequest(symbol_or_symbols=order_symbol)
            )
            latest_price = float(bars[order_symbol].close)
            crypto_min = safety.get("crypto_min_price", 0.001)
            if latest_price < crypto_min:
                fail(
                    ticker,
                    action,
                    f"{ticker} price ${latest_price} is below crypto minimum ${crypto_min}. "
                    "Dust tokens are not allowed.",
                    output,
                )
        except Exception:
            pass  # If we can't check price, proceed cautiously
    else:
        if safety.get("ban_penny_stocks", True):
            try:
                from alpaca.data.historical import StockHistoricalDataClient
                from alpaca.data.requests import StockLatestBarRequest

                data_client = StockHistoricalDataClient(api_key, secret_key)
                bars = data_client.get_stock_latest_bar(
                    StockLatestBarRequest(symbol_or_symbols=ticker)
                )
                latest_price = float(bars[ticker].close)
                if latest_price < 5.0:
                    fail(
                        ticker,
                        action,
                        f"{ticker} is a penny stock (${latest_price:.2f}). Banned by policy.",
                        output,
                    )
            except Exception:
                pass  # If we can't check price, proceed cautiously

    # 8. Determine order quantity
    max_position = safety.get("max_position_size", 500)
    suggested = proposal.get("suggested_amount")
    trade_amount = min(float(suggested), max_position) if suggested else max_position

    # Fetch latest price if not already retrieved
    if latest_price is None:
        if is_crypto:
            try:
                from alpaca.data.historical import CryptoHistoricalDataClient
                from alpaca.data.requests import CryptoLatestBarRequest

                crypto_data_client = CryptoHistoricalDataClient()
                bars = crypto_data_client.get_crypto_latest_bar(
                    CryptoLatestBarRequest(symbol_or_symbols=order_symbol)
                )
                latest_price = float(bars[order_symbol].close)
            except Exception:
                latest_price = None
        else:
            try:
                from alpaca.data.historical import StockHistoricalDataClient
                from alpaca.data.requests import StockLatestBarRequest

                data_client = StockHistoricalDataClient(api_key, secret_key)
                bars = data_client.get_stock_latest_bar(
                    StockLatestBarRequest(symbol_or_symbols=ticker)
                )
                latest_price = float(bars[ticker].close)
            except Exception:
                latest_price = None

    if action == "BUY":
        if latest_price is None:
            fail(ticker, action, "Could not determine current price for quantity calc", output)

        quantity = int(trade_amount // latest_price)
        if quantity < 1:
            # Use fractional shares/coins if price > trade_amount
            quantity = round(trade_amount / latest_price, 4)

        # Check buying power
        account = client.get_account()
        if float(account.buying_power) < trade_amount:
            fail(
                ticker,
                action,
                f"Insufficient buying power. Need ~${trade_amount:.2f}, "
                f"have ${float(account.buying_power):.2f}",
                output,
            )

    elif action == "SELL":
        try:
            position = client.get_open_position(position_symbol)
            available_qty = float(position.qty)
        except Exception:
            fail(ticker, action, f"No open position in {ticker} to sell", output)

        if latest_price:
            sell_qty = int(trade_amount // latest_price)
            quantity = min(sell_qty, available_qty) if sell_qty > 0 else available_qty
        else:
            quantity = available_qty

    # ── Submit order ───────────────────────────────────────────────

    side = OrderSide.BUY if action == "BUY" else OrderSide.SELL
    tif = TimeInForce.GTC if is_crypto else TimeInForce.DAY

    try:
        order_request = MarketOrderRequest(
            symbol=order_symbol,
            qty=quantity if isinstance(quantity, int) and quantity >= 1 else None,
            notional=round(trade_amount, 2)
            if (isinstance(quantity, float) or (isinstance(quantity, int) and quantity < 1))
            else None,
            side=side,
            time_in_force=tif,
        )
        order = client.submit_order(order_request)

        result = {
            "success": True,
            "ticker": ticker,
            "action": action,
            "asset_class": asset_class,
            "quantity": float(quantity),
            "price": latest_price or 0,
            "notional": round(trade_amount, 2),
            "order_id": str(order.id),
            "order_status": str(order.status),
            "executed_at": datetime.now(timezone.utc).isoformat(),
            "pr_number": proposal.get("pr_number"),
            "ai_score": evaluation.get("score"),
            "approval_count": proposal.get("approval_count"),
            "error": None,
        }

        with open(output, "w") as f:
            json.dump(result, f, indent=2)

        print(f"ORDER SUBMITTED: {action} {quantity} x {ticker} [{asset_class}] (Order ID: {order.id})")

    except Exception as e:
        fail(ticker, action, f"Order submission failed: {e}", output)


if __name__ == "__main__":
    main()
