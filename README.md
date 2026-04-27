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
| CEG | 7.0 | $280.00 | $315.80 | $2,210.60 | +$250.60 | +12.8% |
| NVDA | 10.0 | $177.28 | $217.45 | $2,174.50 | +$401.68 | +22.7% |
| CVS | 27.0 | $75.83 | $78.30 | $2,114.10 | +$66.73 | +3.3% |
| BLK | 2.0 | $1,057.92 | $1,056.86 | $2,113.72 | $-2.12 | -0.1% |
| BA | 9.0 | $223.00 | $231.32 | $2,081.88 | +$74.92 | +3.7% |
| NKE | 44.0 | $45.29 | $45.19 | $1,988.51 | $-4.11 | -0.2% |
| MRK | 18.0 | $112.47 | $110.38 | $1,986.84 | $-37.56 | -1.9% |
| CCI | 20.0 | $84.31 | $84.30 | $1,686.00 | $-0.20 | -0.0% |
| MRVL | 9.0 | $159.53 | $157.34 | $1,416.06 | $-19.75 | -1.4% |
| TXN | 5.0 | $272.82 | $269.10 | $1,345.50 | $-18.62 | -1.4% |
| INTC | 14.0 | $66.94 | $84.66 | $1,185.23 | +$248.06 | +26.5% |
| LRCX | 4.0 | $267.37 | $259.32 | $1,037.28 | $-32.20 | -3.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $76,827.90 | $265.05 | +$20.56 | +8.4% |
| UNH | 0.689655172 | $290.00 | $353.75 | $243.97 | +$43.97 | +22.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $25,097.26  
**Cash:** $3,248.02  
**Total P&L:** +$991.95 (+4.8%)  
**Positions:** 15  
*Last updated: 2026-04-27T22:02:24.229043+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| NVDA | sell | 10 | - | stop | 2026-04-27 14:01 | new |
| CEG | sell | 7 | - | stop | 2026-04-27 14:00 | new |
| INTC | sell | 14 | - | stop | 2026-04-27 14:00 | new |
| BA | sell | 9 | - | stop | 2026-04-27 13:59 | new |
| MRVL | sell | 9 | - | stop | 2026-04-27 13:59 | new |
| LRCX | sell | 4 | - | stop | 2026-04-24 13:49 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| CCI | sell | 20 | - | stop | 2026-04-17 14:10 | new |
| NKE | sell | 44 | - | stop | 2026-04-17 14:10 | new |
| CVS | sell | 27 | - | stop | 2026-04-16 14:02 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @nivychu | 1 | 100% | +$20.98 | 78 |
| 2 | @sudharshan-nn | 1 | 0% | $-5.60 | 78 |

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
