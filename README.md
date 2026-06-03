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
| CVS | 27.0 | $75.83 | $91.37 | $2,466.99 | +$419.62 | +20.5% |
| NUE | 9.0 | $223.00 | $257.73 | $2,319.57 | +$312.57 | +15.6% |
| CCI | 20.0 | $84.31 | $88.62 | $1,772.40 | +$86.20 | +5.1% |
| NVDA | 5.0 | $214.44 | $213.65 | $1,068.25 | $-3.96 | -0.4% |
| MU | 1.0 | $908.44 | $1,053.62 | $1,053.62 | +$145.19 | +16.0% |
| TSM | 2.0 | $431.27 | $431.40 | $862.80 | +$0.26 | +0.0% |
| TJX | 4.0 | $159.00 | $157.90 | $631.60 | $-4.40 | -0.7% |
| BA | 3.0 | $220.33 | $210.11 | $630.33 | $-30.66 | -4.6% |
| GE | 2.0 | $285.99 | $314.16 | $628.32 | +$56.34 | +9.8% |
| AVGO | 1.0 | $420.33 | $417.71 | $417.71 | $-2.62 | -0.6% |
| ARM | 1.0 | $390.59 | $393.27 | $393.27 | +$2.68 | +0.7% |
| SYY | 5.0 | $73.21 | $75.24 | $376.20 | +$10.14 | +2.8% |
| MDB | 1.0 | $317.56 | $362.15 | $362.15 | +$44.59 | +14.0% |
| LRCX | 1.0 | $331.36 | $344.00 | $344.00 | +$12.64 | +3.8% |
| DXCM | 4.0 | $64.85 | $73.50 | $294.00 | +$34.58 | +13.3% |
| PANW | 1.0 | $278.81 | $273.00 | $273.00 | $-5.81 | -2.1% |
| D | 4.0 | $68.82 | $65.90 | $263.60 | $-11.68 | -4.2% |
| UNH | 0.689655172 | $290.00 | $377.03 | $260.02 | +$60.02 | +30.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $64,433.50 | $222.29 | $-22.20 | -9.1% |
| ORCL | 1.0 | $231.04 | $219.65 | $219.65 | $-11.39 | -4.9% |
| CRM | 1.0 | $198.91 | $188.70 | $188.70 | $-10.21 | -5.1% |
| CSCO | 1.0 | $117.34 | $129.22 | $129.22 | +$11.88 | +10.1% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,160.86  
**Cash:** $15,983.16  
**Total P&L:** +$1,093.79 (+7.8%)  
**Positions:** 23  
*Last updated: 2026-06-03T23:08:36.649019+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| PANW | sell | 1 | - | stop | 2026-06-03 13:55 | new |
| LRCX | sell | 1 | - | stop | 2026-06-03 11:00 | new |
| MU | sell | 1 | - | stop | 2026-06-03 11:00 | new |
| AVGO | sell | 1 | - | stop | 2026-06-02 17:18 | new |
| CRM | sell | 1 | - | stop | 2026-06-02 13:55 | new |
| MDB | sell | 1 | - | stop | 2026-06-02 11:00 | new |
| TSM | sell | 2 | - | stop | 2026-06-01 17:18 | new |
| NVDA | sell | 5 | - | stop | 2026-06-01 17:18 | new |
| ARM | sell | 1 | - | stop | 2026-06-01 13:57 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$129.30 | 78 |
| 2 | @nivychu | 1 | 0% | $-22.32 | 78 |

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
