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
| BILL | 64.0 | $40.17 | $41.39 | $2,648.96 | +$77.80 | +3.0% |
| CVS | 27.0 | $75.83 | $92.20 | $2,489.40 | +$442.03 | +21.6% |
| MU | 3.0 | $541.11 | $795.85 | $2,387.55 | +$764.22 | +47.1% |
| BLK | 2.0 | $1,057.92 | $1,081.75 | $2,163.50 | +$47.66 | +2.2% |
| NUE | 9.0 | $223.00 | $232.00 | $2,088.00 | +$81.00 | +4.0% |
| MRK | 18.0 | $112.47 | $111.60 | $2,008.80 | $-15.60 | -0.8% |
| CCI | 20.0 | $84.31 | $90.67 | $1,813.40 | +$127.20 | +7.5% |
| MRVL | 9.0 | $159.53 | $169.68 | $1,527.12 | +$91.31 | +6.4% |
| TXN | 5.0 | $272.82 | $297.99 | $1,489.95 | +$125.83 | +9.2% |
| INTC | 6.0 | $96.85 | $129.15 | $774.90 | +$193.80 | +33.4% |
| AMAT | 1.0 | $441.47 | $446.52 | $446.52 | +$5.05 | +1.1% |
| AVGO | 1.0 | $431.40 | $428.36 | $428.36 | $-3.04 | -0.7% |
| BTCUSD | 0.003449908 | $70,867.17 | $81,758.66 | $282.06 | +$37.57 | +15.4% |
| UNH | 0.689655172 | $290.00 | $383.68 | $264.61 | +$64.61 | +32.3% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $26,569.57  
**Cash:** $5,756.44  
**Total P&L:** +$2,039.42 (+10.9%)  
**Positions:** 15  
*Last updated: 2026-05-11T22:15:16.815272+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| AMAT | sell | 1 | - | stop | 2026-05-11 20:23 | accepted |
| AVGO | sell | 1 | - | stop | 2026-05-11 20:23 | accepted |
| INTC | sell | 6 | - | stop | 2026-05-11 11:00 | new |
| MU | sell | 3 | - | stop | 2026-05-08 17:18 | new |
| BILL | sell | 64 | - | stop | 2026-05-08 14:08 | new |
| CVS | sell | 27 | - | stop | 2026-05-06 13:59 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| TXN | sell | 5 | - | stop | 2026-04-28 13:59 | new |
| MRVL | sell | 9 | - | stop | 2026-04-27 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$90.05 | 78 |
| 2 | @nivychu | 1 | 100% | +$38.47 | 78 |

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
