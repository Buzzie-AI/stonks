# Contributing a Trade Proposal

## Before You Submit

1. **This is live trading.** Real money is at stake. Treat proposals seriously.
2. **Review recent trades** in `data/trade_history.json` to understand what's been executed.
3. **Check the portfolio** in `data/portfolio.json` for current holdings.
4. **Read the evaluation criteria** below — your pitch will be scored by AI on 5 dimensions.

## How to Submit

1. Fork the repo and create a branch named `trade/TICKER-ACTION` (e.g. `trade/AAPL-BUY` or `trade/BTC-USD-BUY` for crypto).
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
- Submit dust tokens (crypto under $0.001)
- Write fewer than 200 characters
- Propose more than $1,000 per trade (actual cap depends on your rank)

## Example: Strong Proposal

```yaml
ticker: "MSFT"
action: "BUY"
asset_class: "STOCK"
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

## Example: Crypto Proposal

```yaml
ticker: "BTC/USD"
action: "BUY"
asset_class: "CRYPTO"
suggested_amount: 500
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
- Your rank and stats update on the leaderboard

## Contributor Ranks

Every contributor starts as a **Rookie** and can rank up based on their track record. Higher ranks unlock perks like larger trade sizes and fewer approval requirements.

| Rank | Requirements | Perks |
|------|-------------|-------|
| **Rookie** | First trade | $500 max trade, 2 approvals required |
| **Analyst** | 3+ trades, >50% win rate | $500 max trade, 1 approval required |
| **Strategist** | 5+ trades, >60% win rate | $750 max trade, 2 approvals required |
| **Portfolio Manager** | 10+ trades, >65% win rate, positive P&L | $1,000 max trade, 1 approval required |

**How ranks work:**
- Ranks refresh after every trade execution and during the daily portfolio update
- Win rate is calculated from BUY trades only (profit = current price vs. entry price)
- SELL trades count toward your trade total but not your win rate
- All rank thresholds are configured in `config/config.yml`
- Your current rank and stats are visible on the [Leaderboard](README.md#contributor-leaderboard)

## Questions?

Open a GitHub Issue or start a Discussion.
