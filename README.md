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
| CVS | 27.0 | $75.83 | $95.89 | $2,589.03 | +$541.66 | +26.5% |
| BILL | 64.0 | $40.17 | $40.07 | $2,564.48 | $-6.68 | -0.3% |
| MU | 3.0 | $541.11 | $724.66 | $2,173.98 | +$550.65 | +33.9% |
| BLK | 2.0 | $1,057.92 | $1,081.90 | $2,163.80 | +$47.96 | +2.3% |
| NUE | 9.0 | $223.00 | $227.02 | $2,043.18 | +$36.18 | +1.8% |
| MRK | 18.0 | $112.47 | $111.38 | $2,004.84 | $-19.56 | -1.0% |
| CCI | 20.0 | $84.31 | $86.66 | $1,733.20 | +$47.00 | +2.8% |
| MRVL | 9.0 | $159.53 | $176.89 | $1,592.01 | +$156.19 | +10.9% |
| TXN | 5.0 | $272.82 | $302.73 | $1,513.65 | +$149.53 | +11.0% |
| BA | 3.0 | $231.62 | $220.49 | $661.47 | $-33.38 | -4.8% |
| NOW | 5.0 | $93.02 | $95.07 | $475.35 | +$10.24 | +2.2% |
| AMAT | 1.0 | $441.47 | $436.62 | $436.62 | $-4.85 | -1.1% |
| MSFT | 1.0 | $415.53 | $421.92 | $421.92 | +$6.39 | +1.5% |
| SYY | 5.0 | $73.21 | $72.57 | $362.85 | $-3.21 | -0.9% |
| UNH | 0.689655172 | $290.00 | $393.85 | $271.62 | +$71.62 | +35.8% |
| BTCUSD | 0.003449908 | $70,867.17 | $78,329.30 | $270.23 | +$25.74 | +10.5% |
| PANW | 1.0 | $243.21 | $242.83 | $242.83 | $-0.38 | -0.2% |
| CSCO | 1.0 | $117.34 | $118.21 | $118.21 | +$0.87 | +0.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $26,220.62  
**Cash:** $4,581.35  
**Total P&L:** +$1,575.97 (+7.8%)  
**Positions:** 19  
*Last updated: 2026-05-17T22:01:08.395167+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| PANW | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| NOW | sell | 5 | - | stop | 2026-05-15 13:59 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$88.10 | 78 |
| 2 | @nivychu | 1 | 100% | +$26.22 | 78 |

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
