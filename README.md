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
| WMT | 15.0 | $125.31 | $132.35 | $1,985.25 | +$105.67 | +5.6% |
| REGN | 2.0 | $737.32 | $987.44 | $1,974.88 | +$500.24 | +33.9% |
| LOW | 8.0 | $217.92 | $231.04 | $1,848.32 | +$104.92 | +6.0% |
| IESC | 10.0 | $168.97 | $166.04 | $1,660.40 | $-29.35 | -1.7% |
| PRVA | 60.0 | $25.71 | $25.19 | $1,511.40 | $-31.20 | -2.0% |
| PANW | 3.0 | $344.05 | $346.00 | $1,038.00 | +$5.85 | +0.6% |
| CRWD | 5.0 | $204.95 | $206.01 | $1,030.05 | +$5.32 | +0.5% |
| MRK | 7.0 | $133.62 | $141.85 | $992.95 | +$57.61 | +6.2% |
| ABBV | 3.0 | $273.24 | $300.21 | $900.63 | +$80.92 | +9.9% |
| JNJ | 3.0 | $270.38 | $276.96 | $830.88 | +$19.73 | +2.4% |
| SJM | 6.0 | $130.50 | $130.85 | $785.10 | +$2.07 | +0.3% |
| DIS | 6.0 | $121.16 | $121.98 | $731.88 | +$4.95 | +0.7% |
| UNH | 2.0 | $332.69 | $341.88 | $683.76 | +$18.37 | +2.8% |
| MDT | 7.0 | $99.19 | $96.50 | $675.50 | $-18.83 | -2.7% |
| ADI | 2.0 | $319.11 | $310.99 | $621.98 | $-16.24 | -2.5% |
| HPE | 15.0 | $39.60 | $39.14 | $587.10 | $-6.90 | -1.2% |
| TU | 46.0 | $9.60 | $10.66 | $490.36 | +$48.77 | +11.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $29,868.68  
**Cash:** $11,520.24  
**Total P&L:** +$851.89 (+4.9%)  
**Positions:** 18  
*Last updated: 2026-11-25T04:03:42.456776+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| HPE | sell | 15 | - | stop | 2026-11-24 20:22 | new |
| WMT | sell | 15 | - | stop | 2026-11-24 17:42 | new |
| TU | sell | 46 | - | stop | 2026-11-24 17:42 | new |
| MRK | sell | 7 | - | stop | 2026-11-24 17:42 | new |
| LOW | sell | 8 | - | stop | 2026-11-24 17:40 | new |
| MDT | sell | 7 | - | stop | 2026-11-24 15:09 | new |
| SJM | sell | 6 | - | stop | 2026-11-24 15:09 | new |
| ADI | sell | 2 | - | stop | 2026-11-24 15:09 | new |
| CRWD | sell | 5 | - | stop | 2026-11-23 15:12 | new |
| PANW | sell | 3 | - | stop | 2026-11-20 20:23 | new |
| JNJ | sell | 3 | - | stop | 2026-11-20 17:49 | new |
| IESC | sell | 10 | - | stop | 2026-11-20 15:08 | new |
| UNH | sell | 2 | - | stop | 2026-11-19 18:14 | new |
| PRVA | sell | 60 | - | stop | 2026-11-18 15:08 | new |
| DIS | sell | 6 | - | stop | 2026-11-17 15:07 | new |
| REGN | sell | 2 | - | stop | 2026-11-10 14:37 | new |
| ABBV | sell | 3 | - | stop | 2026-10-07 17:18 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$633.90 | 78 |
| 2 | @nivychu | 1 | 0% | $-40.62 | 78 |

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
