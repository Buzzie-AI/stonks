#!/usr/bin/env python3
"""
Computes contributor metrics, assigns ranks, generates leaderboard,
and updates README.md and data/contributors.json.

Usage:
    python scripts/update_leaderboard.py --config config/config.yml
"""

import argparse
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_trade_history(path: str) -> list[dict]:
    if not Path(path).exists():
        return []
    with open(path) as f:
        data = json.load(f)
    return data.get("trades", [])


def fetch_current_prices(trades: list[dict], api_key: str, secret_key: str) -> dict:
    """Batch-fetch current prices for all tickers in trade history.

    Returns a dict mapping ticker -> current_price.
    Handles both stock and crypto symbols.
    """
    prices = {}
    if not trades:
        return prices

    # Collect unique tickers and classify them
    stock_tickers = set()
    crypto_tickers = set()
    for t in trades:
        ticker = t.get("ticker", "")
        if not ticker:
            continue
        # Detect crypto: has /USD suffix or ends with USD (e.g. BTCUSD, BTC/USD)
        if "/USD" in ticker or (ticker.endswith("USD") and len(ticker) > 3):
            crypto_tickers.add(ticker)
        else:
            stock_tickers.add(ticker)

    # Fetch stock prices
    if stock_tickers:
        try:
            from alpaca.data.historical import StockHistoricalDataClient
            from alpaca.data.requests import StockLatestBarRequest

            client = StockHistoricalDataClient(api_key, secret_key)
            bars = client.get_stock_latest_bar(
                StockLatestBarRequest(symbol_or_symbols=list(stock_tickers))
            )
            for symbol, bar in bars.items():
                prices[symbol] = float(bar.close)
        except Exception as e:
            print(f"WARNING: Stock price fetch failed: {e}")

    # Fetch crypto prices
    if crypto_tickers:
        try:
            from alpaca.data.historical import CryptoHistoricalDataClient
            from alpaca.data.requests import CryptoLatestBarRequest

            client = CryptoHistoricalDataClient(api_key, secret_key)
            # Normalize to slash format for API
            order_symbols = []
            ticker_map = {}  # order_symbol -> original_ticker
            for ticker in crypto_tickers:
                order_sym = ticker if "/" in ticker else ticker.replace("USD", "/USD")
                order_symbols.append(order_sym)
                ticker_map[order_sym] = ticker
            bars = client.get_crypto_latest_bar(
                CryptoLatestBarRequest(symbol_or_symbols=order_symbols)
            )
            for order_sym, bar in bars.items():
                original = ticker_map.get(order_sym, order_sym)
                prices[original] = float(bar.close)
                # Also store under the other format for lookup flexibility
                alt = order_sym.replace("/", "")
                prices[alt] = float(bar.close)
        except Exception as e:
            print(f"WARNING: Crypto price fetch failed: {e}")

    return prices


def compute_contributor_metrics(
    trades: list[dict], current_prices: dict
) -> dict[str, dict]:
    """Group trades by github_username and compute per-contributor metrics.

    Returns dict keyed by username with:
      trades_count, wins, losses, win_rate, total_pnl, avg_ai_score, trades_detail
    """
    by_user = defaultdict(list)
    for t in trades:
        username = t.get("github_username", "")
        if not username:
            continue
        by_user[username].append(t)

    contributors = {}
    for username, user_trades in by_user.items():
        total_pnl = 0.0
        wins = 0
        losses = 0
        ai_scores = []
        trades_detail = []

        for t in user_trades:
            ticker = t.get("ticker", "")
            action = t.get("action", "")
            entry_price = t.get("price", 0)
            quantity = t.get("quantity", 0)
            ai_score = t.get("ai_score")

            if ai_score is not None:
                ai_scores.append(ai_score)

            # P&L only for BUY trades (SELL treated as 0)
            pnl = 0.0
            if action == "BUY" and entry_price > 0 and quantity > 0:
                current_price = current_prices.get(ticker, entry_price)
                pnl = (current_price - entry_price) * quantity
                if pnl > 0:
                    wins += 1
                else:
                    losses += 1

            total_pnl += pnl
            trades_detail.append(
                {
                    "ticker": ticker,
                    "action": action,
                    "entry_price": entry_price,
                    "quantity": quantity,
                    "pnl": round(pnl, 2),
                    "pr_number": t.get("pr_number"),
                    "executed_at": t.get("executed_at"),
                }
            )

        trades_count = len(user_trades)
        buy_count = wins + losses
        win_rate = round(wins / buy_count, 4) if buy_count > 0 else 0.0
        avg_ai = round(sum(ai_scores) / len(ai_scores), 1) if ai_scores else 0.0

        contributors[username] = {
            "trades_count": trades_count,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "total_pnl": round(total_pnl, 2),
            "avg_ai_score": avg_ai,
            "rank": "rookie",  # assigned in next step
            "trades_detail": trades_detail,
        }

    return contributors


def assign_ranks(contributors: dict[str, dict], config: dict) -> dict[str, dict]:
    """Evaluate rank criteria from config (top-down) for each contributor.

    Ranks are checked from highest to lowest; first match sticks.
    """
    ranks_config = config.get("ranks", {})

    # Order: portfolio_manager > strategist > analyst > rookie (highest first)
    rank_order = ["portfolio_manager", "strategist", "analyst", "rookie"]

    for username, data in contributors.items():
        assigned = "rookie"
        for rank_name in rank_order:
            rc = ranks_config.get(rank_name, {})
            min_trades = rc.get("min_trades", 0)
            min_win_rate = rc.get("min_win_rate", 0)
            requires_positive_pnl = rc.get("requires_positive_pnl", False)

            if data["trades_count"] < min_trades:
                continue
            if data["win_rate"] < min_win_rate:
                continue
            if requires_positive_pnl and data["total_pnl"] <= 0:
                continue

            assigned = rank_name
            break

        data["rank"] = assigned

    return contributors


def generate_leaderboard_table(contributors: dict[str, dict]) -> str:
    """Render a markdown leaderboard table sorted by total P&L descending."""
    if not contributors:
        return "No contributors yet. Submit a PR to get on the leaderboard!\n"

    # Sort by total P&L descending
    sorted_users = sorted(
        contributors.items(), key=lambda x: x[1]["total_pnl"], reverse=True
    )

    rank_labels = {
        "rookie": "Rookie",
        "analyst": "Analyst",
        "strategist": "Strategist",
        "portfolio_manager": "Portfolio Manager",
    }

    rows = ["| # | Contributor | Rank | Trades | Win Rate | Total P&L | Avg AI Score |"]
    rows.append("|---|-------------|------|--------|----------|-----------|--------------|")

    for i, (username, data) in enumerate(sorted_users, 1):
        pnl = data["total_pnl"]
        pnl_sign = "+" if pnl >= 0 else ""
        wr = f"{data['win_rate'] * 100:.0f}%"
        rank_label = rank_labels.get(data["rank"], data["rank"])
        rows.append(
            f"| {i} "
            f"| @{username} "
            f"| {rank_label} "
            f"| {data['trades_count']} "
            f"| {wr} "
            f"| {pnl_sign}${pnl:,.2f} "
            f"| {data['avg_ai_score']:.0f} |"
        )

    return "\n".join(rows) + "\n"


def update_readme_leaderboard(contributors: dict[str, dict], readme_path: str = "README.md"):
    """Replace content between LEADERBOARD markers in README."""
    if not Path(readme_path).exists():
        return

    with open(readme_path) as f:
        content = f.read()

    table_md = generate_leaderboard_table(contributors)

    marker_start = "<!-- LEADERBOARD_START -->"
    marker_end = "<!-- LEADERBOARD_END -->"
    pattern = re.escape(marker_start) + r".*?" + re.escape(marker_end)

    replacement = f"{marker_start}\n{table_md}\n{marker_end}"

    if marker_start in content:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Shouldn't happen if README is set up, but append if missing
        content += f"\n\n{replacement}\n"

    with open(readme_path, "w") as f:
        f.write(content)


def save_contributors(contributors: dict[str, dict], path: str):
    """Save contributors data to JSON file."""
    # Strip trades_detail for the saved file to keep it concise
    output = {
        "contributors": {},
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    for username, data in contributors.items():
        output["contributors"][username] = {
            "trades_count": data["trades_count"],
            "wins": data["wins"],
            "losses": data["losses"],
            "win_rate": data["win_rate"],
            "total_pnl": data["total_pnl"],
            "avg_ai_score": data["avg_ai_score"],
            "rank": data["rank"],
            "trades_detail": data["trades_detail"],
        }

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(output, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Update contributor leaderboard")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    config = load_config(args.config)

    history_path = config.get("logging", {}).get(
        "trade_history_file", "data/trade_history.json"
    )
    contributors_path = config.get("logging", {}).get(
        "contributors_file", "data/contributors.json"
    )

    trades = load_trade_history(history_path)

    # Fetch current prices (requires Alpaca keys)
    api_key = os.environ.get("ALPACA_API_KEY", "")
    secret_key = os.environ.get("ALPACA_SECRET_KEY", "")

    if api_key and secret_key:
        current_prices = fetch_current_prices(trades, api_key, secret_key)
    else:
        print("WARNING: No Alpaca keys — using entry prices for P&L calculation")
        current_prices = {}

    # Compute metrics
    contributors = compute_contributor_metrics(trades, current_prices)

    # Assign ranks
    contributors = assign_ranks(contributors, config)

    # Save contributors.json
    save_contributors(contributors, contributors_path)

    # Update README leaderboard
    update_readme_leaderboard(contributors)

    print(f"Leaderboard updated: {len(contributors)} contributor(s)")
    for username, data in sorted(
        contributors.items(), key=lambda x: x[1]["total_pnl"], reverse=True
    ):
        print(f"  @{username}: {data['rank']} — P&L ${data['total_pnl']:+,.2f}")


if __name__ == "__main__":
    main()
