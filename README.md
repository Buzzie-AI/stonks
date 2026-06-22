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
| CVS | 27.0 | $75.83 | $101.04 | $2,728.08 | +$680.71 | +33.2% |
| NUE | 9.0 | $223.00 | $244.93 | $2,204.37 | +$197.37 | +9.8% |
| NVDA | 8.0 | $211.61 | $207.77 | $1,662.16 | $-30.70 | -1.8% |
| AMD | 2.0 | $520.61 | $546.96 | $1,093.92 | +$52.70 | +5.1% |
| MRVL | 3.0 | $291.75 | $303.44 | $910.32 | +$35.08 | +4.0% |
| GE | 2.0 | $285.99 | $355.31 | $710.62 | +$138.64 | +24.2% |
| BA | 3.0 | $220.33 | $220.70 | $662.10 | +$1.11 | +0.2% |
| TJX | 4.0 | $159.00 | $164.17 | $656.68 | +$20.68 | +3.2% |
| TSM | 1.0 | $417.29 | $466.79 | $466.79 | +$49.50 | +11.9% |
| SYY | 5.0 | $73.21 | $77.98 | $389.90 | +$23.84 | +6.5% |
| GD | 1.0 | $359.71 | $343.36 | $343.36 | $-16.36 | -4.5% |
| UNH | 0.689655172 | $290.00 | $406.00 | $280.00 | +$80.00 | +40.0% |
| D | 4.0 | $68.82 | $68.04 | $272.16 | $-3.12 | -1.1% |
| BTCUSD | 0.003449908 | $70,867.17 | $63,823.10 | $220.18 | $-24.30 | -9.9% |
| CSCO | 1.0 | $117.34 | $121.50 | $121.50 | +$4.16 | +3.5% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,478.29  
**Cash:** $18,756.15  
**Total P&L:** +$1,209.32 (+10.5%)  
**Positions:** 16  
*Last updated: 2026-06-22T22:51:41.885031+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TSM | sell | 1 | - | stop | 2026-06-18 17:18 | new |
| NVDA | sell | 8 | - | stop | 2026-06-18 17:18 | new |
| MRVL | sell | 3 | - | stop | 2026-06-18 15:04 | new |
| AMD | sell | 2 | - | stop | 2026-06-18 14:35 | new |
| GE | sell | 2 | - | stop | 2026-06-15 13:58 | new |
| GD | sell | 1 | - | stop | 2026-06-11 17:20 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$231.90 | 78 |
| 2 | @nivychu | 1 | 0% | $-24.33 | 78 |

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
