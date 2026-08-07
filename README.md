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
| NVDA | 16.0 | $207.41 | $219.59 | $3,513.44 | +$194.94 | +5.9% |
| ASML | 1.0 | $1,647.13 | $1,721.72 | $1,721.72 | +$74.59 | +4.5% |
| LLY | 1.0 | $1,158.37 | $1,190.64 | $1,190.64 | +$32.27 | +2.8% |
| AVGO | 2.0 | $372.44 | $421.37 | $842.74 | +$97.86 | +13.1% |
| GE | 2.0 | $285.99 | $374.67 | $749.34 | +$177.36 | +31.0% |
| TJX | 4.0 | $159.00 | $162.06 | $648.24 | +$12.24 | +1.9% |
| MRVL | 3.0 | $220.84 | $214.15 | $642.45 | $-20.06 | -3.0% |
| SYY | 5.0 | $73.21 | $84.35 | $421.75 | +$55.69 | +15.2% |
| GD | 1.0 | $359.71 | $386.92 | $386.92 | +$27.20 | +7.6% |
| D | 4.0 | $68.82 | $66.80 | $267.20 | $-8.08 | -2.9% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,281.14 | $221.76 | $-22.72 | -9.3% |
| UNH | 0.519655172 | $290.00 | $404.06 | $209.97 | +$59.27 | +39.3% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,942.19  
**Cash:** $20,126.01  
**Total P&L:** +$680.56 (+6.7%)  
**Positions:** 13  
*Last updated: 2026-08-07T01:01:13.281181+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| NVDA | sell | 16 | - | stop | 2026-08-06 14:03 | new |
| LLY | sell | 1 | - | stop | 2026-08-05 17:01 | new |
| GE | sell | 2 | - | stop | 2026-08-05 14:00 | new |
| ASML | sell | 1 | - | stop | 2026-08-05 14:00 | new |
| AVGO | sell | 2 | - | stop | 2026-08-05 14:00 | new |
| GD | sell | 1 | - | stop | 2026-08-05 11:00 | new |
| SYY | sell | 5 | - | stop | 2026-08-05 11:00 | new |
| MRVL | sell | 3 | - | stop | 2026-08-04 16:58 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$344.10 | 78 |
| 2 | @nivychu | 1 | 0% | $-22.74 | 78 |

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
