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
| CVS | 27.0 | $75.83 | $98.32 | $2,654.64 | +$607.27 | +29.7% |
| NUE | 9.0 | $223.00 | $243.83 | $2,194.47 | +$187.47 | +9.3% |
| NVDA | 8.0 | $211.61 | $210.69 | $1,685.52 | $-7.33 | -0.4% |
| ARM | 3.0 | $364.31 | $439.46 | $1,318.38 | +$225.44 | +20.6% |
| AMD | 2.0 | $520.61 | $537.37 | $1,074.74 | +$33.52 | +3.2% |
| MRVL | 3.0 | $291.75 | $310.58 | $931.74 | +$56.51 | +6.5% |
| GE | 2.0 | $285.99 | $357.64 | $715.28 | +$143.30 | +25.1% |
| BA | 3.0 | $220.33 | $222.72 | $668.16 | +$7.17 | +1.1% |
| TJX | 4.0 | $159.00 | $163.81 | $655.24 | +$19.24 | +3.0% |
| TSM | 1.0 | $417.29 | $462.12 | $462.12 | +$44.83 | +10.7% |
| SYY | 5.0 | $73.21 | $78.70 | $393.50 | +$27.44 | +7.5% |
| GD | 1.0 | $359.71 | $350.01 | $350.01 | $-9.71 | -2.7% |
| UNH | 0.689655172 | $290.00 | $400.96 | $276.52 | +$76.52 | +38.3% |
| D | 4.0 | $68.82 | $68.41 | $273.64 | $-1.64 | -0.6% |
| BTCUSD | 0.003449908 | $70,867.17 | $63,035.47 | $217.47 | $-27.02 | -11.1% |
| CSCO | 1.0 | $117.34 | $119.54 | $119.54 | +$2.20 | +1.9% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,499.50  
**Cash:** $17,508.53  
**Total P&L:** +$1,385.21 (+11.0%)  
**Positions:** 17  
*Last updated: 2026-06-19T22:11:08.255155+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TSM | sell | 1 | - | stop | 2026-06-18 17:18 | new |
| NVDA | sell | 8 | - | stop | 2026-06-18 17:18 | new |
| MRVL | sell | 3 | - | stop | 2026-06-18 15:04 | new |
| ARM | sell | 3 | - | stop | 2026-06-18 15:04 | new |
| AMD | sell | 2 | - | stop | 2026-06-18 14:35 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| CSCO | sell | 1 | - | stop | 2026-06-05 13:56 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$236.90 | 78 |
| 2 | @nivychu | 1 | 0% | $-27.37 | 78 |

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
