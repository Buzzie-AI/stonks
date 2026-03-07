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
| NVDA | 50.0 | $180.94 | $177.82 | $8,891.00 | $-155.97 | -1.7% |
| PONY | 420.0 | $18.05 | $12.48 | $5,241.60 | $-2,339.68 | -30.9% |
| FIG | 100.0 | $48.18 | $29.11 | $2,911.00 | $-1,907.00 | -39.6% |
| HOOD | 25.0 | $126.69 | $77.09 | $1,927.25 | $-1,239.93 | -39.1% |
| HNGE | 10.0 | $45.67 | $46.14 | $461.40 | +$4.70 | +1.0% |
| UNH | 0.689655172 | $290.00 | $286.48 | $197.57 | $-2.43 | -1.2% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $23,803.58  
**Cash:** $4,173.76  
**Total P&L:** $-5,640.31 (-22.3%)  
**Positions:** 7  
*Last updated: 2026-03-07T21:30:57.349977+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| NVDA | buy | 10 | - | market | 2026-03-06 21:02 | accepted |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$4.00 | 78 |

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
