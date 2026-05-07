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
| CVS | 27.0 | $75.83 | $87.36 | $2,358.72 | +$311.35 | +15.2% |
| CEG | 7.0 | $280.00 | $311.40 | $2,179.80 | +$219.80 | +11.2% |
| BLK | 2.0 | $1,057.92 | $1,055.00 | $2,110.00 | $-5.84 | -0.3% |
| NUE | 9.0 | $223.00 | $226.70 | $2,040.30 | +$33.30 | +1.7% |
| MRK | 18.0 | $112.47 | $112.30 | $2,021.40 | $-3.00 | -0.1% |
| NKE | 44.0 | $45.29 | $44.29 | $1,948.76 | $-43.86 | -2.2% |
| MU | 3.0 | $541.11 | $640.79 | $1,922.37 | +$299.04 | +18.4% |
| CCI | 20.0 | $84.31 | $91.07 | $1,821.40 | +$135.20 | +8.0% |
| MRVL | 9.0 | $159.53 | $158.76 | $1,428.84 | $-6.97 | -0.5% |
| TXN | 5.0 | $272.82 | $283.38 | $1,416.90 | +$52.77 | +3.9% |
| INTC | 12.0 | $96.85 | $107.46 | $1,289.52 | +$127.32 | +11.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $79,676.86 | $274.88 | +$30.39 | +12.4% |
| UNH | 0.689655172 | $290.00 | $368.50 | $254.14 | +$54.14 | +27.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $25,672.74  
**Cash:** $4,605.71  
**Total P&L:** +$1,203.64 (+6.1%)  
**Positions:** 14  
*Last updated: 2026-05-07T22:11:24.168773+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MU | sell | 3 | - | stop | 2026-05-07 11:00 | new |
| CVS | sell | 27 | - | stop | 2026-05-06 13:59 | new |
| INTC | sell | 12 | - | stop | 2026-05-06 11:00 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| TXN | sell | 5 | - | stop | 2026-04-28 13:59 | new |
| CEG | sell | 7 | - | stop | 2026-04-27 14:00 | new |
| MRVL | sell | 9 | - | stop | 2026-04-27 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| NKE | sell | 44 | - | stop | 2026-04-17 14:10 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$92.60 | 78 |
| 2 | @nivychu | 1 | 100% | +$31.04 | 78 |

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
