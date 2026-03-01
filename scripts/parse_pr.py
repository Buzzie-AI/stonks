#!/usr/bin/env python3
"""
Parses a PR body to extract the YAML trade details and markdown pitch.
Outputs structured JSON for downstream evaluation and execution.

Usage:
    python scripts/parse_pr.py --pr-number 42 --repo owner/repo
    # Reads PR body via GitHub API, writes /tmp/trade_proposal.json
"""

import argparse
import json
import os
import re
import sys
import requests


def fetch_pr_body(repo: str, pr_number: int) -> str:
    """Fetch PR body from GitHub API."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get("body", "")


def fetch_pr_reviews(repo: str, pr_number: int) -> int:
    """Count the number of approved reviews on a PR."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/reviews"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    reviews = resp.json()
    approved = [r for r in reviews if r.get("state") == "APPROVED"]
    # Deduplicate by user — only count latest review per user
    seen_users = set()
    unique_approvals = 0
    for review in reversed(approved):
        user = review.get("user", {}).get("login", "")
        if user not in seen_users:
            seen_users.add(user)
            unique_approvals += 1
    return unique_approvals


def parse_yaml_block(body: str) -> dict:
    """Extract the YAML code block from the PR body."""
    pattern = r"```yaml\s*\n(.*?)```"
    match = re.search(pattern, body, re.DOTALL)
    if not match:
        return {}

    yaml_text = match.group(1).strip()
    result = {}
    for line in yaml_text.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                result[key] = value
    return result


def extract_pitch_text(body: str) -> str:
    """Extract the markdown pitch (everything outside the YAML block)."""
    # Remove the YAML code block
    cleaned = re.sub(r"```yaml\s*\n.*?```", "", body, flags=re.DOTALL)
    # Remove HTML comments
    cleaned = re.sub(r"<!--.*?-->", "", cleaned, flags=re.DOTALL)
    # Remove checklist section
    cleaned = re.sub(r"### Checklist.*", "", cleaned, flags=re.DOTALL)
    return cleaned.strip()


def validate_proposal(yaml_data: dict, pitch_text: str) -> list[str]:
    """Validate the trade proposal. Returns list of errors (empty = valid)."""
    errors = []

    if not yaml_data.get("ticker"):
        errors.append("Missing required field: ticker")
    if not yaml_data.get("action"):
        errors.append("Missing required field: action")
    elif yaml_data["action"].upper() not in ("BUY", "SELL"):
        errors.append(f"Invalid action: {yaml_data['action']}. Must be BUY or SELL.")

    asset_class = yaml_data.get("asset_class", "STOCK").upper()
    if asset_class not in ("STOCK", "CRYPTO"):
        errors.append(f"Invalid asset_class: {asset_class}. Must be STOCK or CRYPTO.")

    if len(pitch_text) < 200:
        errors.append(
            f"Pitch too short ({len(pitch_text)} chars). Minimum 200 characters required."
        )

    if yaml_data.get("suggested_amount"):
        try:
            amount = float(yaml_data["suggested_amount"])
            if amount > 500:
                errors.append(
                    f"Suggested amount ${amount} exceeds max of $500 per trade."
                )
            if amount <= 0:
                errors.append("Suggested amount must be positive.")
        except ValueError:
            errors.append(f"Invalid suggested_amount: {yaml_data['suggested_amount']}")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Parse PR trade proposal")
    parser.add_argument("--pr-number", type=int, required=True)
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--output", default="/tmp/trade_proposal.json")
    args = parser.parse_args()

    # Fetch PR body
    body = fetch_pr_body(args.repo, args.pr_number)
    if not body:
        print("ERROR: PR body is empty")
        sys.exit(1)

    # Parse structured data
    yaml_data = parse_yaml_block(body)
    pitch_text = extract_pitch_text(body)
    approval_count = fetch_pr_reviews(args.repo, args.pr_number)

    # Validate
    errors = validate_proposal(yaml_data, pitch_text)

    proposal = {
        "pr_number": args.pr_number,
        "repo": args.repo,
        "ticker": yaml_data.get("ticker", "").upper(),
        "action": yaml_data.get("action", "").upper(),
        "asset_class": yaml_data.get("asset_class", "STOCK").upper(),
        "suggested_amount": yaml_data.get("suggested_amount"),
        "pitch_text": pitch_text,
        "approval_count": approval_count,
        "validation_errors": errors,
        "is_valid": len(errors) == 0,
    }

    with open(args.output, "w") as f:
        json.dump(proposal, f, indent=2)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(
            f"Parsed proposal: {proposal['action']} {proposal['ticker']} "
            f"[{proposal['asset_class']}] (approvals: {approval_count})"
        )


if __name__ == "__main__":
    main()
