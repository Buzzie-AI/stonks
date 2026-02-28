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
No open positions yet. Submit a PR to make the first trade!
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
