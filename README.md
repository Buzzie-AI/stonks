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
| CVS | 27.0 | $75.83 | $99.16 | $2,677.32 | +$629.95 | +30.8% |
| NUE | 9.0 | $223.00 | $252.60 | $2,273.40 | +$266.40 | +13.3% |
| NVDA | 8.0 | $211.61 | $205.60 | $1,644.80 | $-48.05 | -2.8% |
| ARM | 2.0 | $323.12 | $429.92 | $859.84 | +$213.60 | +33.0% |
| GE | 2.0 | $285.99 | $358.40 | $716.80 | +$144.82 | +25.3% |
| BA | 3.0 | $220.33 | $226.94 | $680.81 | +$19.83 | +3.0% |
| TJX | 4.0 | $159.00 | $164.13 | $656.52 | +$20.52 | +3.2% |
| MRVL | 2.0 | $275.75 | $298.20 | $596.40 | +$44.91 | +8.1% |
| AMD | 1.0 | $512.00 | $522.19 | $522.19 | +$10.19 | +2.0% |
| TSM | 1.0 | $417.29 | $436.90 | $436.90 | +$19.61 | +4.7% |
| SYY | 5.0 | $73.21 | $79.00 | $395.00 | +$28.94 | +7.9% |
| GD | 1.0 | $359.71 | $362.83 | $362.83 | +$3.12 | +0.9% |
| UNH | 0.689655172 | $290.00 | $399.75 | $275.69 | +$75.69 | +37.8% |
| D | 4.0 | $68.82 | $68.02 | $272.08 | $-3.20 | -1.2% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,366.43 | $222.06 | $-22.43 | -9.2% |
| CSCO | 1.0 | $117.34 | $117.82 | $117.82 | +$0.48 | +0.4% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,518.67  
**Cash:** $18,808.21  
**Total P&L:** +$1,404.36 (+12.4%)  
**Positions:** 17  
*Last updated: 2026-06-17T22:49:48.969040+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MRVL | sell | 2 | - | stop | 2026-06-17 17:18 | new |
| ARM | sell | 2 | - | stop | 2026-06-17 17:18 | new |
| NVDA | sell | 8 | - | stop | 2026-06-16 11:00 | new |
| AMD | sell | 1 | - | stop | 2026-06-16 11:00 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| TSM | sell | 1 | - | stop | 2026-06-10 13:59 | new |
| CSCO | sell | 1 | - | stop | 2026-06-05 13:56 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| NUE | sell | 9 | - | stop | 2026-06-05 13:56 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$213.80 | 78 |
| 2 | @nivychu | 1 | 0% | $-22.73 | 78 |

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
