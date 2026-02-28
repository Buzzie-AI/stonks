# stonks — Open Source Investment Portfolio (Sandbox)

A community-managed investment portfolio where **anyone can propose trades via Pull Requests**. Supports both **stocks and cryptocurrency**. An AI evaluates every pitch, the community votes, and approved trades execute automatically through Alpaca's **paper trading** API — no real money at risk.

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
| ETHUSD | 0.049639164 | $1,969.61 | $1,975.27 | $98.05 | +$0.28 | +0.3% |
| BTCUSD | 0.001453976 | $67,251.10 | $67,329.90 | $97.90 | +$0.11 | +0.1% |
| FUTU | 0.384304984 | $52.04 | $148.84 | $57.20 | +$37.20 | +186.0% |
| BOOT | 0.273440704 | $73.14 | $189.22 | $51.74 | +$31.74 | +158.7% |
| CMA | 0.360711322 | $55.45 | $88.67 | $31.98 | +$11.98 | +59.9% |
| EMR | 0.209432855 | $95.50 | $150.75 | $31.57 | +$11.57 | +57.9% |
| GTLS | 0.14690112 | $136.15 | $207.30 | $30.45 | +$10.45 | +52.3% |
| TFC | 0.537518813 | $37.21 | $49.31 | $26.51 | +$6.51 | +32.5% |
| MUSA | 0.05306391 | $376.90 | $390.74 | $20.73 | +$0.73 | +3.7% |
| DNB | 1.63692912 | $12.22 | $9.15 | $14.98 | $-5.02 | -25.1% |
| EXTR | 1.0 | $11.54 | $13.98 | $13.98 | +$2.44 | +21.1% |
| FRSH | 0.910829765 | $21.96 | $7.82 | $7.12 | $-12.88 | -64.4% |
| BBBY | 0.75832259 | $26.37 | $5.33 | $4.04 | $-15.96 | -79.8% |

**Portfolio Value:** $580.25  
**Cash:** $93.99  
**Total P&L:** +$79.17 (+19.4%)  
**Positions:** 13  
*Last updated: 2026-02-28T22:58:19.686420+00:00*

<!-- PORTFOLIO_END -->

## Quick Start

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/stonks.git
cd stonks
git checkout -b trade/AAPL-BUY      # stocks
git checkout -b trade/BTC-USD-BUY   # crypto

# Open a PR using the template — fill in the YAML block and write your pitch
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details on writing a strong proposal.

## Safety Guardrails

This branch uses **paper trading** (simulated). The following guardrails are still enforced:

- **$500 max** per trade (stocks and crypto)
- **3 trades/day** maximum
- **AI score >= 65** required
- **2+ PR approvals** required
- **Penny stocks banned** (stocks under $5)
- **Dust tokens banned** (crypto under $0.001)
- **Banned tickers list** maintained in `config/banned_tickers.txt`
- Every order is validated for buying power and ticker existence before execution

All parameters are configurable in `config/config.yml`.

## Repo Structure

```
├── .github/workflows/     # evaluate → execute → portfolio update
├── scripts/               # Python: parse, evaluate, trade, update
├── config/                # config.yml + banned tickers
├── data/                  # portfolio.json + trade_history.json
├── CONTRIBUTING.md        # How to submit a trade
└── README.md              # You are here
```

## Secrets Required

Set these in your repo's **Settings → Secrets and variables → Actions**:

| Secret | Description |
|--------|-------------|
| `ALPACA_API_KEY` | Alpaca **paper trading** API key |
| `ALPACA_SECRET_KEY` | Alpaca **paper trading** secret |
| `ANTHROPIC_API_KEY` | Claude API key for pitch evaluation |

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

## Risk Disclaimer

**This is a sandbox branch using paper trading (simulated money).** No real capital is at risk. Use this branch to test strategies before deploying to the `main` branch which trades with real money.

---

Built with [Alpaca](https://alpaca.markets), [Claude](https://anthropic.com), and GitHub Actions.
