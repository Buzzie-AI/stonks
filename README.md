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
| CVS | 27.0 | $75.83 | $98.02 | $2,646.54 | +$599.17 | +29.3% |
| NUE | 9.0 | $223.00 | $249.10 | $2,241.90 | +$234.90 | +11.7% |
| CCI | 20.0 | $84.31 | $93.38 | $1,867.60 | +$181.40 | +10.8% |
| NVDA | 8.0 | $211.61 | $199.65 | $1,597.16 | $-95.69 | -5.7% |
| MU | 1.0 | $919.03 | $871.71 | $871.71 | $-47.32 | -5.2% |
| TJX | 4.0 | $159.00 | $167.66 | $670.64 | +$34.64 | +5.5% |
| GE | 2.0 | $285.99 | $317.94 | $635.88 | +$63.90 | +11.2% |
| BA | 3.0 | $220.33 | $208.67 | $626.01 | $-34.98 | -5.3% |
| TSM | 1.0 | $417.29 | $406.78 | $406.78 | $-10.51 | -2.5% |
| SYY | 5.0 | $73.21 | $78.60 | $393.00 | +$26.94 | +7.4% |
| UNH | 0.689655172 | $290.00 | $405.02 | $279.32 | +$79.32 | +39.7% |
| D | 4.0 | $68.82 | $66.77 | $267.08 | $-8.20 | -3.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $61,274.30 | $211.39 | $-33.09 | -13.5% |
| ORCL | 1.0 | $209.20 | $181.85 | $181.85 | $-27.35 | -13.1% |
| CSCO | 1.0 | $117.34 | $118.74 | $118.74 | +$1.40 | +1.2% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,952.97  
**Cash:** $17,937.37  
**Total P&L:** +$964.52 (+8.0%)  
**Positions:** 16  
*Last updated: 2026-06-10T22:54:31.455474+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| ORCL | sell | 1 | - | stop | 2026-06-10 14:00 | new |
| TSM | sell | 1 | - | stop | 2026-06-10 13:59 | new |
| MU | sell | 1 | - | stop | 2026-06-10 13:59 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$163.30 | 78 |
| 2 | @nivychu | 1 | 0% | $-33.11 | 78 |

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
