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
| CVS | 27.0 | $75.83 | $89.24 | $2,409.39 | +$362.01 | +17.7% |
| NUE | 9.0 | $223.00 | $258.46 | $2,326.14 | +$319.14 | +15.9% |
| BLK | 2.0 | $1,057.92 | $1,018.96 | $2,037.92 | $-77.92 | -3.7% |
| CCI | 20.0 | $84.31 | $89.92 | $1,798.40 | +$112.20 | +6.7% |
| NVDA | 5.0 | $214.44 | $221.60 | $1,108.00 | +$35.79 | +3.3% |
| MU | 1.0 | $908.44 | $1,054.00 | $1,054.00 | +$145.56 | +16.0% |
| TSM | 2.0 | $431.27 | $446.33 | $892.65 | +$30.11 | +3.5% |
| BA | 3.0 | $220.33 | $217.18 | $651.54 | $-9.45 | -1.4% |
| GE | 2.0 | $285.99 | $317.70 | $635.40 | +$63.42 | +11.1% |
| TJX | 4.0 | $159.00 | $153.69 | $614.76 | $-21.24 | -3.3% |
| SMCI | 10.0 | $49.16 | $49.56 | $495.65 | +$4.10 | +0.8% |
| AVGO | 1.0 | $420.33 | $494.06 | $494.06 | +$73.73 | +17.5% |
| MSFT | 1.0 | $415.53 | $439.40 | $439.40 | +$23.87 | +5.7% |
| ARM | 1.0 | $390.59 | $399.20 | $399.20 | +$8.61 | +2.2% |
| MDB | 1.0 | $317.56 | $397.42 | $397.42 | +$79.86 | +25.1% |
| SYY | 5.0 | $73.21 | $74.10 | $370.50 | +$4.44 | +1.2% |
| LRCX | 1.0 | $331.36 | $334.39 | $334.39 | +$3.03 | +0.9% |
| DXCM | 4.0 | $64.85 | $73.45 | $293.80 | +$34.38 | +13.2% |
| PANW | 1.0 | $292.27 | $292.68 | $292.68 | +$0.41 | +0.1% |
| D | 4.0 | $68.82 | $66.47 | $265.88 | $-9.40 | -3.4% |
| UNH | 0.689655172 | $290.00 | $377.40 | $260.28 | +$60.28 | +30.1% |
| ORCL | 1.0 | $231.04 | $241.01 | $241.01 | +$9.97 | +4.3% |
| BTCUSD | 0.003449908 | $70,867.17 | $66,157.64 | $228.24 | $-16.25 | -6.7% |
| CRM | 1.0 | $198.91 | $199.53 | $199.53 | +$0.62 | +0.3% |
| CSCO | 1.0 | $117.34 | $128.38 | $128.38 | +$11.04 | +9.4% |
| 737CVR019 | 4.064262182 | $0.00 | $0.00 | $0.00 | +$0.00 | +0.0% |

**Portfolio Value:** $31,477.31  
**Cash:** $13,108.69  
**Total P&L:** +$1,248.32 (+7.3%)  
**Positions:** 26  
*Last updated: 2026-06-02T23:05:45.520377+00:00*

### Pending Orders

| Symbol | Side | Qty | Notional | Type | Submitted | Status |
|--------|------|-----|----------|------|-----------|--------|
| SMCI | sell | 10 | - | stop | 2026-06-02 20:21 | new |
| LRCX | sell | 1 | - | stop | 2026-06-02 20:21 | new |
| MU | sell | 1 | - | stop | 2026-06-02 20:21 | new |
| PANW | sell | 1 | - | stop | 2026-06-02 20:21 | new |
| AVGO | sell | 1 | - | stop | 2026-06-02 17:18 | new |
| LRCX | sell | 1 | - | stop | 2026-06-02 13:55 | pending_replace |
| PANW | sell | 1 | - | stop | 2026-06-02 13:55 | pending_replace |
| SMCI | sell | 10 | - | stop | 2026-06-02 13:55 | pending_replace |
| CRM | sell | 1 | - | stop | 2026-06-02 13:55 | new |
| MU | sell | 1 | - | stop | 2026-06-02 13:55 | pending_replace |
| MDB | sell | 1 | - | stop | 2026-06-02 11:00 | new |
| TSM | sell | 2 | - | stop | 2026-06-01 17:18 | new |
| NVDA | sell | 5 | - | stop | 2026-06-01 17:18 | new |
| ARM | sell | 1 | - | stop | 2026-06-01 13:57 | new |
| ORCL | sell | 1 | - | stop | 2026-06-01 13:57 | new |
| MSFT | sell | 1 | - | stop | 2026-06-01 13:56 | new |
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
| BLK | sell | 2 | - | stop | 2026-04-15 11:00 | new |

<!-- PORTFOLIO_END -->

## Contributor Leaderboard

<!-- LEADERBOARD_START -->
| # | Contributor | Trades | Win Rate | Total P&L | Avg AI Score |
|---|-------------|--------|----------|-----------|--------------|
| 1 | @sudharshan-nn | 1 | 100% | +$126.55 | 78 |
| 2 | @nivychu | 1 | 0% | $-16.08 | 78 |

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
