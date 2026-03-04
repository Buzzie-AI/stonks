#!/usr/bin/env python3
"""
Fetches current positions from Alpaca, updates portfolio.json,
and regenerates the portfolio section in README.md.

Usage:
    python scripts/update_portfolio.py --config config/config.yml
"""

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def fetch_portfolio(client: TradingClient) -> dict:
    """Fetch account info and all open positions."""
    account = client.get_account()
    positions = client.get_all_positions()

    pos_list = []
    for p in positions:
        current_price = float(p.current_price) if p.current_price is not None else float(p.avg_entry_price)
        market_value = float(p.market_value) if p.market_value is not None else current_price * float(p.qty)
        unrealized_pl = float(p.unrealized_pl) if p.unrealized_pl is not None else 0.0
        unrealized_plpc = round(float(p.unrealized_plpc) * 100, 2) if p.unrealized_plpc is not None else 0.0
        pos_list.append(
            {
                "symbol": p.symbol,
                "qty": float(p.qty),
                "avg_entry_price": float(p.avg_entry_price),
                "current_price": current_price,
                "market_value": market_value,
                "unrealized_pl": unrealized_pl,
                "unrealized_plpc": unrealized_plpc,
                "side": str(p.side),
            }
        )

    # Sort by market value descending
    pos_list.sort(key=lambda x: x["market_value"], reverse=True)

    total_value = sum(p["market_value"] for p in pos_list)
    total_pl = sum(p["unrealized_pl"] for p in pos_list)
    cost_basis = total_value - total_pl
    total_plpc = round((total_pl / cost_basis * 100), 2) if cost_basis > 0 else 0

    return {
        "positions": pos_list,
        "totals": {
            "total_value": round(total_value, 2),
            "total_pl": round(total_pl, 2),
            "total_plpc": total_plpc,
            "position_count": len(pos_list),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        },
        "account": {
            "cash": round(float(account.cash), 2),
            "portfolio_value": round(float(account.portfolio_value), 2),
            "buying_power": round(float(account.buying_power), 2),
        },
    }


def fetch_pending_orders(client: TradingClient) -> list:
    """Fetch all open/pending orders."""
    orders = client.get_orders(filter=GetOrdersRequest(status="open"))
    result = []
    for o in orders:
        result.append(
            {
                "symbol": o.symbol,
                "side": str(o.side),
                "qty": str(o.qty) if o.qty is not None else None,
                "notional": str(o.notional) if o.notional is not None else None,
                "type": str(o.type),
                "submitted_at": o.submitted_at.strftime("%Y-%m-%d %H:%M") if o.submitted_at else "",
                "status": str(o.status),
            }
        )
    return result


def generate_portfolio_table(portfolio: dict, pending_orders: list | None = None) -> str:
    """Generate a markdown table of current holdings."""
    positions = portfolio["positions"]
    totals = portfolio["totals"]
    account = portfolio["account"]

    if not positions:
        table = "No open positions yet. Submit a PR to make the first trade!\n"
    else:
        rows = ["| Symbol | Qty | Avg Cost | Current | Market Value | P&L | Return |"]
        rows.append("|--------|-----|----------|---------|-------------|-----|--------|")
        for p in positions:
            pl_sign = "+" if p["unrealized_pl"] >= 0 else ""
            ret_sign = "+" if p["unrealized_plpc"] >= 0 else ""
            rows.append(
                f"| {p['symbol']} "
                f"| {p['qty']} "
                f"| ${p['avg_entry_price']:,.2f} "
                f"| ${p['current_price']:,.2f} "
                f"| ${p['market_value']:,.2f} "
                f"| {pl_sign}${p['unrealized_pl']:,.2f} "
                f"| {ret_sign}{p['unrealized_plpc']:.1f}% |"
            )
        table = "\n".join(rows) + "\n"

    pl_sign = "+" if totals["total_pl"] >= 0 else ""
    summary = (
        f"\n**Portfolio Value:** ${account['portfolio_value']:,.2f}  \n"
        f"**Cash:** ${account['cash']:,.2f}  \n"
        f"**Total P&L:** {pl_sign}${totals['total_pl']:,.2f} "
        f"({pl_sign}{totals['total_plpc']:.1f}%)  \n"
        f"**Positions:** {totals['position_count']}  \n"
        f"*Last updated: {totals['updated_at']}*\n"
    )

    orders_section = "\n### Pending Orders\n\n"
    if pending_orders:
        order_rows = ["| Symbol | Side | Qty | Notional | Type | Submitted | Status |"]
        order_rows.append("|--------|------|-----|----------|------|-----------|--------|")
        for o in pending_orders:
            qty_display = o["qty"] if o["qty"] else "-"
            notional_display = f"${float(o['notional']):,.2f}" if o["notional"] else "-"
            order_rows.append(
                f"| {o['symbol']} "
                f"| {o['side']} "
                f"| {qty_display} "
                f"| {notional_display} "
                f"| {o['type']} "
                f"| {o['submitted_at']} "
                f"| {o['status']} |"
            )
        orders_section += "\n".join(order_rows) + "\n"
    else:
        orders_section += "*No pending orders.*\n"

    return table + summary + orders_section


def update_readme(portfolio: dict, readme_path: str = "README.md", pending_orders: list | None = None):
    """Update the portfolio section in README.md."""
    if not Path(readme_path).exists():
        return

    with open(readme_path) as f:
        content = f.read()

    table_md = generate_portfolio_table(portfolio, pending_orders)

    # Replace content between portfolio markers
    marker_start = "<!-- PORTFOLIO_START -->"
    marker_end = "<!-- PORTFOLIO_END -->"
    pattern = re.escape(marker_start) + r".*?" + re.escape(marker_end)

    replacement = f"{marker_start}\n{table_md}\n{marker_end}"

    if marker_start in content:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # If markers don't exist, append after first heading
        content += f"\n\n{replacement}\n"

    with open(readme_path, "w") as f:
        f.write(content)


def log_trade_result(execution_path: str, history_path: str):
    """Append a trade execution result to the history file."""
    if not Path(execution_path).exists():
        return

    with open(execution_path) as f:
        execution = json.load(f)

    if not execution.get("success"):
        return

    if Path(history_path).exists():
        with open(history_path) as f:
            history = json.load(f)
    else:
        history = {"trades": [], "summary": {"total_trades": 0, "successful_trades": 0, "failed_trades": 0, "total_capital_deployed": 0}}

    trade_entry = {
        "id": f"trade_{len(history['trades']) + 1:04d}",
        "pr_number": execution.get("pr_number"),
        "github_username": execution.get("github_username", ""),
        "ticker": execution["ticker"],
        "action": execution["action"],
        "quantity": execution["quantity"],
        "price": execution.get("price", 0),
        "notional": execution.get("notional", 0),
        "order_id": execution.get("order_id"),
        "executed_at": execution["executed_at"],
        "ai_score": execution.get("ai_score"),
        "approval_count": execution.get("approval_count"),
        "status": "filled",
    }

    history["trades"].append(trade_entry)
    history["summary"]["total_trades"] += 1
    history["summary"]["successful_trades"] += 1
    history["summary"]["total_capital_deployed"] += execution.get("notional", 0)

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Update portfolio state")
    parser.add_argument("--config", required=True)
    parser.add_argument(
        "--log-trade",
        help="Path to trade_execution.json to log (optional)",
        default=None,
    )
    args = parser.parse_args()

    config = load_config(args.config)

    api_key = os.environ["ALPACA_API_KEY"]
    secret_key = os.environ["ALPACA_SECRET_KEY"]
    is_paper = config.get("alpaca", {}).get("paper", False)
    client = TradingClient(api_key, secret_key, paper=is_paper)

    # Log trade if provided
    if args.log_trade:
        history_path = config.get("logging", {}).get(
            "trade_history_file", "data/trade_history.json"
        )
        log_trade_result(args.log_trade, history_path)

    # Fetch and write portfolio
    portfolio = fetch_portfolio(client)
    portfolio_path = config.get("logging", {}).get(
        "portfolio_file", "data/portfolio.json"
    )

    with open(portfolio_path, "w") as f:
        json.dump(portfolio, f, indent=2)

    # Fetch pending orders and update README
    pending_orders = fetch_pending_orders(client)
    update_readme(portfolio, pending_orders=pending_orders)

    print(
        f"Portfolio updated: {portfolio['totals']['position_count']} positions, "
        f"value ${portfolio['account']['portfolio_value']:,.2f}"
    )


if __name__ == "__main__":
    main()
