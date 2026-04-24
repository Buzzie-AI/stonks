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
| NVDA | 12.0 | $177.28 | $207.85 | $2,494.20 | +$366.81 | +17.2% |
| CEG | 7.0 | $280.00 | $313.36 | $2,193.52 | +$233.52 | +11.9% |
| CVS | 27.0 | $75.83 | $77.67 | $2,097.09 | +$49.72 | +2.4% |
| BA | 9.0 | $223.00 | $232.60 | $2,093.40 | +$86.44 | +4.3% |
| BLK | 2.0 | $1,057.92 | $1,044.96 | $2,089.92 | $-25.92 | -1.2% |
| MRK | 18.0 | $112.47 | $111.90 | $2,014.20 | $-10.20 | -0.5% |
| NKE | 44.0 | $45.29 | $44.80 | $1,971.20 | $-21.42 | -1.1% |
| CCI | 20.0 | $84.31 | $86.34 | $1,726.80 | +$40.60 | +2.4% |
| MRVL | 9.0 | $159.53 | $164.30 | $1,478.70 | +$42.88 | +3.0% |
| INTC | 14.0 | $66.94 | $82.54 | $1,155.56 | +$218.40 | +23.3% |
| LRCX | 4.0 | $267.37 | $268.88 | $1,075.52 | +$6.04 | +0.6% |
| BTCUSD | 0.003449908 | $70,867.17 | $77,645.25 | $267.87 | +$23.38 | +9.6% |
| UNH | 0.689655172 | $290.00 | $354.00 | $244.14 | +$44.14 | +22.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $25,093.25  
**Cash:** $4,191.13  
**Total P&L:** +$1,054.39 (+5.3%)  
**Positions:** 14  
*Last updated: 2026-04-24T21:55:28.543040+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| INTC | sell | 14 | - | stop | 2026-04-24 20:24 | new |
| CEG | sell | 7 | - | stop | 2026-04-24 17:18 | new |
| INTC | sell | 14 | - | stop | 2026-04-24 14:14 | pending_replace |
| BA | sell | 9 | - | stop | 2026-04-24 13:52 | new |
| LRCX | sell | 4 | - | stop | 2026-04-24 13:49 | new |
| MRK | sell | 18 | - | stop | 2026-04-22 13:53 | new |
| CCI | sell | 20 | - | stop | 2026-04-17 14:10 | new |
| NKE | sell | 44 | - | stop | 2026-04-17 14:10 | new |
| CVS | sell | 27 | - | stop | 2026-04-16 14:02 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |
| NVDA | sell | 12 | - | stop | 2026-04-14 18:58 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @nivychu | 1 | 100% | +$23.70 | 78 |
| 2 | @sudharshan-nn | 1 | 0% | $-14.45 | 78 |

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
