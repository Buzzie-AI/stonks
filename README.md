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
| CVS | 27.0 | $75.83 | $93.26 | $2,518.02 | +$470.65 | +23.0% |
| MRK | 18.0 | $112.47 | $122.41 | $2,203.38 | +$178.98 | +8.8% |
| BLK | 2.0 | $1,057.92 | $1,073.00 | $2,146.00 | +$30.16 | +1.4% |
| NUE | 9.0 | $223.00 | $232.00 | $2,088.00 | +$81.00 | +4.0% |
| CCI | 20.0 | $84.31 | $91.46 | $1,829.20 | +$143.00 | +8.5% |
| TXN | 5.0 | $272.82 | $309.21 | $1,546.05 | +$181.93 | +13.3% |
| MRVL | 5.0 | $189.11 | $196.33 | $981.65 | +$36.10 | +3.8% |
| CRWD | 1.0 | $609.48 | $663.46 | $663.46 | +$53.98 | +8.9% |
| BA | 3.0 | $220.33 | $219.02 | $657.06 | $-3.93 | -0.6% |
| TJX | 4.0 | $159.00 | $158.27 | $633.08 | $-2.92 | -0.5% |
| GE | 2.0 | $285.99 | $302.84 | $605.68 | +$33.70 | +5.9% |
| ZS | 3.0 | $180.83 | $182.37 | $547.11 | +$4.63 | +0.8% |
| OKTA | 5.0 | $89.36 | $92.24 | $461.20 | +$14.40 | +3.2% |
| NFLX | 5.0 | $91.12 | $88.60 | $443.00 | $-12.60 | -2.8% |
| MSFT | 1.0 | $415.53 | $418.57 | $418.57 | +$3.04 | +0.7% |
| SYY | 5.0 | $73.21 | $76.29 | $381.45 | +$15.39 | +4.2% |
| BSX | 5.0 | $55.14 | $57.78 | $288.90 | +$13.18 | +4.8% |
| DXCM | 4.0 | $64.85 | $72.10 | $288.40 | +$28.98 | +11.2% |
| D | 4.0 | $68.82 | $67.67 | $270.68 | $-4.60 | -1.7% |
| UNH | 0.689655172 | $290.00 | $388.47 | $267.91 | +$67.91 | +34.0% |
| BTCUSD | 0.003449908 | $70,867.17 | $77,326.90 | $266.77 | +$22.29 | +9.1% |
| PANW | 1.0 | $243.21 | $260.58 | $260.58 | +$17.37 | +7.1% |
| CSCO | 1.0 | $117.34 | $120.41 | $120.41 | +$3.07 | +2.6% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,288.89  
**Cash:** $11,402.33  
**Total P&L:** +$1,375.71 (+7.4%)  
**Positions:** 24  
*Last updated: 2026-05-25T22:14:40.978669+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| ZS | sell | 3 | - | stop | 2026-05-22 20:24 | new |
| MRK | sell | 18 | - | stop | 2026-05-22 17:18 | new |
| PANW | sell | 1 | - | stop | 2026-05-22 13:58 | new |
| CRWD | sell | 1 | - | stop | 2026-05-22 13:58 | new |
| TXN | sell | 5 | - | stop | 2026-05-22 13:58 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| MRVL | sell | 5 | - | stop | 2026-05-21 17:18 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| OKTA | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| ZS | sell | 3 | - | stop | 2026-05-19 13:59 | pending_replace |
| BSX | sell | 5 | - | stop | 2026-05-18 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$95.30 | 78 |
| 2 | @nivychu | 1 | 100% | +$22.81 | 78 |

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
