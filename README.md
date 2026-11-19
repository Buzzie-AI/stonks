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
| REGN | 2.0 | $737.32 | $948.00 | $1,896.00 | +$421.36 | +28.6% |
| LOW | 8.0 | $217.92 | $222.78 | $1,782.24 | +$38.84 | +2.2% |
| PRVA | 60.0 | $25.71 | $24.60 | $1,476.00 | $-66.60 | -4.3% |
| TXT | 15.0 | $82.95 | $82.79 | $1,241.85 | $-2.48 | -0.2% |
| CSCO | 12.0 | $95.64 | $98.10 | $1,177.20 | +$29.46 | +2.6% |
| TTEK | 23.0 | $39.15 | $38.11 | $876.53 | $-23.80 | -2.6% |
| ABBV | 3.0 | $273.24 | $285.50 | $856.50 | +$36.79 | +4.5% |
| DIS | 6.0 | $121.16 | $122.31 | $733.86 | +$6.93 | +0.9% |
| TU | 46.0 | $9.60 | $9.51 | $437.46 | $-4.13 | -0.9% |
| SPCX | 3.0 | $144.69 | $145.10 | $435.30 | +$1.23 | +0.3% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $29,883.04  
**Cash:** $18,970.10  
**Total P&L:** +$437.60 (+4.2%)  
**Positions:** 11  
*Last updated: 2026-11-19T02:28:31.566629+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| SPCX | sell | 3 | - | stop | 2026-11-18 17:49 | new |
| LOW | sell | 8 | - | stop | 2026-11-18 15:08 | new |
| PRVA | sell | 60 | - | stop | 2026-11-18 15:08 | new |
| TXT | sell | 15 | - | stop | 2026-11-18 15:08 | new |
| DIS | sell | 6 | - | stop | 2026-11-17 15:07 | new |
| TU | sell | 46 | - | stop | 2026-11-16 15:07 | new |
| CSCO | sell | 12 | - | stop | 2026-11-13 17:48 | new |
| TTEK | sell | 23 | - | stop | 2026-11-12 17:58 | new |
| REGN | sell | 2 | - | stop | 2026-11-10 14:37 | new |
| ABBV | sell | 3 | - | stop | 2026-10-07 17:18 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$686.05 | 78 |
| 2 | @nivychu | 1 | 0% | $-28.06 | 78 |

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
