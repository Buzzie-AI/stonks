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
| CVS | 27.0 | $75.83 | $95.93 | $2,590.11 | +$542.74 | +26.5% |
| NUE | 9.0 | $223.00 | $258.54 | $2,326.83 | +$319.83 | +15.9% |
| CCI | 20.0 | $84.31 | $94.18 | $1,883.60 | +$197.40 | +11.7% |
| NVDA | 7.0 | $212.13 | $205.38 | $1,437.65 | $-47.25 | -3.2% |
| TSM | 2.0 | $431.27 | $412.20 | $824.40 | $-38.14 | -4.4% |
| GE | 2.0 | $285.99 | $326.50 | $653.00 | +$81.02 | +14.2% |
| BA | 3.0 | $220.33 | $214.62 | $643.86 | $-17.13 | -2.6% |
| TJX | 4.0 | $159.00 | $159.25 | $637.00 | +$1.00 | +0.2% |
| SYY | 5.0 | $73.21 | $75.74 | $378.70 | +$12.64 | +3.5% |
| DXCM | 4.0 | $64.85 | $71.61 | $286.43 | +$27.02 | +10.4% |
| UNH | 0.689655172 | $290.00 | $396.76 | $273.63 | +$73.63 | +36.8% |
| PANW | 1.0 | $278.81 | $268.50 | $268.50 | $-10.31 | -3.7% |
| D | 4.0 | $68.82 | $66.96 | $267.84 | $-7.44 | -2.7% |
| BTCUSD | 0.003449908 | $70,867.17 | $61,475.46 | $212.08 | $-32.40 | -13.2% |
| CSCO | 1.0 | $117.34 | $121.64 | $121.64 | +$4.30 | +3.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,209.65  
**Cash:** $18,404.37  
**Total P&L:** +$1,106.91 (+9.5%)  
**Positions:** 16  
*Last updated: 2026-06-05T22:21:05.431154+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| NVDA | sell | 7 | - | stop | 2026-06-05 19:47 | new |
| CSCO | sell | 1 | - | stop | 2026-06-05 13:56 | new |
| CVS | sell | 27 | - | stop | 2026-06-05 13:56 | new |
| CCI | sell | 20 | - | stop | 2026-06-05 13:56 | new |
| NUE | sell | 9 | - | stop | 2026-06-05 13:56 | new |
| GE | sell | 2 | - | stop | 2026-06-05 13:56 | new |
| DXCM | sell | 4 | - | stop | 2026-06-05 13:56 | new |
| PANW | sell | 1 | - | stop | 2026-06-03 13:55 | new |
| TSM | sell | 2 | - | stop | 2026-06-01 17:18 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$178.15 | 78 |
| 2 | @nivychu | 1 | 0% | $-32.31 | 78 |

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
