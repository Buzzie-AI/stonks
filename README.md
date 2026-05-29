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
| CVS | 27.0 | $75.83 | $90.98 | $2,456.46 | +$409.09 | +20.0% |
| NUE | 9.0 | $223.00 | $250.00 | $2,250.00 | +$243.00 | +12.1% |
| MRK | 18.0 | $112.47 | $118.72 | $2,136.96 | +$112.56 | +5.6% |
| BLK | 2.0 | $1,057.92 | $1,046.88 | $2,093.76 | $-22.08 | -1.0% |
| CCI | 20.0 | $84.31 | $91.50 | $1,830.00 | +$143.80 | +8.5% |
| MU | 1.0 | $908.44 | $962.05 | $962.05 | +$53.61 | +5.9% |
| NVDA | 4.0 | $212.69 | $212.93 | $851.72 | +$0.96 | +0.1% |
| BA | 3.0 | $220.33 | $231.15 | $693.45 | +$32.46 | +4.9% |
| GE | 2.0 | $285.99 | $323.38 | $646.76 | +$74.78 | +13.1% |
| TJX | 4.0 | $159.00 | $154.75 | $619.00 | $-17.00 | -2.7% |
| OKTA | 5.0 | $89.36 | $122.90 | $614.50 | +$167.70 | +37.5% |
| MSFT | 1.0 | $415.53 | $448.50 | $448.50 | +$32.97 | +7.9% |
| AVGO | 1.0 | $420.33 | $446.16 | $446.16 | +$25.83 | +6.1% |
| NFLX | 5.0 | $91.12 | $85.95 | $429.75 | $-25.84 | -5.7% |
| TSM | 1.0 | $416.43 | $419.16 | $419.16 | +$2.73 | +0.7% |
| SYY | 5.0 | $73.21 | $75.81 | $379.05 | +$12.99 | +3.5% |
| MDB | 1.0 | $317.56 | $332.16 | $332.16 | +$14.60 | +4.6% |
| DXCM | 4.0 | $64.85 | $73.03 | $292.14 | +$32.72 | +12.6% |
| D | 4.0 | $68.82 | $66.94 | $267.76 | $-7.52 | -2.7% |
| UNH | 0.689655172 | $290.00 | $379.50 | $261.72 | +$61.72 | +30.9% |
| BTCUSD | 0.003449908 | $70,867.17 | $73,461.10 | $253.43 | +$8.95 | +3.7% |
| CSCO | 1.0 | $117.34 | $120.36 | $120.36 | +$3.02 | +2.6% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,340.68  
**Cash:** $12,535.83  
**Total P&L:** +$1,361.04 (+7.8%)  
**Positions:** 23  
*Last updated: 2026-05-29T22:40:04.761513+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| AVGO | sell | 1 | - | stop | 2026-05-29 20:23 | new |
| OKTA | sell | 5 | - | stop | 2026-05-29 20:23 | new |
| MSFT | sell | 1 | - | stop | 2026-05-29 17:19 | new |
| MU | sell | 1 | - | stop | 2026-05-29 17:19 | new |
| OKTA | sell | 5 | - | stop | 2026-05-29 17:19 | pending_replace |
| MDB | sell | 1 | - | stop | 2026-05-29 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-05-29 13:58 | new |
| TSM | sell | 1 | - | stop | 2026-05-28 14:00 | new |
| AVGO | sell | 1 | - | stop | 2026-05-28 14:00 | pending_replace |
| NVDA | sell | 4 | - | stop | 2026-05-28 14:00 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$104.90 | 78 |
| 2 | @nivychu | 1 | 100% | +$8.88 | 78 |

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
