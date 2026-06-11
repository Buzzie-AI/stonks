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
| CVS | 27.0 | $75.83 | $100.48 | $2,712.96 | +$665.59 | +32.5% |
| NUE | 9.0 | $223.00 | $260.90 | $2,348.10 | +$341.10 | +17.0% |
| CCI | 20.0 | $84.31 | $92.04 | $1,840.80 | +$154.60 | +9.2% |
| NVDA | 8.0 | $211.61 | $206.21 | $1,649.68 | $-43.17 | -2.5% |
| MU | 1.0 | $919.03 | $997.71 | $997.71 | +$78.68 | +8.6% |
| ARM | 2.0 | $323.12 | $351.30 | $702.59 | +$56.35 | +8.7% |
| TJX | 4.0 | $159.00 | $168.34 | $673.36 | +$37.36 | +5.9% |
| GE | 2.0 | $285.99 | $332.60 | $665.20 | +$93.22 | +16.3% |
| BA | 3.0 | $220.33 | $221.12 | $663.36 | +$2.37 | +0.4% |
| TSM | 1.0 | $417.29 | $422.95 | $422.95 | +$5.66 | +1.4% |
| SYY | 5.0 | $73.21 | $79.64 | $398.20 | +$32.14 | +8.8% |
| GD | 1.0 | $359.71 | $358.86 | $358.86 | $-0.85 | -0.2% |
| UNH | 0.689655172 | $290.00 | $404.33 | $278.85 | +$78.85 | +39.4% |
| D | 4.0 | $68.82 | $66.69 | $266.76 | $-8.52 | -3.1% |
| INTC | 2.0 | $117.61 | $118.16 | $236.32 | +$1.10 | +0.5% |
| BTCUSD | 0.003449908 | $70,867.17 | $63,496.75 | $219.06 | $-25.43 | -10.4% |
| CSCO | 1.0 | $117.34 | $122.35 | $122.35 | +$5.01 | +4.3% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,430.99  
**Cash:** $16,873.89  
**Total P&L:** +$1,474.04 (+11.3%)  
**Positions:** 18  
*Last updated: 2026-06-11T22:52:42.932738+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MU | sell | 1 | - | stop | 2026-06-11 20:03 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
| ARM | sell | 2 | - | stop | 2026-06-11 17:19 | new |
| INTC | sell | 2 | - | stop | 2026-06-11 13:58 | new |
| TSM | sell | 1 | - | stop | 2026-06-10 13:59 | new |
| MU | sell | 1 | - | stop | 2026-06-10 13:59 | pending_replace |
| GE | sell | 2 | - | stop | 2026-06-09 13:58 | new |
| NVDA | sell | 8 | - | stop | 2026-06-08 13:55 | new |
| CSCO | sell | 1 | - | stop | 2026-06-05 13:56 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| CCI | sell | 20 | - | stop | 2026-06-05 13:56 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$191.40 | 78 |
| 2 | @nivychu | 1 | 0% | $-25.75 | 78 |

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
