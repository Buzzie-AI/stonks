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
| WMT | 15.0 | $125.31 | $131.88 | $1,978.20 | +$98.62 | +5.2% |
| REGN | 2.0 | $737.32 | $981.87 | $1,963.74 | +$489.10 | +33.2% |
| LOW | 8.0 | $217.92 | $235.65 | $1,885.20 | +$141.80 | +8.1% |
| IESC | 10.0 | $168.97 | $175.00 | $1,750.00 | +$60.25 | +3.6% |
| PRVA | 60.0 | $25.71 | $25.84 | $1,550.40 | +$7.80 | +0.5% |
| ADSK | 6.0 | $250.77 | $248.00 | $1,488.00 | $-16.62 | -1.1% |
| NBIS | 12.0 | $77.92 | $92.30 | $1,107.60 | +$172.56 | +18.4% |
| CRWD | 5.0 | $204.95 | $216.35 | $1,081.75 | +$57.02 | +5.6% |
| PANW | 3.0 | $344.05 | $355.91 | $1,067.73 | +$35.58 | +3.5% |
| MRK | 7.0 | $133.62 | $140.29 | $982.03 | +$46.69 | +5.0% |
| BBIO | 10.0 | $87.39 | $89.79 | $897.90 | +$24.00 | +2.8% |
| ABBV | 3.0 | $273.24 | $294.82 | $884.46 | +$64.75 | +7.9% |
| JNJ | 3.0 | $270.38 | $274.09 | $822.27 | +$11.12 | +1.4% |
| SJM | 6.0 | $130.50 | $130.06 | $780.36 | $-2.67 | -0.3% |
| DIS | 6.0 | $121.16 | $125.94 | $755.67 | +$28.73 | +4.0% |
| UNH | 2.0 | $332.69 | $347.57 | $695.14 | +$29.75 | +4.5% |
| ADI | 2.0 | $319.11 | $344.31 | $688.62 | +$50.40 | +7.9% |
| MDT | 7.0 | $99.19 | $96.06 | $672.42 | $-21.91 | -3.2% |
| HPE | 15.0 | $39.60 | $42.24 | $633.60 | +$39.60 | +6.7% |
| TEM | 11.0 | $52.23 | $56.94 | $626.34 | +$51.87 | +9.0% |
| SPCX | 4.0 | $127.27 | $133.47 | $533.88 | +$24.80 | +4.9% |
| TU | 46.0 | $9.60 | $10.80 | $496.80 | +$55.21 | +12.5% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,465.22  
**Cash:** $7,123.11  
**Total P&L:** +$1,448.45 (+6.6%)  
**Positions:** 23  
*Last updated: 2026-11-27T03:34:43.477777+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| SPCX | sell | 4 | - | stop | 2026-11-25 20:21 | new |
| NBIS | sell | 12 | - | stop | 2026-11-25 19:05 | new |
| PRVA | sell | 60 | - | stop | 2026-11-25 18:45 | new |
| IESC | sell | 10 | - | stop | 2026-11-25 18:45 | new |
| BBIO | sell | 10 | - | stop | 2026-11-25 17:59 | new |
| ADSK | sell | 6 | - | stop | 2026-11-25 17:59 | new |
| REGN | sell | 2 | - | stop | 2026-11-25 17:56 | new |
| ABBV | sell | 3 | - | stop | 2026-11-25 17:51 | new |
| TU | sell | 46 | - | stop | 2026-11-25 17:10 | new |
| LOW | sell | 8 | - | stop | 2026-11-25 17:05 | new |
| TEM | sell | 11 | - | stop | 2026-11-25 15:08 | new |
| HPE | sell | 15 | - | stop | 2026-11-24 20:22 | new |
| WMT | sell | 15 | - | stop | 2026-11-24 17:42 | new |
| MRK | sell | 7 | - | stop | 2026-11-24 17:42 | new |
| MDT | sell | 7 | - | stop | 2026-11-24 15:09 | new |
| SJM | sell | 6 | - | stop | 2026-11-24 15:09 | new |
| ADI | sell | 2 | - | stop | 2026-11-24 15:09 | new |
| CRWD | sell | 5 | - | stop | 2026-11-23 15:12 | new |
| PANW | sell | 3 | - | stop | 2026-11-20 20:23 | new |
| JNJ | sell | 3 | - | stop | 2026-11-20 17:49 | new |
| UNH | sell | 2 | - | stop | 2026-11-19 18:14 | new |
| DIS | sell | 6 | - | stop | 2026-11-17 15:07 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$633.90 | 78 |
| 2 | @nivychu | 1 | 0% | $-32.45 | 78 |

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
