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
| NVDA | 15.0 | $206.40 | $215.39 | $3,230.85 | +$134.79 | +4.3% |
| CVS | 27.0 | $75.83 | $104.69 | $2,826.63 | +$779.26 | +38.1% |
| ASML | 1.0 | $1,647.13 | $1,703.00 | $1,703.00 | +$55.87 | +3.4% |
| AVGO | 2.0 | $372.44 | $417.00 | $834.00 | +$89.12 | +12.0% |
| GE | 2.0 | $285.99 | $377.69 | $755.38 | +$183.40 | +32.1% |
| MRVL | 3.0 | $220.84 | $217.06 | $651.17 | $-11.34 | -1.7% |
| TJX | 4.0 | $159.00 | $157.55 | $630.20 | $-5.80 | -0.9% |
| SYY | 5.0 | $73.21 | $82.94 | $414.70 | +$48.64 | +13.3% |
| GD | 1.0 | $359.71 | $385.76 | $385.76 | +$26.05 | +7.2% |
| D | 4.0 | $68.82 | $68.71 | $274.82 | $-0.46 | -0.2% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,118.80 | $221.20 | $-23.28 | -9.5% |
| UNH | 0.519655172 | $290.00 | $408.01 | $212.02 | +$61.32 | +40.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,115.36  
**Cash:** $18,975.62  
**Total P&L:** +$1,337.56 (+12.4%)  
**Positions:** 13  
*Last updated: 2026-08-04T22:18:42.483746+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MRVL | sell | 3 | - | stop | 2026-08-04 16:58 | new |
| AVGO | sell | 2 | - | stop | 2026-08-04 13:58 | new |
| NVDA | sell | 15 | - | stop | 2026-08-04 13:58 | new |
| CVS | sell | 27 | - | stop | 2026-08-04 13:58 | new |
| ASML | sell | 1 | - | stop | 2026-08-03 18:43 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$336.90 | 78 |
| 2 | @nivychu | 1 | 0% | $-23.37 | 78 |

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
