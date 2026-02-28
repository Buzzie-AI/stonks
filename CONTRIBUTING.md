# Contributing a Trade Proposal

## Before You Submit

1. **This is paper trading (sandbox).** No real money at risk, but treat proposals seriously — this is practice for the live branch.
2. **Review recent trades** in `data/trade_history.json` to understand what's been executed.
3. **Check the portfolio** in `data/portfolio.json` for current holdings.
4. **Read the evaluation criteria** below — your pitch will be scored by AI on 5 dimensions.

## How to Submit

1. Fork the repo and create a branch named `trade/TICKER-ACTION` (e.g. `trade/AAPL-BUY`).
2. Open a PR using the provided template. Fill in both the YAML block and the markdown pitch.
3. Wait for the AI evaluation comment (posted automatically within minutes).
4. Address any feedback from reviewers. Iterate on your pitch if needed.
5. Once you have 2+ approvals and the AI score is >= 65, a maintainer can merge.
6. On merge, the trade executes automatically and results are posted to your PR.

## Evaluation Criteria (100 points)

| Dimension             | Points | What the AI looks for                                  |
|-----------------------|--------|--------------------------------------------------------|
| Pitch Quality         | 20     | Clear structure, well-written, logical flow             |
| Fundamental Analysis  | 25     | Earnings, revenue, moat, catalysts — data over opinion |
| Risk Assessment       | 20     | Honest downside acknowledgment, not just bull case      |
| Market Outlook        | 20     | Realistic targets, reasonable time horizon               |
| Strategy Alignment    | 15     | Does this fit the portfolio's existing positions?        |

**Minimum score to proceed: 65/100**

## Writing a Strong Pitch

**Do:**
- Lead with data (earnings, P/E, revenue growth, market share)
- Cite specific catalysts (product launch, earnings date, regulatory change)
- Acknowledge what could go wrong
- State a clear time horizon and price target
- Explain why *now* is the right entry point

**Don't:**
- Use hype language ("moonshot", "guaranteed", "can't lose")
- Ignore downside risk
- Submit penny stocks (under $5) or banned tickers
- Write fewer than 200 characters
- Propose more than $500 per trade

## Example: Strong Proposal

```yaml
ticker: "MSFT"
action: "BUY"
suggested_amount: 400
```

### Investment Thesis

Microsoft is well-positioned in the enterprise AI infrastructure cycle. Azure revenue grew 29% YoY in the latest quarter, and the Copilot product line is driving incremental SaaS revenue across Office 365.

### Fundamental Analysis

- TTM EPS: $11.50 (10.2% YoY growth)
- P/E: 32x (premium but justified by growth)
- Free cash flow: $65B annually
- AI capital expenditure yielding measurable ROI in enterprise contracts

### Risk Factors

- Cloud spending deceleration if macro weakens
- AI competition from Google Cloud and AWS
- Regulatory scrutiny on AI and antitrust
- Valuation compression in a rate-rising environment

### Time Horizon & Confidence

- **Time Horizon:** Medium-term (6-12 months)
- **Confidence:** Medium — strong fundamentals, but macro uncertainty

## After Your Trade Executes

- Execution details are posted as a comment on your PR
- The trade is logged in `data/trade_history.json`
- Portfolio updates daily at market close
- Your contribution is public and attributed to your GitHub username

## Questions?

Open a GitHub Issue or start a Discussion.
