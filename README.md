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
| WMT | 15.0 | $125.31 | $129.80 | $1,947.00 | +$67.42 | +3.6% |
| REGN | 2.0 | $737.32 | $940.00 | $1,880.00 | +$405.36 | +27.5% |
| LOW | 8.0 | $217.92 | $226.14 | $1,809.12 | +$65.72 | +3.8% |
| IESC | 10.0 | $168.97 | $170.91 | $1,709.10 | +$19.35 | +1.1% |
| PRVA | 60.0 | $25.71 | $24.71 | $1,482.60 | $-60.00 | -3.9% |
| AMD | 3.0 | $445.63 | $450.00 | $1,350.00 | +$13.11 | +1.0% |
| PANW | 3.0 | $344.05 | $352.12 | $1,056.36 | +$24.21 | +2.4% |
| CRWD | 5.0 | $204.95 | $210.59 | $1,052.95 | +$28.22 | +2.8% |
| MRK | 7.0 | $133.62 | $135.80 | $950.60 | +$15.26 | +1.6% |
| ABBV | 3.0 | $273.24 | $288.80 | $866.40 | +$46.69 | +5.7% |
| JNJ | 3.0 | $270.38 | $269.49 | $808.47 | $-2.68 | -0.3% |
| DIS | 6.0 | $121.16 | $120.27 | $721.62 | $-5.31 | -0.7% |
| UNH | 2.0 | $332.69 | $335.00 | $670.00 | +$4.61 | +0.7% |
| TU | 46.0 | $9.60 | $10.50 | $483.00 | +$41.41 | +9.4% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $29,835.31  
**Cash:** $13,048.09  
**Total P&L:** +$663.37 (+4.1%)  
**Positions:** 15  
*Last updated: 2026-11-24T05:14:14.406497+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| CRWD | sell | 5 | - | stop | 2026-11-23 15:12 | new |
| PANW | sell | 3 | - | stop | 2026-11-20 20:23 | new |
| JNJ | sell | 3 | - | stop | 2026-11-20 17:49 | new |
| AMD | sell | 3 | - | stop | 2026-11-20 16:12 | new |
| IESC | sell | 10 | - | stop | 2026-11-20 15:08 | new |
| UNH | sell | 2 | - | stop | 2026-11-19 18:14 | new |
| MRK | sell | 7 | - | stop | 2026-11-19 17:48 | new |
| WMT | sell | 15 | - | stop | 2026-11-19 15:07 | new |
| LOW | sell | 8 | - | stop | 2026-11-18 15:08 | new |
| PRVA | sell | 60 | - | stop | 2026-11-18 15:08 | new |
| DIS | sell | 6 | - | stop | 2026-11-17 15:07 | new |
| TU | sell | 46 | - | stop | 2026-11-16 15:07 | new |
| REGN | sell | 2 | - | stop | 2026-11-10 14:37 | new |
| ABBV | sell | 3 | - | stop | 2026-10-07 17:18 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$648.40 | 78 |
| 2 | @nivychu | 1 | 0% | $-36.21 | 78 |

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
