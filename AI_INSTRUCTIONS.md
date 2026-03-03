# AI Trade Submission Instructions

This file is designed to be read by AI coding assistants (Claude Code, Copilot, Cursor, etc.) to help you submit trade proposals to the Stonks portfolio.

**Point your AI at this file:** "Read AI_INSTRUCTIONS.md and submit a trade for me."

---

## What This Repo Does

This is a community-managed investment portfolio that trades real money. Anyone can propose a trade by opening a Pull Request. An AI (Claude) scores the pitch, the community reviews it, and if it passes (score >= 65, enough approvals), the trade executes automatically via Alpaca.

## Step-by-Step: Submit a Trade

### 1. Gather Context

Before writing a proposal, read these files to understand the current state:

- **`data/portfolio.json`** — Current holdings, cash, buying power. Check what positions already exist to avoid over-concentration and to argue for strategy alignment.
- **`data/trade_history.json`** — Past trades. See what's been bought/sold recently.
- **`config/banned_tickers.txt`** — Never propose a ticker on this list.
- **`config/config.yml`** — Safety limits, evaluation rubric weights.

### 2. Create a Branch

```
trade/TICKER-ACTION
```

Examples: `trade/AAPL-BUY`, `trade/BTC-USD-BUY`, `trade/MSFT-SELL`

### 3. Open a PR With This Exact Format

The PR body must contain a YAML code block and markdown sections. Use this structure:

````markdown
```yaml
ticker: "AAPL"           # Stock symbol, or slash format for crypto: BTC/USD, ETH/USD
action: "BUY"            # BUY or SELL
asset_class: "STOCK"     # STOCK or CRYPTO
```

## Investment Thesis

[Why should the portfolio make this trade? Be specific and data-driven. This is the most important section.]

## Fundamental Analysis

[Hard numbers: earnings, revenue, P/E, growth rates, market share, moat. For crypto: on-chain metrics, adoption data, tokenomics, hash rate, TVL.]

## Technical Analysis (optional)

[Price levels, moving averages, volume patterns, support/resistance.]

## Risk Factors

[What could go wrong? Every strong pitch acknowledges downside. Be honest — the AI evaluator penalizes pitches that ignore risk.]

## Time Horizon & Confidence

- **Time Horizon:** Short-term (1-3 mo) / Medium-term (3-12 mo) / Long-term (1+ yr)
- **Confidence:** High / Medium / Low
````

### 4. Important Constraints

| Rule | Detail |
|------|--------|
| **Minimum pitch length** | 200 characters (the markdown sections, not counting YAML) |
| **Allowed actions** | `BUY` or `SELL` only |
| **Allowed asset classes** | `STOCK` or `CRYPTO` only |
| **Penny stocks banned** | No stocks trading under $5 |
| **Dust tokens banned** | No crypto under $0.001 |
| **Banned tickers** | Check `config/banned_tickers.txt` before proposing |
| **Crypto ticker format** | Use slash format in YAML: `BTC/USD`, `ETH/USD`, `SOL/USD` |

### 5. What the AI Evaluator Scores (100 points)

Your pitch is scored on 5 dimensions. Optimize for all of them:

| Dimension | Points | What to include |
|-----------|--------|-----------------|
| **Pitch Quality** | 20 | Clear structure, logical flow, well-written prose |
| **Fundamental Analysis** | 25 | Earnings, revenue, P/E, growth metrics, competitive moat, specific catalysts. For crypto: on-chain data, adoption metrics, tokenomics |
| **Risk Assessment** | 20 | Honest downside risks, what could go wrong, risk mitigation |
| **Market Outlook** | 20 | Realistic price targets, reasonable time horizon, macro context |
| **Strategy Alignment** | 15 | How this fits the existing portfolio — check `data/portfolio.json` for current positions |

**Minimum passing score: 65/100**

### 6. Red Flags That Kill Your Score

The evaluator is trained to reject pitches with these patterns:

- Speculative language: "moonshot", "guaranteed", "can't lose", "to the moon"
- No risk acknowledgment
- Unrealistic return expectations (>100% short-term)
- Penny stocks (under $5)
- Low-liquidity crypto with no utility
- Vague thesis without data ("this stock is good")
- Ignoring current portfolio composition

## Tips for High-Scoring Proposals

1. **Lead with numbers.** The Fundamental Analysis dimension is worth the most points (25). Include specific financial metrics, not opinions.
2. **Be honest about risk.** A pitch that says "this could drop 20% if earnings miss" scores higher than one that ignores downside entirely.
3. **Check the portfolio first.** If the portfolio already holds 3 tech stocks, proposing a 4th tech stock hurts your Strategy Alignment score. Argue for diversification or explain why concentration is justified.
4. **Cite catalysts with dates.** "Earnings report on March 15" or "FDA approval expected Q2" is much stronger than "good company with growth potential."
5. **State your time horizon clearly.** The evaluator wants to know when you expect the thesis to play out.
6. **Use real data.** Web search for current financials, recent earnings, analyst estimates. Stale or made-up numbers will be flagged.

## Example Prompt for Your AI

> Read AI_INSTRUCTIONS.md, then check the current portfolio in data/portfolio.json and recent trades in data/trade_history.json. Research [TICKER] and write a trade proposal PR for a [BUY/SELL]. Make sure the pitch scores well on all 5 evaluation dimensions. Create the branch and open the PR.
