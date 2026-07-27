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
| CVS | 27.0 | $75.83 | $107.07 | $2,890.89 | +$843.52 | +41.2% |
| NVDA | 7.0 | $204.68 | $196.61 | $1,376.27 | $-56.51 | -3.9% |
| AAPL | 3.0 | $326.34 | $336.71 | $1,010.13 | +$31.12 | +3.2% |
| AVGO | 2.0 | $372.44 | $382.81 | $765.62 | +$20.74 | +2.8% |
| GE | 2.0 | $285.99 | $361.78 | $723.56 | +$151.58 | +26.5% |
| TJX | 4.0 | $159.00 | $156.38 | $625.52 | $-10.48 | -1.6% |
| SYY | 5.0 | $73.21 | $83.26 | $416.30 | +$50.24 | +13.7% |
| GD | 1.0 | $359.71 | $390.00 | $390.00 | +$30.29 | +8.4% |
| UNH | 0.689655172 | $290.00 | $417.19 | $287.72 | +$87.72 | +43.9% |
| D | 4.0 | $68.82 | $70.20 | $280.80 | +$5.52 | +2.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,662.42 | $223.08 | $-21.41 | -8.8% |
| NBIS | 1.0 | $195.76 | $188.00 | $188.00 | $-7.76 | -4.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,996.49  
**Cash:** $21,818.60  
**Total P&L:** +$1,124.56 (+14.0%)  
**Positions:** 13  
*Last updated: 2026-07-27T22:13:32.100814+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| NBIS | sell | 1 | - | stop | 2026-07-21 13:40 | new |
| AVGO | sell | 2 | - | stop | 2026-07-16 19:49 | new |
| NVDA | sell | 7 | - | stop | 2026-07-16 19:46 | new |
| AAPL | sell | 3 | - | stop | 2026-07-15 17:19 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$294.20 | 78 |
| 2 | @nivychu | 1 | 0% | $-21.62 | 78 |

<!-- LEADERBOARD_END -->

## Quick Start

All contributions come through **forks** — you don't need collaborator access.

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/stonks.git
cd stonks

# 2. Create a branch for your trade
git checkout -b trade/AAPL-BUY      # stocks
git checkout -b trade/BTC-USD-BUY   # crypto

# 3. Open a PR from your fork to Buzzie-AI/stonks:main
#    Fill in the YAML block and write your pitch using the template
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details on writing a strong proposal.

**Using an AI assistant?** Point it at [AI_INSTRUCTIONS.md](AI_INSTRUCTIONS.md) — it has everything your AI needs to research tickers, write pitches, and open PRs for you.

## Safety Guardrails

This is live trading. The following guardrails are enforced automatically:

- **Trade size** set by maintainer via `/execute <amount>` comment before merge
- **2+ approvals** required
- **3 trades/day** maximum
- **AI score >= 65** required
- **Penny stocks banned** (stocks under $5)
- **Dust tokens banned** (crypto under $0.001)
- **Banned tickers list** maintained in `config/banned_tickers.txt`
- Every order is validated for buying power and ticker existence before execution

All parameters are configurable in `config/config.yml`.

## Repo Structure

```
├── .github/workflows/     # evaluate → execute → portfolio update + leaderboard
├── scripts/               # Python: parse, evaluate, trade, update, leaderboard
├── config/                # config.yml + banned tickers
├── data/                  # portfolio.json, trade_history.json
├── CONTRIBUTING.md        # How to submit a trade
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
