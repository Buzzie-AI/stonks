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
| NVDA | 15.0 | $229.00 | $240.29 | $3,604.35 | +$169.35 | +4.9% |
| REGN | 2.0 | $737.32 | $738.72 | $1,477.44 | +$2.79 | +0.2% |
| AVGO | 3.0 | $353.38 | $377.30 | $1,131.90 | +$71.77 | +6.8% |
| MU | 1.0 | $1,061.09 | $1,048.10 | $1,048.10 | $-12.99 | -1.2% |
| HPE | 14.0 | $64.00 | $71.39 | $999.46 | +$103.46 | +11.6% |
| DLR | 4.0 | $198.87 | $184.65 | $738.60 | $-56.88 | -7.2% |
| SYM | 15.0 | $41.00 | $44.39 | $665.85 | +$50.85 | +8.3% |
| SYY | 5.0 | $73.21 | $77.45 | $387.25 | +$21.19 | +5.8% |
| BTCUSD | 0.003449908 | $70,867.17 | $85,426.75 | $294.71 | +$50.23 | +20.5% |
| UNH | 0.519655172 | $290.00 | $376.04 | $195.41 | +$44.71 | +29.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,618.04  
**Cash:** $20,074.96  
**Total P&L:** +$444.48 (+4.4%)  
**Positions:** 11  
*Last updated: 2026-10-07T00:35:10.439772+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| HPE | sell | 14 | - | stop | 2026-10-06 17:18 | new |
| AVGO | sell | 3 | - | stop | 2026-10-06 17:17 | new |
| MU | sell | 1 | - | stop | 2026-10-05 13:58 | new |
| REGN | sell | 2 | - | stop | 2026-10-01 17:18 | new |
| NVDA | sell | 15 | - | stop | 2026-10-01 11:00 | new |
| SYM | sell | 15 | - | stop | 2026-08-18 13:42 | new |
| DLR | sell | 4 | - | stop | 2026-08-17 15:24 | new |
| SYY | sell | 5 | - | stop | 2026-08-05 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$526.20 | 78 |
| 2 | @nivychu | 1 | 100% | +$51.17 | 78 |

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
