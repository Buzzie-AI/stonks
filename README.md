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
| CVS | 27.0 | $75.83 | $94.83 | $2,560.41 | +$513.04 | +25.1% |
| NUE | 9.0 | $223.00 | $262.28 | $2,360.52 | +$353.52 | +17.6% |
| CCI | 20.0 | $84.31 | $93.79 | $1,875.80 | +$189.60 | +11.2% |
| NVDA | 5.0 | $214.44 | $216.67 | $1,083.33 | +$11.12 | +1.0% |
| TSM | 2.0 | $431.27 | $440.52 | $881.03 | +$18.50 | +2.1% |
| GE | 2.0 | $285.99 | $327.65 | $655.30 | +$83.32 | +14.6% |
| BA | 3.0 | $220.33 | $217.39 | $652.17 | $-8.81 | -1.3% |
| TJX | 4.0 | $159.00 | $158.63 | $634.52 | $-1.48 | -0.2% |
| AVGO | 1.0 | $420.33 | $415.50 | $415.50 | $-4.83 | -1.1% |
| MDB | 1.0 | $317.56 | $378.11 | $378.11 | +$60.55 | +19.1% |
| SYY | 5.0 | $73.21 | $74.35 | $371.75 | +$5.69 | +1.6% |
| LRCX | 1.0 | $331.36 | $333.50 | $333.50 | +$2.14 | +0.7% |
| DXCM | 4.0 | $64.85 | $72.59 | $290.36 | +$30.94 | +11.9% |
| PANW | 1.0 | $278.81 | $278.25 | $278.25 | $-0.56 | -0.2% |
| UNH | 0.689655172 | $290.00 | $397.00 | $273.79 | +$73.79 | +36.9% |
| D | 4.0 | $68.82 | $66.50 | $266.00 | $-9.28 | -3.4% |
| ORCL | 1.0 | $231.04 | $234.58 | $234.58 | +$3.54 | +1.5% |
| BTCUSD | 0.003449908 | $70,867.17 | $63,191.02 | $218.00 | $-26.48 | -10.8% |
| CRM | 1.0 | $198.91 | $189.00 | $189.00 | $-9.91 | -5.0% |
| CSCO | 1.0 | $117.34 | $130.14 | $130.14 | +$12.80 | +10.9% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,440.70  
**Cash:** $17,358.63  
**Total P&L:** +$1,297.18 (+10.2%)  
**Positions:** 21  
*Last updated: 2026-06-04T22:39:53.270961+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| AVGO | sell | 1 | - | stop | 2026-06-04 12:46 | new |
| PANW | sell | 1 | - | stop | 2026-06-03 13:55 | new |
| LRCX | sell | 1 | - | stop | 2026-06-03 11:00 | new |
| CRM | sell | 1 | - | stop | 2026-06-02 13:55 | new |
| MDB | sell | 1 | - | stop | 2026-06-02 11:00 | new |
| TSM | sell | 2 | - | stop | 2026-06-01 17:18 | new |
| NVDA | sell | 5 | - | stop | 2026-06-01 17:18 | new |
| ORCL | sell | 1 | - | stop | 2026-06-01 13:57 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$171.60 | 78 |
| 2 | @nivychu | 1 | 0% | $-26.13 | 78 |

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
