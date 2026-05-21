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
| CVS | 27.0 | $75.83 | $93.00 | $2,511.00 | +$463.63 | +22.6% |
| BILL | 64.0 | $40.17 | $36.70 | $2,348.80 | $-222.36 | -8.7% |
| MRK | 18.0 | $112.47 | $120.24 | $2,164.32 | +$139.92 | +6.9% |
| BLK | 2.0 | $1,057.92 | $1,063.75 | $2,127.50 | +$11.66 | +0.6% |
| NUE | 9.0 | $223.00 | $226.60 | $2,039.40 | +$32.40 | +1.6% |
| CCI | 20.0 | $84.31 | $92.04 | $1,840.80 | +$154.60 | +9.2% |
| TXN | 5.0 | $272.82 | $298.03 | $1,490.14 | +$126.02 | +9.2% |
| MRVL | 5.0 | $189.11 | $191.97 | $959.86 | +$14.31 | +1.5% |
| BA | 3.0 | $220.33 | $219.69 | $659.07 | $-1.91 | -0.3% |
| CRWD | 1.0 | $609.48 | $648.27 | $648.27 | +$38.79 | +6.4% |
| TJX | 4.0 | $159.00 | $159.87 | $639.48 | +$3.48 | +0.6% |
| GE | 2.0 | $285.99 | $302.67 | $605.34 | +$33.36 | +5.8% |
| ZS | 3.0 | $180.83 | $172.50 | $517.50 | $-24.98 | -4.6% |
| OKTA | 5.0 | $89.36 | $89.76 | $448.80 | +$2.00 | +0.5% |
| NFLX | 5.0 | $91.12 | $89.54 | $447.70 | $-7.90 | -1.7% |
| MSFT | 1.0 | $415.53 | $420.17 | $420.17 | +$4.64 | +1.1% |
| SYY | 5.0 | $73.21 | $77.00 | $385.00 | +$18.94 | +5.2% |
| DXCM | 4.0 | $64.85 | $71.79 | $287.16 | +$27.74 | +10.7% |
| BSX | 5.0 | $55.14 | $57.38 | $286.90 | +$11.18 | +4.1% |
| D | 4.0 | $68.82 | $68.25 | $273.00 | $-2.28 | -0.8% |
| BTCUSD | 0.003449908 | $70,867.17 | $77,577.70 | $267.64 | +$23.15 | +9.5% |
| UNH | 0.689655172 | $290.00 | $381.52 | $263.12 | +$63.12 | +31.6% |
| PANW | 1.0 | $243.21 | $252.08 | $252.08 | +$8.87 | +3.6% |
| CSCO | 1.0 | $117.34 | $118.61 | $118.61 | +$1.27 | +1.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,103.91  
**Cash:** $9,102.24  
**Total P&L:** +$919.66 (+4.4%)  
**Positions:** 25  
*Last updated: 2026-05-21T22:25:32.412523+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| SYY | sell | 5 | - | stop | 2026-05-21 20:25 | new |
| PANW | sell | 1 | - | stop | 2026-05-21 20:25 | new |
| MRVL | sell | 5 | - | stop | 2026-05-21 17:18 | new |
| CRWD | sell | 1 | - | stop | 2026-05-21 13:58 | new |
| TXN | sell | 5 | - | stop | 2026-05-21 11:00 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| OKTA | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| ZS | sell | 3 | - | stop | 2026-05-19 13:59 | new |
| BSX | sell | 5 | - | stop | 2026-05-18 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-05-18 13:58 | new |
| PANW | sell | 1 | - | stop | 2026-05-15 17:18 | pending_replace |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| SYY | sell | 5 | - | stop | 2026-05-14 14:40 | pending_replace |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| BILL | sell | 64 | - | stop | 2026-05-08 14:08 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$93.00 | 78 |
| 2 | @nivychu | 1 | 100% | +$23.65 | 78 |

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
