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
| CVS | 27.0 | $75.83 | $92.97 | $2,510.19 | +$462.82 | +22.6% |
| NUE | 9.0 | $223.00 | $249.30 | $2,243.70 | +$236.70 | +11.8% |
| MRK | 18.0 | $112.47 | $119.89 | $2,158.02 | +$133.62 | +6.6% |
| BLK | 2.0 | $1,057.92 | $1,046.49 | $2,092.98 | $-22.86 | -1.1% |
| CCI | 20.0 | $84.31 | $91.09 | $1,821.80 | +$135.60 | +8.0% |
| TXN | 5.0 | $272.82 | $316.25 | $1,581.25 | +$217.12 | +15.9% |
| MU | 1.0 | $908.44 | $934.98 | $934.98 | +$26.54 | +2.9% |
| NVDA | 4.0 | $212.69 | $214.32 | $857.28 | +$6.52 | +0.8% |
| BA | 3.0 | $220.33 | $228.75 | $686.25 | +$25.26 | +3.8% |
| GE | 2.0 | $285.99 | $320.63 | $641.26 | +$69.28 | +12.1% |
| TJX | 4.0 | $159.00 | $154.89 | $619.56 | $-16.44 | -2.6% |
| OKTA | 5.0 | $89.36 | $102.50 | $512.50 | +$65.70 | +14.7% |
| NFLX | 5.0 | $91.12 | $86.35 | $431.75 | $-23.85 | -5.2% |
| AVGO | 1.0 | $420.33 | $430.87 | $430.87 | +$10.54 | +2.5% |
| MSFT | 1.0 | $415.53 | $427.29 | $427.29 | +$11.76 | +2.8% |
| TSM | 1.0 | $416.43 | $424.70 | $424.70 | +$8.27 | +2.0% |
| SYY | 5.0 | $73.21 | $75.92 | $379.60 | +$13.54 | +3.7% |
| DXCM | 4.0 | $64.85 | $72.47 | $289.90 | +$30.48 | +11.8% |
| D | 4.0 | $68.82 | $67.38 | $269.52 | $-5.76 | -2.1% |
| UNH | 0.689655172 | $290.00 | $381.29 | $262.96 | +$62.96 | +31.5% |
| BTCUSD | 0.003449908 | $70,867.17 | $73,431.12 | $253.33 | +$8.85 | +3.6% |
| CBRS | 1.0 | $263.33 | $244.23 | $244.23 | $-19.10 | -7.3% |
| CSCO | 1.0 | $117.34 | $118.80 | $118.80 | +$1.46 | +1.2% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,261.80  
**Cash:** $11,069.09  
**Total P&L:** +$1,439.00 (+7.7%)  
**Positions:** 24  
*Last updated: 2026-05-28T22:43:26.304714+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| OKTA | sell | 5 | - | stop | 2026-05-28 20:23 | new |
| CBRS | sell | 1 | - | stop | 2026-05-28 14:00 | new |
| TSM | sell | 1 | - | stop | 2026-05-28 14:00 | new |
| AVGO | sell | 1 | - | stop | 2026-05-28 14:00 | new |
| MU | sell | 1 | - | stop | 2026-05-28 14:00 | new |
| NVDA | sell | 4 | - | stop | 2026-05-28 14:00 | new |
| OKTA | sell | 5 | - | stop | 2026-05-26 17:02 | pending_replace |
| TXN | sell | 5 | - | stop | 2026-05-26 17:02 | new |
| MRK | sell | 18 | - | stop | 2026-05-22 17:18 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$91.40 | 78 |
| 2 | @nivychu | 1 | 100% | +$9.11 | 78 |

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
