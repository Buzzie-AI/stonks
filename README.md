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
| CVS | 27.0 | $75.83 | $90.62 | $2,446.74 | +$399.37 | +19.5% |
| NUE | 9.0 | $223.00 | $251.49 | $2,263.41 | +$256.41 | +12.8% |
| BLK | 2.0 | $1,057.92 | $1,020.73 | $2,041.46 | $-74.38 | -3.5% |
| CCI | 20.0 | $84.31 | $91.03 | $1,820.60 | +$134.40 | +8.0% |
| NVDA | 5.0 | $214.44 | $223.96 | $1,119.80 | +$47.59 | +4.4% |
| MU | 1.0 | $908.44 | $1,037.42 | $1,037.42 | +$128.98 | +14.2% |
| TSM | 2.0 | $431.27 | $437.54 | $875.07 | +$12.54 | +1.4% |
| OKTA | 5.0 | $89.36 | $138.00 | $690.00 | +$243.20 | +54.4% |
| BA | 3.0 | $220.33 | $224.20 | $672.60 | +$11.61 | +1.8% |
| GE | 2.0 | $285.99 | $324.36 | $648.72 | +$76.74 | +13.4% |
| TJX | 4.0 | $159.00 | $152.75 | $611.00 | $-25.00 | -3.9% |
| AVGO | 1.0 | $420.33 | $473.01 | $473.01 | +$52.68 | +12.5% |
| MSFT | 1.0 | $415.53 | $452.89 | $452.89 | +$37.36 | +9.0% |
| NFLX | 5.0 | $91.12 | $85.66 | $428.30 | $-27.30 | -6.0% |
| ARM | 1.0 | $390.59 | $412.90 | $412.90 | +$22.31 | +5.7% |
| MDB | 1.0 | $317.56 | $400.01 | $400.01 | +$82.45 | +26.0% |
| SYY | 5.0 | $73.21 | $73.72 | $368.60 | +$2.54 | +0.7% |
| DXCM | 4.0 | $64.85 | $74.78 | $299.12 | +$39.70 | +15.3% |
| UNH | 0.689655172 | $290.00 | $379.86 | $261.97 | +$61.97 | +31.0% |
| D | 4.0 | $68.82 | $64.61 | $258.44 | $-16.84 | -6.1% |
| BTCUSD | 0.003449908 | $70,867.17 | $71,302.80 | $245.99 | +$1.50 | +0.6% |
| ORCL | 1.0 | $231.04 | $241.06 | $241.06 | +$10.02 | +4.3% |
| CSCO | 1.0 | $117.34 | $121.99 | $121.99 | +$4.65 | +4.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,543.69  
**Cash:** $13,352.58  
**Total P&L:** +$1,482.51 (+8.9%)  
**Positions:** 24  
*Last updated: 2026-06-01T23:06:01.378379+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| MDB | sell | 1 | - | stop | 2026-06-01 20:23 | new |
| OKTA | sell | 5 | - | stop | 2026-06-01 20:23 | new |
| MU | sell | 1 | - | stop | 2026-06-01 17:18 | new |
| MDB | sell | 1 | - | stop | 2026-06-01 17:18 | pending_replace |
| OKTA | sell | 5 | - | stop | 2026-06-01 17:18 | pending_replace |
| TSM | sell | 2 | - | stop | 2026-06-01 17:18 | new |
| NVDA | sell | 5 | - | stop | 2026-06-01 17:18 | new |
| ARM | sell | 1 | - | stop | 2026-06-01 13:57 | new |
| ORCL | sell | 1 | - | stop | 2026-06-01 13:57 | new |
| MSFT | sell | 1 | - | stop | 2026-06-01 13:56 | new |
| AVGO | sell | 1 | - | stop | 2026-06-01 11:00 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$151.20 | 78 |
| 2 | @nivychu | 1 | 100% | +$1.49 | 78 |

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
