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
| CVS | 27.0 | $75.83 | $93.28 | $2,518.56 | +$471.19 | +23.0% |
| BILL | 64.0 | $40.17 | $38.34 | $2,453.76 | $-117.40 | -4.6% |
| BLK | 2.0 | $1,057.92 | $1,051.57 | $2,103.14 | $-12.70 | -0.6% |
| MRK | 18.0 | $112.47 | $113.29 | $2,039.17 | +$14.76 | +0.7% |
| NUE | 9.0 | $223.00 | $225.67 | $2,031.03 | +$24.03 | +1.2% |
| CCI | 20.0 | $84.31 | $92.64 | $1,852.80 | +$166.60 | +9.9% |
| TXN | 5.0 | $272.82 | $303.99 | $1,519.95 | +$155.82 | +11.4% |
| MRVL | 5.0 | $189.11 | $187.90 | $939.50 | $-6.05 | -0.6% |
| BA | 3.0 | $220.33 | $221.34 | $664.02 | +$3.03 | +0.5% |
| CRWD | 1.0 | $609.48 | $647.50 | $647.50 | +$38.02 | +6.2% |
| TJX | 4.0 | $159.00 | $158.65 | $634.58 | $-1.42 | -0.2% |
| GE | 2.0 | $285.99 | $298.55 | $597.10 | +$25.12 | +4.4% |
| ZS | 3.0 | $180.83 | $172.68 | $518.04 | $-24.44 | -4.5% |
| OKTA | 5.0 | $89.36 | $88.53 | $442.67 | $-4.13 | -0.9% |
| NFLX | 5.0 | $91.12 | $87.88 | $439.40 | $-16.20 | -3.5% |
| MSFT | 1.0 | $415.53 | $418.66 | $418.66 | +$3.13 | +0.8% |
| SYY | 5.0 | $73.21 | $75.46 | $377.30 | +$11.24 | +3.1% |
| BSX | 5.0 | $55.14 | $56.67 | $283.35 | +$7.63 | +2.8% |
| DXCM | 4.0 | $64.85 | $70.50 | $282.00 | +$22.58 | +8.7% |
| D | 4.0 | $68.82 | $67.73 | $270.92 | $-4.36 | -1.6% |
| BTCUSD | 0.003449908 | $70,867.17 | $77,384.11 | $266.97 | +$22.48 | +9.2% |
| UNH | 0.689655172 | $290.00 | $381.95 | $263.41 | +$63.41 | +31.7% |
| PANW | 1.0 | $243.21 | $244.11 | $244.11 | +$0.90 | +0.4% |
| CSCO | 1.0 | $117.34 | $113.81 | $113.81 | $-3.53 | -3.0% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,024.00  
**Cash:** $9,102.24  
**Total P&L:** +$839.74 (+4.0%)  
**Positions:** 25  
*Last updated: 2026-05-20T22:39:08.675103+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TXN | sell | 5 | - | stop | 2026-05-20 20:24 | new |
| DXCM | sell | 4 | - | stop | 2026-05-20 20:24 | new |
| CRWD | sell | 1 | - | stop | 2026-05-20 17:17 | new |
| BA | sell | 3 | - | stop | 2026-05-20 13:59 | new |
| TJX | sell | 4 | - | stop | 2026-05-20 13:59 | new |
| MRVL | sell | 5 | - | stop | 2026-05-20 13:59 | new |
| TXN | sell | 5 | - | stop | 2026-05-20 11:00 | pending_replace |
| GE | sell | 2 | - | stop | 2026-05-19 13:59 | new |
| NFLX | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| OKTA | sell | 5 | - | stop | 2026-05-19 13:59 | new |
| ZS | sell | 3 | - | stop | 2026-05-19 13:59 | new |
| DXCM | sell | 4 | - | stop | 2026-05-18 13:59 | pending_replace |
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
| 1 | @sudharshan-nn | 1 | 100% | +$90.20 | 78 |
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
