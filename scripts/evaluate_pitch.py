#!/usr/bin/env python3
"""
Evaluates a trade pitch using the Claude API.
Scores the proposal on 5 dimensions (100 points total), detects red flags,
and outputs a structured evaluation result.

Usage:
    python scripts/evaluate_pitch.py --proposal /tmp/trade_proposal.json --config config/config.yml
    # Writes /tmp/evaluation_result.json
"""

import argparse
import json
import sys
from datetime import datetime, timezone

import anthropic
import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_proposal(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


SYSTEM_PROMPT = """\
You are a senior investment analyst evaluating trade proposals for a community-managed \
investment portfolio (stocks and cryptocurrency). You are rigorous, data-driven, and \
skeptical of hype. Your job is to score each proposal fairly and identify risks the \
author may have missed.

You MUST respond with valid JSON only — no markdown, no commentary outside the JSON."""

EVAL_PROMPT_TEMPLATE = """\
Evaluate this trade proposal and return a JSON object.

PROPOSAL
--------
Ticker: {ticker}
Action: {action}
Asset Class: {asset_class}
Suggested Amount: {amount}

PITCH
-----
{pitch_text}

SCORING RUBRIC (100 points total)
----------------------------------
1. pitch_quality (0-20): Is the pitch clear, well-structured, and logically coherent?
2. fundamental_analysis (0-25): Does it cite earnings, revenue, competitive position, or catalysts? \
For crypto, consider on-chain metrics, adoption data, protocol fundamentals, and tokenomics.
3. risk_assessment (0-20): Does it honestly acknowledge what could go wrong?
4. market_outlook (0-20): Are the price target and time horizon realistic?
5. strategy_alignment (0-15): Does this trade make sense for a diversified portfolio?

RED FLAGS to check for:
- Speculative language without data ("moonshot", "guaranteed", "can't lose")
- No risk acknowledgment at all
- Unrealistic return expectations (>100% in short term)
- Purely emotional reasoning
{red_flag_extras}
Return this exact JSON structure:
{{
    "score": <int 0-100, sum of all dimensions>,
    "sentiment": "<bullish|neutral|bearish>",
    "recommendation": "<STRONG_BUY|BUY|HOLD|SELL|STRONG_SELL|REJECT>",
    "dimensions": {{
        "pitch_quality": <int 0-20>,
        "fundamental_analysis": <int 0-25>,
        "risk_assessment": <int 0-20>,
        "market_outlook": <int 0-20>,
        "strategy_alignment": <int 0-15>
    }},
    "red_flags": ["<list of detected issues, empty if none>"],
    "detailed_analysis": "<2-3 paragraph assessment explaining the score>"
}}"""

STOCK_RED_FLAGS = """\
- Penny stock or highly volatile ticker (under $5)
"""

CRYPTO_RED_FLAGS = """\
- Extremely low-liquidity or micro-cap token
- No clear utility or adoption beyond speculation
- Excessive volatility without acknowledgment
"""


def evaluate(proposal: dict, config: dict) -> dict:
    """Call Claude API to evaluate the pitch."""
    client = anthropic.Anthropic()

    model = config.get("anthropic", {}).get("model", "claude-sonnet-4-5-20250929")
    amount = proposal.get("suggested_amount") or "Not specified (default $500 max)"
    asset_class = proposal.get("asset_class", "STOCK")
    red_flag_extras = CRYPTO_RED_FLAGS if asset_class == "CRYPTO" else STOCK_RED_FLAGS

    prompt = EVAL_PROMPT_TEMPLATE.format(
        ticker=proposal["ticker"],
        action=proposal["action"],
        asset_class=asset_class,
        amount=amount,
        pitch_text=proposal["pitch_text"],
        red_flag_extras=red_flag_extras,
    )

    message = client.messages.create(
        model=model,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = message.content[0].text

    # Parse JSON from response — handle potential markdown wrapping
    text = response_text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]  # remove opening ```json
        text = text.rsplit("```", 1)[0]  # remove closing ```

    try:
        result = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse Claude response as JSON: {e}")
        print(f"Raw response:\n{response_text}")
        sys.exit(1)

    # Validate score is sum of dimensions
    dims = result.get("dimensions", {})
    expected_score = sum(dims.values())
    if result.get("score") != expected_score:
        result["score"] = expected_score

    return result


def main():
    parser = argparse.ArgumentParser(description="Evaluate trade pitch with Claude")
    parser.add_argument("--proposal", required=True, help="Path to trade_proposal.json")
    parser.add_argument("--config", required=True, help="Path to config.yml")
    parser.add_argument("--output", default="/tmp/evaluation_result.json")
    args = parser.parse_args()

    config = load_config(args.config)
    proposal = load_proposal(args.proposal)

    # Skip evaluation if proposal itself is invalid
    if not proposal.get("is_valid"):
        result = {
            "score": 0,
            "sentiment": "neutral",
            "recommendation": "REJECT",
            "dimensions": {
                "pitch_quality": 0,
                "fundamental_analysis": 0,
                "risk_assessment": 0,
                "market_outlook": 0,
                "strategy_alignment": 0,
            },
            "red_flags": proposal.get("validation_errors", []),
            "detailed_analysis": "Proposal failed validation. See red_flags for details.",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ticker": proposal.get("ticker", "UNKNOWN"),
            "action": proposal.get("action", "UNKNOWN"),
        }
    else:
        result = evaluate(proposal, config)
        result["timestamp"] = datetime.now(timezone.utc).isoformat()
        result["ticker"] = proposal["ticker"]
        result["action"] = proposal["action"]

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Evaluation complete — Score: {result['score']}/100 | {result['recommendation']}")
    min_score = config.get("safety", {}).get("min_ai_score", 65)
    if result["score"] < min_score:
        print(f"Below minimum threshold ({min_score}). Trade will NOT be eligible.")


if __name__ == "__main__":
    main()
