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
| WMT | 15.0 | $125.31 | $133.13 | $1,996.95 | +$117.37 | +6.2% |
| REGN | 2.0 | $737.32 | $992.14 | $1,984.28 | +$509.63 | +34.6% |
| LOW | 8.0 | $217.92 | $236.46 | $1,891.68 | +$148.28 | +8.5% |
| IESC | 10.0 | $168.97 | $178.64 | $1,786.40 | +$96.65 | +5.7% |
| PRVA | 60.0 | $25.71 | $25.97 | $1,558.20 | +$15.60 | +1.0% |
| ADSK | 6.0 | $250.77 | $251.88 | $1,511.28 | +$6.66 | +0.4% |
| PANW | 3.0 | $344.05 | $366.76 | $1,100.28 | +$68.13 | +6.6% |
| CRWD | 5.0 | $204.95 | $217.20 | $1,086.00 | +$61.27 | +6.0% |
| NBIS | 12.0 | $77.92 | $89.46 | $1,073.52 | +$138.48 | +14.8% |
| MRK | 7.0 | $133.62 | $141.32 | $989.24 | +$53.90 | +5.8% |
| BBIO | 10.0 | $87.39 | $91.12 | $911.20 | +$37.30 | +4.3% |
| ABBV | 3.0 | $273.24 | $291.88 | $875.64 | +$55.93 | +6.8% |
| JNJ | 3.0 | $270.38 | $275.51 | $826.53 | +$15.38 | +1.9% |
| DIS | 6.0 | $121.16 | $127.24 | $763.44 | +$36.51 | +5.0% |
| SJM | 6.0 | $130.50 | $126.86 | $761.16 | $-21.87 | -2.8% |
| UNH | 2.0 | $332.69 | $351.41 | $702.82 | +$37.43 | +5.6% |
| ADI | 2.0 | $319.11 | $346.00 | $692.00 | +$53.78 | +8.4% |
| MDT | 7.0 | $99.19 | $95.41 | $667.87 | $-26.46 | -3.8% |
| HPE | 15.0 | $39.60 | $42.76 | $641.40 | +$47.40 | +8.0% |
| TEM | 11.0 | $52.23 | $55.91 | $615.01 | +$40.53 | +7.1% |
| SPCX | 4.0 | $127.27 | $133.59 | $534.36 | +$25.28 | +5.0% |
| TU | 46.0 | $9.60 | $10.79 | $496.34 | +$54.75 | +12.4% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,588.71  
**Cash:** $7,123.11  
**Total P&L:** +$1,571.94 (+7.2%)  
**Positions:** 23  
*Last updated: 2026-11-28T03:12:37.645659+00:00*

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
| 1 | @sudharshan-nn | 1 | 100% | +$655.20 | 78 |
| 2 | @nivychu | 1 | 0% | $-38.03 | 78 |

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
