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
| LLY | 1.0 | $1,158.37 | $1,175.75 | $1,175.75 | +$17.38 | +1.5% |
| DLR | 4.0 | $198.87 | $192.10 | $768.40 | $-27.08 | -3.4% |
| GD | 2.0 | $377.63 | $380.06 | $760.12 | +$4.86 | +0.6% |
| SYM | 15.0 | $41.00 | $41.12 | $616.80 | +$1.80 | +0.3% |
| RKLB | 8.0 | $73.56 | $67.45 | $539.60 | $-48.88 | -8.3% |
| RARE | 20.0 | $26.54 | $26.37 | $527.40 | $-3.40 | -0.6% |
| SYY | 5.0 | $73.21 | $82.45 | $412.25 | +$46.19 | +12.6% |
| BTCUSD | 0.003449908 | $70,867.17 | $79,657.62 | $274.81 | +$30.33 | +12.4% |
| D | 4.0 | $68.82 | $66.50 | $266.00 | $-9.28 | -3.4% |
| UNH | 0.519655172 | $290.00 | $395.89 | $205.73 | +$55.03 | +36.5% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,470.81  
**Cash:** $24,923.95  
**Total P&L:** +$66.94 (+1.2%)  
**Positions:** 11  
*Last updated: 2026-08-28T05:16:57.915858+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| RKLB | sell | 8 | - | stop | 2026-08-20 13:51 | new |
| RARE | sell | 20 | - | stop | 2026-08-20 13:50 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$471.00 | 78 |
| 2 | @nivychu | 1 | 100% | +$30.91 | 78 |

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
