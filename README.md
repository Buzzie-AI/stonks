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
| LLY | 1.0 | $1,158.37 | $1,232.13 | $1,232.13 | +$73.76 | +6.4% |
| PANW | 3.0 | $369.31 | $339.50 | $1,018.50 | $-89.42 | -8.1% |
| DLR | 4.0 | $198.87 | $192.32 | $769.28 | $-26.20 | -3.3% |
| GD | 2.0 | $377.63 | $376.58 | $753.16 | $-2.10 | -0.3% |
| SYM | 15.0 | $41.00 | $40.47 | $607.05 | $-7.95 | -1.3% |
| RKLB | 8.0 | $73.56 | $67.20 | $537.60 | $-50.88 | -8.7% |
| RARE | 20.0 | $26.54 | $26.60 | $532.00 | +$1.20 | +0.2% |
| SYY | 5.0 | $73.21 | $83.46 | $417.30 | +$51.24 | +14.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $78,463.42 | $270.69 | +$26.21 | +10.7% |
| D | 4.0 | $68.82 | $66.95 | $267.80 | $-7.48 | -2.7% |
| UNH | 0.519655172 | $290.00 | $396.30 | $205.94 | +$55.24 | +36.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,543.38  
**Cash:** $23,931.93  
**Total P&L:** +$23.62 (+0.4%)  
**Positions:** 12  
*Last updated: 2026-08-25T21:36:39.562991+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| RKLB | sell | 8 | - | stop | 2026-08-20 13:51 | new |
| RARE | sell | 20 | - | stop | 2026-08-20 13:50 | new |
| PANW | sell | 3 | - | stop | 2026-08-19 13:49 | new |
| LLY | sell | 1 | - | stop | 2026-08-19 13:42 | new |
| SYM | sell | 15 | - | stop | 2026-08-18 13:42 | new |
| DLR | sell | 4 | - | stop | 2026-08-17 15:24 | new |
| D | sell | 4 | - | stop | 2026-08-11 13:58 | new |
| GD | sell | 2 | - | stop | 2026-08-10 14:02 | new |
| SYY | sell | 5 | - | stop | 2026-08-05 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$439.90 | 78 |
| 2 | @nivychu | 1 | 100% | +$26.98 | 78 |

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
