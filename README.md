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
| CVS | 27.0 | $75.83 | $97.25 | $2,625.75 | +$578.38 | +28.2% |
| BILL | 64.0 | $40.17 | $39.49 | $2,527.36 | $-43.80 | -1.7% |
| MU | 3.0 | $541.11 | $782.62 | $2,347.86 | +$724.53 | +44.6% |
| BLK | 2.0 | $1,057.92 | $1,102.84 | $2,205.68 | +$89.84 | +4.2% |
| NUE | 9.0 | $223.00 | $232.85 | $2,095.65 | +$88.65 | +4.4% |
| MRK | 18.0 | $112.47 | $112.33 | $2,021.97 | $-2.44 | -0.1% |
| CCI | 20.0 | $84.31 | $87.31 | $1,746.20 | +$60.00 | +3.6% |
| MRVL | 9.0 | $159.53 | $183.25 | $1,649.25 | +$213.44 | +14.9% |
| TXN | 5.0 | $272.82 | $309.00 | $1,545.00 | +$180.88 | +13.3% |
| BA | 3.0 | $231.62 | $229.75 | $689.25 | $-5.60 | -0.8% |
| AMAT | 1.0 | $441.47 | $443.99 | $443.99 | +$2.52 | +0.6% |
| SYY | 5.0 | $73.21 | $73.31 | $366.55 | +$0.49 | +0.1% |
| BTCUSD | 0.003449908 | $70,867.17 | $81,467.55 | $281.06 | +$36.57 | +15.0% |
| UNH | 0.689655172 | $290.00 | $398.90 | $275.10 | +$75.10 | +37.5% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $26,643.21  
**Cash:** $5,822.54  
**Total P&L:** +$1,998.55 (+10.6%)  
**Positions:** 15  
*Last updated: 2026-05-14T22:17:18.355373+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| SYY | sell | 5 | - | stop | 2026-05-14 14:40 | new |
| BA | sell | 3 | - | stop | 2026-05-14 14:25 | new |
| MRVL | sell | 9 | - | stop | 2026-05-14 13:58 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| AMAT | sell | 1 | - | stop | 2026-05-12 11:00 | new |
| MU | sell | 3 | - | stop | 2026-05-08 17:18 | new |
| BILL | sell | 64 | - | stop | 2026-05-08 14:08 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| TXN | sell | 5 | - | stop | 2026-04-28 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$80.40 | 78 |
| 2 | @nivychu | 1 | 100% | +$37.14 | 78 |

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
