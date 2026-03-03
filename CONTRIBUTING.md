# Contributing a Trade Proposal

## Before You Submit

1. **This is live trading.** Real money is at stake. Treat proposals seriously.
2. **Review recent trades** in `data/trade_history.json` to understand what's been executed.
3. **Check the portfolio** in `data/portfolio.json` for current holdings.
4. **Read the evaluation criteria** below — your pitch will be scored by AI on 5 dimensions.

## How to Submit

1. **Fork the repo** — Click the "Fork" button on GitHub to create your own copy. You do **not** need collaborator access; all contributions come through forks.
2. **Create a branch** named `trade/TICKER-ACTION` (e.g. `trade/AAPL-BUY` or `trade/BTC-USD-BUY` for crypto).
3. **Open a PR** from your fork back to `Buzzie-AI/stonks:main` using the provided template. Fill in both the YAML block and the markdown pitch.
4. **Wait for the AI evaluation** comment (posted automatically within minutes).
5. **Address feedback** from reviewers. Iterate on your pitch if needed.
6. Once you have **2+ approvals** and the **AI score >= 65**, a maintainer can merge.
7. Before merging, the maintainer posts a `/execute <amount>` comment (e.g. `/execute 250`) to set the trade size.
8. On merge, the trade executes automatically and results are posted to your PR.

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
- Submit dust tokens (crypto under $0.001)
- Write fewer than 200 characters
- Propose trades without substantive analysis

## Example: Strong Proposal

```yaml
ticker: "MSFT"
action: "BUY"
asset_class: "STOCK"
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

## Example: Crypto Proposal

```yaml
ticker: "BTC/USD"
action: "BUY"
asset_class: "CRYPTO"
```

### Investment Thesis

Bitcoin's fourth halving cycle (April 2024) has historically preceded 12-18 month bull runs. On-chain metrics show accumulation by long-term holders, and institutional inflows via spot ETFs are creating sustained demand pressure.

### Fundamental Analysis

- Hash rate at all-time highs (network security)
- Spot ETF daily inflows averaging $200M+
- Supply on exchanges at multi-year lows
- Post-halving supply shock reducing new issuance by 50%

### Risk Factors

- Regulatory crackdowns in major markets
- Macro risk: correlation with risk assets during liquidity crises
- Extreme volatility — 30%+ drawdowns are normal
- Concentration risk in a single digital asset

### Time Horizon & Confidence

- **Time Horizon:** Medium-term (6-12 months)
- **Confidence:** Medium — strong on-chain data, but crypto volatility is inherent

## After Your Trade Executes

- Execution details are posted as a comment on your PR
- The trade is logged in `data/trade_history.json`
- Portfolio updates daily at market close
- Your contribution is public and attributed to your GitHub username
- Your stats update on the leaderboard

## AI-Assisted Submissions

Want your AI coding assistant to submit trades for you? See [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md) for a complete guide designed to be read by Claude Code, Copilot, Cursor, and other AI tools.

## Questions?

Open a GitHub Issue or start a Discussion.
