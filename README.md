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
| CVS | 27.0 | $75.83 | $86.55 | $2,336.85 | +$289.48 | +14.1% |
| CEG | 7.0 | $280.00 | $323.99 | $2,267.93 | +$307.93 | +15.7% |
| BLK | 2.0 | $1,057.92 | $1,075.12 | $2,150.23 | +$34.39 | +1.6% |
| NUE | 9.0 | $223.00 | $233.68 | $2,103.09 | +$96.09 | +4.8% |
| MRK | 18.0 | $112.47 | $113.56 | $2,044.08 | +$19.68 | +1.0% |
| MU | 3.0 | $541.11 | $656.50 | $1,969.50 | +$346.17 | +21.3% |
| NKE | 44.0 | $45.29 | $43.90 | $1,931.60 | $-61.02 | -3.1% |
| CVX | 10.0 | $191.91 | $184.95 | $1,849.50 | $-69.65 | -3.6% |
| CCI | 20.0 | $84.31 | $90.87 | $1,817.40 | +$131.20 | +7.8% |
| MRVL | 9.0 | $159.53 | $169.50 | $1,525.50 | +$89.69 | +6.2% |
| TXN | 5.0 | $272.82 | $288.36 | $1,441.80 | +$77.67 | +5.7% |
| INTC | 12.0 | $96.85 | $110.45 | $1,325.40 | +$163.20 | +14.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $81,553.14 | $281.35 | +$36.87 | +15.1% |
| UNH | 0.689655172 | $290.00 | $365.40 | $252.00 | +$52.00 | +26.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $26,087.00  
**Cash:** $2,790.76  
**Total P&L:** +$1,513.70 (+7.0%)  
**Positions:** 15  
*Last updated: 2026-05-06T22:04:43.799612+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MU | sell | 3 | - | stop | 2026-05-06 20:24 | accepted |
| CVS | sell | 27 | - | stop | 2026-05-06 13:59 | new |
| INTC | sell | 12 | - | stop | 2026-05-06 11:00 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| CVX | sell | 10 | - | stop | 2026-05-01 13:57 | new |
| TXN | sell | 5 | - | stop | 2026-04-28 13:59 | new |
| CEG | sell | 7 | - | stop | 2026-04-27 14:00 | new |
| MRVL | sell | 9 | - | stop | 2026-04-27 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| NKE | sell | 44 | - | stop | 2026-04-17 14:10 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$91.35 | 78 |
| 2 | @nivychu | 1 | 100% | +$37.25 | 78 |

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
