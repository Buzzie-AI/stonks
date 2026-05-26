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
| CVS | 27.0 | $75.83 | $90.73 | $2,449.71 | +$402.34 | +19.6% |
| NUE | 9.0 | $223.00 | $240.29 | $2,162.61 | +$155.61 | +7.8% |
| MRK | 18.0 | $112.47 | $119.72 | $2,154.96 | +$130.56 | +6.5% |
| BLK | 2.0 | $1,057.92 | $1,077.40 | $2,154.80 | +$38.96 | +1.8% |
| CCI | 20.0 | $84.31 | $90.64 | $1,812.80 | +$126.60 | +7.5% |
| TXN | 5.0 | $272.82 | $324.88 | $1,624.40 | +$260.27 | +19.1% |
| MRVL | 5.0 | $189.11 | $213.46 | $1,067.30 | +$121.75 | +12.9% |
| BA | 3.0 | $220.33 | $218.67 | $656.02 | $-4.97 | -0.8% |
| CRWD | 1.0 | $609.48 | $654.50 | $654.50 | +$45.02 | +7.4% |
| TJX | 4.0 | $159.00 | $158.97 | $635.88 | $-0.12 | -0.0% |
| GE | 2.0 | $285.99 | $314.49 | $628.98 | +$57.00 | +10.0% |
| OKTA | 5.0 | $89.36 | $91.78 | $458.91 | +$12.11 | +2.7% |
| ZS | 3.0 | $180.83 | $148.00 | $444.00 | $-98.48 | -18.1% |
| NFLX | 5.0 | $91.12 | $87.55 | $437.75 | $-17.85 | -3.9% |
| MSFT | 1.0 | $415.53 | $415.21 | $415.21 | $-0.32 | -0.1% |
| SYY | 5.0 | $73.21 | $75.32 | $376.60 | +$10.54 | +2.9% |
| BSX | 5.0 | $55.14 | $57.64 | $288.20 | +$12.48 | +4.5% |
| DXCM | 4.0 | $64.85 | $71.94 | $287.76 | +$28.34 | +10.9% |
| D | 4.0 | $68.82 | $67.24 | $268.94 | $-6.34 | -2.3% |
| BTCUSD | 0.003449908 | $70,867.17 | $75,738.45 | $261.29 | +$16.81 | +6.9% |
| UNH | 0.689655172 | $290.00 | $376.64 | $259.75 | +$59.75 | +29.9% |
| PANW | 1.0 | $243.21 | $249.50 | $249.50 | +$6.29 | +2.6% |
| CSCO | 1.0 | $117.34 | $118.15 | $118.15 | +$0.81 | +0.7% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,270.35  
**Cash:** $11,402.33  
**Total P&L:** +$1,357.17 (+7.3%)  
**Positions:** 24  
*Last updated: 2026-05-26T22:35:57.108996+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| OKTA | sell | 5 | - | stop | 2026-05-26 17:02 | new |
| MRVL | sell | 5 | - | stop | 2026-05-26 17:02 | new |
| TXN | sell | 5 | - | stop | 2026-05-26 17:02 | new |
| ZS | sell | 3 | - | stop | 2026-05-26 11:00 | new |
| MRK | sell | 18 | - | stop | 2026-05-22 17:18 | new |
| PANW | sell | 1 | - | stop | 2026-05-22 13:58 | new |
| CRWD | sell | 1 | - | stop | 2026-05-22 13:58 | new |
| SYY | sell | 5 | - | stop | 2026-05-22 11:00 | new |
| DXCM | sell | 4 | - | stop | 2026-05-21 11:00 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
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
| 1 | @sudharshan-nn | 1 | 100% | +$73.70 | 78 |
| 2 | @nivychu | 1 | 100% | +$17.23 | 78 |

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
