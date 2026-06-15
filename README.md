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
| CVS | 27.0 | $75.83 | $100.68 | $2,718.36 | +$670.99 | +32.8% |
| NUE | 9.0 | $223.00 | $260.00 | $2,340.00 | +$333.00 | +16.6% |
| CCI | 20.0 | $84.31 | $88.74 | $1,774.80 | +$88.60 | +5.2% |
| NVDA | 8.0 | $211.61 | $211.51 | $1,692.07 | $-0.79 | -0.1% |
| MU | 1.0 | $919.03 | $1,080.50 | $1,080.50 | +$161.47 | +17.6% |
| ARM | 2.0 | $323.12 | $406.08 | $812.16 | +$165.92 | +25.7% |
| BA | 3.0 | $220.33 | $228.39 | $685.17 | +$24.18 | +3.7% |
| GE | 2.0 | $285.99 | $342.26 | $684.52 | +$112.54 | +19.7% |
| TJX | 4.0 | $159.00 | $167.33 | $669.32 | +$33.32 | +5.2% |
| MRVL | 2.0 | $275.75 | $304.00 | $608.00 | +$56.51 | +10.2% |
| AMD | 1.0 | $512.00 | $545.12 | $545.12 | +$33.12 | +6.5% |
| TSM | 1.0 | $417.29 | $439.60 | $439.60 | +$22.31 | +5.3% |
| SYY | 5.0 | $73.21 | $79.69 | $398.45 | +$32.39 | +8.8% |
| GD | 1.0 | $359.71 | $359.53 | $359.53 | $-0.18 | -0.1% |
| UNH | 0.689655172 | $290.00 | $410.75 | $283.28 | +$83.28 | +41.6% |
| D | 4.0 | $68.82 | $68.15 | $272.60 | $-2.68 | -1.0% |
| INTC | 2.0 | $117.61 | $125.80 | $251.60 | +$16.38 | +7.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $66,205.94 | $228.40 | $-16.08 | -6.6% |
| CSCO | 1.0 | $117.34 | $120.19 | $120.19 | +$2.85 | +2.4% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,774.06  
**Cash:** $15,810.39  
**Total P&L:** +$1,817.12 (+12.8%)  
**Positions:** 20  
*Last updated: 2026-06-15T23:06:43.003097+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| AMD | sell | 1 | - | stop | 2026-06-15 20:18 | new |
| NVDA | sell | 8 | - | stop | 2026-06-15 20:18 | new |
| ARM | sell | 2 | - | stop | 2026-06-15 20:18 | new |
| MU | sell | 1 | - | stop | 2026-06-15 20:18 | new |
| MRVL | sell | 2 | - | stop | 2026-06-15 17:10 | new |
| ARM | sell | 2 | - | stop | 2026-06-15 17:10 | pending_replace |
| MU | sell | 1 | - | stop | 2026-06-15 17:10 | pending_replace |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| INTC | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| AMD | sell | 1 | - | stop | 2026-06-12 13:59 | pending_replace |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| TSM | sell | 1 | - | stop | 2026-06-10 13:59 | new |
| NVDA | sell | 8 | - | stop | 2026-06-08 13:55 | pending_replace |
| CSCO | sell | 1 | - | stop | 2026-06-05 13:56 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| CCI | sell | 20 | - | stop | 2026-06-05 13:56 | new |
| NUE | sell | 9 | - | stop | 2026-06-05 13:56 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$227.40 | 78 |
| 2 | @nivychu | 1 | 0% | $-16.09 | 78 |

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
