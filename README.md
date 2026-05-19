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
| CVS | 27.0 | $75.83 | $94.10 | $2,540.70 | +$493.33 | +24.1% |
| BILL | 64.0 | $40.17 | $37.74 | $2,415.36 | $-155.80 | -6.1% |
| BLK | 2.0 | $1,057.92 | $1,036.56 | $2,073.12 | $-42.72 | -2.0% |
| MRK | 18.0 | $112.47 | $114.24 | $2,056.32 | +$31.92 | +1.6% |
| NUE | 9.0 | $223.00 | $221.64 | $1,994.76 | $-12.24 | -0.6% |
| CCI | 20.0 | $84.31 | $92.06 | $1,841.16 | +$154.96 | +9.2% |
| TXN | 5.0 | $272.82 | $302.31 | $1,511.55 | +$147.43 | +10.8% |
| CRWD | 1.0 | $609.48 | $615.40 | $615.40 | +$5.92 | +1.0% |
| GE | 2.0 | $285.99 | $284.25 | $568.50 | $-3.48 | -0.6% |
| ZS | 3.0 | $180.83 | $173.81 | $521.42 | $-21.05 | -3.9% |
| NOW | 5.0 | $93.02 | $100.92 | $504.62 | +$39.51 | +8.5% |
| NFLX | 5.0 | $91.12 | $89.11 | $445.55 | $-10.05 | -2.2% |
| OKTA | 5.0 | $89.36 | $85.74 | $428.70 | $-18.10 | -4.0% |
| MSFT | 1.0 | $415.53 | $416.40 | $416.40 | +$0.87 | +0.2% |
| SYY | 5.0 | $73.21 | $75.19 | $375.95 | +$9.89 | +2.7% |
| BSX | 5.0 | $55.14 | $56.86 | $284.30 | +$8.58 | +3.1% |
| D | 4.0 | $68.82 | $68.03 | $272.11 | $-3.17 | -1.1% |
| UNH | 0.689655172 | $290.00 | $387.70 | $267.38 | +$67.38 | +33.7% |
| DXCM | 4.0 | $64.85 | $66.78 | $267.12 | +$7.70 | +3.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $76,599.57 | $264.26 | +$19.78 | +8.1% |
| PANW | 1.0 | $243.21 | $239.38 | $239.38 | $-3.83 | -1.6% |
| CSCO | 1.0 | $117.34 | $115.29 | $115.29 | $-2.05 | -1.8% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $30,864.16  
**Cash:** $10,844.81  
**Total P&L:** +$714.77 (+3.7%)  
**Positions:** 23  
*Last updated: 2026-05-19T22:21:40.079662+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TXN | sell | 5 | - | stop | 2026-05-19 20:24 | new |
| CRWD | sell | 1 | - | stop | 2026-05-19 17:18 | new |
| NOW | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| OKTA | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| ZS | sell | 3 | - | stop | 2026-05-19 13:59 | new |
| TXN | sell | 5 | - | stop | 2026-05-19 11:00 | pending_replace |
| DXCM | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| BSX | sell | 5 | - | stop | 2026-05-18 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-05-18 13:58 | new |
| PANW | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| SYY | sell | 5 | - | stop | 2026-05-14 14:40 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$91.65 | 78 |
| 2 | @nivychu | 1 | 100% | +$20.45 | 78 |

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
