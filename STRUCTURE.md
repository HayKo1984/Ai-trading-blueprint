# Project Structure

```
ai-trading-blueprint/
├── README.md                    # This file
├── setup.py                    # Installation script
├── docs/                       # PDF Modules
│   ├── module-01-foundation.md
│   ├── module-02-trading.md
│   ├── module-03-memory.md
│   ├── module-04-automation.md
│   └── module-05-scale.md
├── agents/                     # Strategy Agent configs
│   ├── strategy-01-momentum.yaml
│   ├── strategy-02-mean-reversion.yaml
│   ├── strategy-03-goldman-smallcap.yaml
│   ├── strategy-04-lynch-discovery.yaml
│   ├── strategy-05-social-arbitrage.yaml
│   ├── strategy-06-100-bagger.yaml
│   ├── strategy-07-cathie-wood.yaml
│   ├── strategy-08-magic-formula.yaml
│   ├── strategy-09-pabrai-asymmetric.yaml
│   ├── strategy-10-howard-marks.yaml
│   ├── strategy-11-nick-sleep.yaml
│   ├── strategy-12-burry-deep-value.yaml
│   ├── strategy-13-insider-13f.yaml
│   └── strategy-14-blind-spots.yaml
└── notion/                    # Notion Templates
    ├── trading-dashboard.md
    ├── strategy-scorecard.md
    └── daily-workflow.md
```

## Module Descriptions

### docs/ - Educational Content
Complete guides for building your AI trading system:
- Module 1: Foundation (OpenClaw, Gateway, Agents)
- Module 2: Trading Division (14 strategies, screener)
- Module 3: Memory System (MemPalace, 6 palaces)
- Module 4: Automation (Alert-Only Mode, Cron)
- Module 5: Scale (Agency Agents, DevOps)

### agents/ - Configuration Files
YAML configurations for 14 trading strategy agents:
- Each strategy has specific triggers, scoring, and signals
- Ready to import into OpenClaw
- Documented with examples

### notion/ - Productivity Templates
Notion-compatible templates for daily trading:
- Trading Dashboard: Portfolio overview
- Strategy Scorecard: Evaluate signals
- Daily Workflow: Structured routine