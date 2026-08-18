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
| NVDA | 16.0 | $207.41 | $219.45 | $3,511.20 | +$192.70 | +5.8% |
| LLY | 1.0 | $1,158.37 | $1,226.00 | $1,226.00 | +$67.63 | +5.8% |
| HPE | 15.0 | $57.88 | $55.43 | $831.45 | $-36.75 | -4.2% |
| TER | 2.0 | $416.78 | $400.00 | $800.00 | $-33.56 | -4.0% |
| GD | 2.0 | $377.63 | $396.38 | $792.77 | +$37.51 | +5.0% |
| ISRG | 2.0 | $394.24 | $391.40 | $782.80 | $-5.69 | -0.7% |
| DLR | 4.0 | $198.87 | $195.25 | $781.00 | $-14.48 | -1.8% |
| GE | 2.0 | $285.99 | $374.92 | $749.85 | +$177.87 | +31.1% |
| TJX | 4.0 | $159.00 | $151.85 | $607.40 | $-28.60 | -4.5% |
| SYM | 15.0 | $41.00 | $40.47 | $607.05 | $-7.95 | -1.3% |
| SYY | 5.0 | $73.21 | $82.12 | $410.60 | +$44.54 | +12.2% |
| D | 4.0 | $68.82 | $68.61 | $274.44 | $-0.84 | -0.3% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,600.00 | $222.86 | $-21.62 | -8.8% |
| UNH | 0.519655172 | $290.00 | $393.44 | $204.45 | +$53.75 | +35.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,951.74  
**Cash:** $19,149.87  
**Total P&L:** +$424.51 (+3.7%)  
**Positions:** 15  
*Last updated: 2026-08-18T21:31:33.771834+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TER | sell | 2 | - | stop | 2026-08-18 13:49 | new |
| ISRG | sell | 2 | - | stop | 2026-08-18 13:42 | new |
| SYM | sell | 15 | - | stop | 2026-08-18 13:42 | new |
| HPE | sell | 15 | - | stop | 2026-08-17 17:19 | new |
| DLR | sell | 4 | - | stop | 2026-08-17 15:24 | new |
| NVDA | sell | 16 | - | stop | 2026-08-13 18:21 | new |
| TJX | sell | 4 | - | stop | 2026-08-11 13:58 | new |
| D | sell | 4 | - | stop | 2026-08-11 13:58 | new |
| GD | sell | 2 | - | stop | 2026-08-10 14:02 | new |
| LLY | sell | 1 | - | stop | 2026-08-05 17:01 | new |
| GE | sell | 2 | - | stop | 2026-08-05 14:00 | new |
| SYY | sell | 5 | - | stop | 2026-08-05 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$425.00 | 78 |
| 2 | @nivychu | 1 | 0% | $-21.77 | 78 |

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
