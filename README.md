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
| CVS | 27.0 | $75.83 | $96.00 | $2,592.00 | +$544.63 | +26.6% |
| BILL | 64.0 | $40.17 | $38.92 | $2,491.12 | $-80.04 | -3.1% |
| BLK | 2.0 | $1,057.92 | $1,085.88 | $2,171.76 | +$55.92 | +2.6% |
| NUE | 9.0 | $223.00 | $226.48 | $2,038.32 | +$31.32 | +1.6% |
| MRK | 18.0 | $112.47 | $111.64 | $2,009.52 | $-14.88 | -0.7% |
| CCI | 20.0 | $84.31 | $89.92 | $1,798.40 | +$112.20 | +6.7% |
| TXN | 5.0 | $272.82 | $300.60 | $1,503.00 | +$138.88 | +10.2% |
| BA | 3.0 | $231.62 | $220.50 | $661.50 | $-33.35 | -4.8% |
| CRWD | 1.0 | $609.48 | $619.50 | $619.50 | +$10.02 | +1.6% |
| NOW | 5.0 | $93.02 | $104.24 | $521.20 | +$56.09 | +12.1% |
| MSFT | 1.0 | $415.53 | $423.44 | $423.44 | +$7.91 | +1.9% |
| SYY | 5.0 | $73.21 | $73.52 | $367.60 | +$1.54 | +0.4% |
| BSX | 5.0 | $55.14 | $56.19 | $280.96 | +$5.24 | +1.9% |
| D | 4.0 | $68.82 | $67.65 | $270.60 | $-4.68 | -1.7% |
| UNH | 0.689655172 | $290.00 | $390.20 | $269.10 | +$69.10 | +34.5% |
| BTCUSD | 0.003449908 | $70,867.17 | $77,098.17 | $265.98 | +$21.50 | +8.8% |
| DXCM | 4.0 | $64.85 | $65.00 | $260.00 | +$0.58 | +0.2% |
| PANW | 1.0 | $243.21 | $247.49 | $247.49 | +$4.28 | +1.8% |
| CSCO | 1.0 | $117.34 | $118.87 | $118.87 | +$1.53 | +1.3% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,116.96  
**Cash:** $12,206.60  
**Total P&L:** +$927.78 (+5.2%)  
**Positions:** 20  
*Last updated: 2026-05-18T22:08:40.301473+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| TXN | sell | 5 | - | stop | 2026-05-18 20:24 | new |
| NOW | sell | 5 | - | stop | 2026-05-18 20:24 | new |
| DXCM | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| BSX | sell | 5 | - | stop | 2026-05-18 13:59 | new |
| CRWD | sell | 1 | - | stop | 2026-05-18 13:59 | new |
| D | sell | 4 | - | stop | 2026-05-18 13:59 | new |
| MRK | sell | 18 | - | stop | 2026-05-18 13:58 | new |
| PANW | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| CSCO | sell | 1 | - | stop | 2026-05-15 17:18 | new |
| MSFT | sell | 1 | - | stop | 2026-05-15 13:59 | new |
| NOW | sell | 5 | - | stop | 2026-05-15 13:59 | pending_replace |
| SYY | sell | 5 | - | stop | 2026-05-14 14:40 | new |
| BA | sell | 3 | - | stop | 2026-05-14 14:25 | new |
| CVS | sell | 27 | - | stop | 2026-05-13 13:57 | new |
| BILL | sell | 64 | - | stop | 2026-05-08 14:08 | new |
| CCI | sell | 20 | - | stop | 2026-05-01 13:58 | new |
| NUE | sell | 9 | - | stop | 2026-05-01 13:57 | new |
| TXN | sell | 5 | - | stop | 2026-04-28 13:59 | pending_replace |
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$90.60 | 78 |
| 2 | @nivychu | 1 | 100% | +$21.88 | 78 |

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
