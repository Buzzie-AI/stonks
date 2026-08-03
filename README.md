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
| NVDA | 15.0 | $206.40 | $206.96 | $3,104.36 | +$8.30 | +0.3% |
| CVS | 27.0 | $75.83 | $105.37 | $2,844.99 | +$797.62 | +39.0% |
| ASML | 1.0 | $1,647.13 | $1,643.30 | $1,643.30 | $-3.83 | -0.2% |
| AVGO | 2.0 | $372.44 | $392.33 | $784.66 | +$39.78 | +5.3% |
| GE | 2.0 | $285.99 | $369.41 | $738.82 | +$166.84 | +29.2% |
| TJX | 4.0 | $159.00 | $157.21 | $628.84 | $-7.16 | -1.1% |
| SYY | 5.0 | $73.21 | $85.10 | $425.50 | +$59.44 | +16.2% |
| GD | 1.0 | $359.71 | $382.43 | $382.43 | +$22.71 | +6.3% |
| D | 4.0 | $68.82 | $68.75 | $275.00 | $-0.28 | -0.1% |
| BTCUSD | 0.003449908 | $70,867.17 | $63,408.30 | $218.75 | $-25.73 | -10.5% |
| UNH | 0.519655172 | $290.00 | $415.03 | $215.67 | +$64.97 | +43.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,900.47  
**Cash:** $19,638.14  
**Total P&L:** +$1,122.66 (+11.1%)  
**Positions:** 12  
*Last updated: 2026-08-03T22:13:33.267522+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| ASML | sell | 1 | - | stop | 2026-08-03 18:43 | new |
| NVDA | sell | 15 | - | stop | 2026-08-03 18:43 | new |
| AVGO | sell | 2 | - | stop | 2026-07-16 19:49 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$319.50 | 78 |
| 2 | @nivychu | 1 | 0% | $-25.81 | 78 |

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
