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
| NVDA | 16.0 | $207.41 | $223.20 | $3,571.20 | +$252.70 | +7.6% |
| ASML | 1.0 | $1,647.13 | $1,741.87 | $1,741.87 | +$94.74 | +5.8% |
| LLY | 1.0 | $1,158.37 | $1,184.00 | $1,184.00 | +$25.63 | +2.2% |
| AVGO | 2.0 | $372.44 | $426.00 | $852.00 | +$107.12 | +14.4% |
| GE | 2.0 | $285.99 | $370.81 | $741.62 | +$169.64 | +29.7% |
| MRVL | 3.0 | $220.84 | $218.00 | $654.00 | $-8.51 | -1.3% |
| TJX | 4.0 | $159.00 | $161.36 | $645.44 | +$9.44 | +1.5% |
| SYY | 5.0 | $73.21 | $84.29 | $421.45 | +$55.39 | +15.1% |
| GD | 1.0 | $359.71 | $392.83 | $392.83 | +$33.12 | +9.2% |
| D | 4.0 | $68.82 | $67.47 | $269.88 | $-5.40 | -2.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,953.90 | $224.08 | $-20.40 | -8.3% |
| UNH | 0.519655172 | $290.00 | $406.30 | $211.14 | +$60.44 | +40.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,037.11  
**Cash:** $20,127.60  
**Total P&L:** +$773.90 (+7.6%)  
**Positions:** 13  
*Last updated: 2026-08-07T21:49:09.715500+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| AVGO | sell | 2 | - | stop | 2026-08-07 17:07 | new |
| GD | sell | 1 | - | stop | 2026-08-07 17:07 | new |
| NVDA | sell | 16 | - | stop | 2026-08-06 14:03 | new |
| LLY | sell | 1 | - | stop | 2026-08-05 17:01 | new |
| GE | sell | 2 | - | stop | 2026-08-05 14:00 | new |
| ASML | sell | 1 | - | stop | 2026-08-05 14:00 | new |
| SYY | sell | 5 | - | stop | 2026-08-05 11:00 | new |
| MRVL | sell | 3 | - | stop | 2026-08-04 16:58 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$436.50 | 78 |
| 2 | @nivychu | 1 | 0% | $-20.56 | 78 |

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
