#!/usr/bin/env python3
"""
One-time utility to backfill github_username on trade_history entries
that are missing it. Looks up PR author via GitHub API.

Usage:
    python scripts/backfill_usernames.py --repo owner/repo
    python scripts/backfill_usernames.py --repo owner/repo --history data/trade_history.json
"""

import argparse
import json
import os
import sys
from pathlib import Path

import requests


def fetch_pr_author(repo: str, pr_number: int) -> str:
    """Look up the author of a PR via GitHub API."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get("user", {}).get("login", "")


def main():
    parser = argparse.ArgumentParser(
        description="Backfill github_username in trade history"
    )
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument(
        "--history",
        default="data/trade_history.json",
        help="Path to trade_history.json",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print changes without writing",
    )
    args = parser.parse_args()

    if not Path(args.history).exists():
        print(f"No trade history file found at {args.history}")
        sys.exit(1)

    with open(args.history) as f:
        history = json.load(f)

    trades = history.get("trades", [])
    updated = 0

    for trade in trades:
        if trade.get("github_username"):
            continue  # Already has a username

        pr_number = trade.get("pr_number")
        if not pr_number:
            print(f"  SKIP {trade.get('id', '?')}: no pr_number")
            continue

        try:
            username = fetch_pr_author(args.repo, pr_number)
            if username:
                trade["github_username"] = username
                updated += 1
                print(f"  {trade.get('id', '?')}: PR #{pr_number} -> @{username}")
            else:
                print(f"  SKIP {trade.get('id', '?')}: PR #{pr_number} has no author")
        except Exception as e:
            print(f"  ERROR {trade.get('id', '?')}: PR #{pr_number} -> {e}")

    if updated == 0:
        print("No trades needed backfilling.")
        return

    if args.dry_run:
        print(f"\nDry run: would update {updated} trade(s). Use without --dry-run to write.")
        return

    with open(args.history, "w") as f:
        json.dump(history, f, indent=2)

    print(f"\nBackfilled {updated} trade(s) in {args.history}")


if __name__ == "__main__":
    main()
