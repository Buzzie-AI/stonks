# Stonks — Open Source Investment Portfolio

A community-managed investment portfolio where **anyone can propose trades via Pull Requests**. Supports both **stocks and cryptocurrency**. An AI evaluates every pitch, the community votes, and approved trades execute automatically with real money through Alpaca.

## How It Works

```
You open a PR → Claude scores your pitch → Community reviews → PR merged → Trade executes → Portfolio updates
```

1. **Submit a trade proposal** — Fork the repo, open a PR with the template (ticker, action, asset class, and your investment thesis).
2. **AI evaluation** — A GitHub Action calls the Claude API to score your pitch on 5 dimensions (0–100).
3. **Community review** — Maintainers and contributors discuss, ask questions, and approve.
4. **Trade execution** — Once merged with score >= 65 and 2+ approvals, the trade executes via Alpaca's live API.
5. **Portfolio tracking** — Holdings and performance update daily (stocks and crypto).

## Live Portfolio

<!-- PORTFOLIO_START -->
| Symbol | Qty | Avg Cost | Current | Market Value | P&L | Return |
|--------|-----|----------|---------|-------------|-----|--------|
| PONY | 420.0 | $18.05 | $14.34 | $6,022.80 | $-1,558.48 | -20.6% |
| NVDA | 30.0 | $182.20 | $177.19 | $5,315.70 | $-150.40 | -2.8% |
| FIG | 100.0 | $48.18 | $29.39 | $2,939.00 | $-1,879.00 | -39.0% |
| NVTS | 300.0 | $14.97 | $9.00 | $2,700.00 | $-1,789.83 | -39.9% |
| BBAI | 500.0 | $5.92 | $3.96 | $1,980.00 | $-977.58 | -33.0% |
| HOOD | 25.0 | $126.69 | $75.85 | $1,896.25 | $-1,270.93 | -40.1% |
| QUBT | 50.0 | $22.67 | $8.41 | $420.50 | $-712.83 | -62.9% |
| RGTI | 20.0 | $51.88 | $17.42 | $348.40 | $-689.20 | -66.4% |
| INTS | 40.0 | $19.24 | $7.66 | $306.40 | $-463.30 | -60.2% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $24,578.20  
**Cash:** $2,649.15  
**Total P&L:** $-9,491.55 (-30.2%)  
**Positions:** 10  
*Last updated: 2026-03-01T20:25:38.208545+00:00*

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
No contributors yet. Submit a PR to get on the leaderboard!

<!-- LEADERBOARD_END -->

## Quick Start

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/stonks.git
cd stonks
git checkout -b trade/AAPL-BUY      # stocks
git checkout -b trade/BTC-USD-BUY   # crypto

# Open a PR using the template — fill in the YAML block and write your pitch
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details on writing a strong proposal.

**Using an AI assistant?** Point it at [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md) — it has everything your AI needs to research tickers, write pitches, and open PRs for you.

## Safety Guardrails

This is live trading. The following guardrails are enforced automatically:

- **Position size and approvals** vary by contributor rank (see table below)
- **3 trades/day** maximum
- **AI score >= 65** required
- **Penny stocks banned** (stocks under $5)
- **Dust tokens banned** (crypto under $0.001)
- **Banned tickers list** maintained in `config/banned_tickers.txt`
- Every order is validated for buying power and ticker existence before execution

### Contributor Ranks

Build a track record to unlock higher trade limits and fewer approval requirements:

| Rank | Requirements | Max Trade | Approvals Needed |
|------|-------------|-----------|-----------------|
| Rookie | First trade | $500 | 2 |
| Analyst | 3+ trades, >50% win rate | $500 | 1 |
| Strategist | 5+ trades, >60% win rate | $750 | 2 |
| Portfolio Manager | 10+ trades, >65% win rate, positive P&L | $1,000 | 1 |

Ranks refresh after every trade and during the daily portfolio update.

All parameters are configurable in `config/config.yml`.

## Repo Structure

```
├── .github/workflows/     # evaluate → execute → portfolio update + leaderboard
├── scripts/               # Python: parse, evaluate, trade, update, leaderboard
├── config/                # config.yml + banned tickers
├── data/                  # portfolio.json, trade_history.json, contributors.json
├── CONTRIBUTING.md        # How to submit a trade + rank system
└── README.md              # You are here
```

## Secrets Required

Set these in your repo's **Settings → Secrets and variables → Actions**:

| Secret | Description |
|--------|-------------|
| `ALPACA_API_KEY` | Alpaca live trading API key |
| `ALPACA_SECRET_KEY` | Alpaca live trading secret |
| `ANTHROPIC_API_KEY` | Claude API key for pitch evaluation |

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

## Important Disclaimers

**No compensation.** Contributors who submit trade proposals do not receive any financial compensation, profit-sharing, or payment of any kind. The only reward is bragging rights and community recognition.

**No liability.** The Alpaca account owner(s) are not liable to pay contributors for their proposals, analysis, or any form of consultation. By submitting a PR, you acknowledge that your contribution is voluntary and uncompensated.

**Real capital at risk.** This portfolio trades with real money. Past performance does not guarantee future results. All investments carry risk of loss. Community approval is not professional financial advice. Understand the risks before proposing or approving trades.

---

Built with [Alpaca](https://alpaca.markets), [Claude](https://anthropic.com), and GitHub Actions.
