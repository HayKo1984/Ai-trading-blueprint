#!/usr/bin/env python3
"""
AI Trading Setup Blueprint - Installation Script
=================================================

Sets up the complete AI trading system environment.
"""

import os
import sys

def print_step(msg):
    print(f"\n{'='*50}")
    print(f"  {msg}")
    print('='*50)

def main():
    print_step("AI Trading Blueprint Setup")
    
    # Check Python version
    print("[1/5] Checking Python version...")
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required")
        return 1
    print(f"  Python {sys.version_info.major}.{sys.version_info.minor} - OK")
    
    # Check OpenClaw
    print("\n[2/5] Checking OpenClaw...")
    try:
        import openclaw
        print("  OpenClaw installed - OK")
    except ImportError:
        print("  OpenClaw not found - installing...")
        os.system("pip install openclaw")
    
    # Create directories
    print("\n[3/5] Creating directory structure...")
    dirs = [
        "agents/strategy",
        "memory_palaces/trading",
        "memory_palaces/research",
        "memory_palaces/tech",
        "memory_palaces/office",
        "memory_palaces/monetize",
        "memory_palaces/system",
        "tools",
        "logs",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"  Created: {d}/")
    
    # Copy files
    print("\n[4/5] Setting up configuration...")
    
    # Create AGENTS.md
    agents_md = """# AI Trading Agent Team

## Available Agents

### Strategy Agents (14)
1. Momentum Breakout
2. Mean Reversion
3. Goldman Small Cap
4. Lynch Discovery
5. Social Arbitrage
6. 100 Bagger
7. Cathie Wood Innovation
8. Magic Formula
9. Pabrai Asymmetric
10. Howard Marks Contrarian
11. Nick Sleep Owner
12. Burry Deep Value
13. Insider/13F Smart Money
14. Wall Street Blind Spots

### System Agents
- CEO_Trading: Orchestrates trading operations
- CEO_Research: Market analysis & opportunities
- Trade_Executor: Executes paper trades
- Strategy_Screener: Evaluates signals

## Usage

Import strategy YAML from `agents/` directory.
Run screener: `python tools/master_screener.py`
"""

    with open("AGENTS.md", "w") as f:
        f.write(agents_md)
    print("  Created: AGENTS.md")
    
    # Create HEARTBEAT.md
    heartbeat_md = """# Heartbeat Configuration - Alert-Only Mode

## Trigger-Regeln

### Nur melden bei:
1. Stop-Loss ausgelöst (-10% oder mehr)
2. Profit Target erreicht (+15% oder mehr)
3. Momentum-Breakout (>5% in 10 Minuten)
4. Score > 8.0 (Trading Screener)
5. Manuelle Anfrage

### Symbole überwacht
- ASTS, RKLB, NNE, SOFI, OKLO

## Output-Format
```
ALERT: [SYMBOL] [EREIGNIS]
Preis: $[X] ([Change]%)
Action: [KAUFEN/VERKAUFEN/HALTEN]
```
"""

    with open("HEARTBEAT.md", "w") as f:
        f.write(heartbeat_md)
    print("  Created: HEARTBEAT.md")
    
    print_step("Setup Complete!")
    print("\nNext steps:")
    print("1. Configure your Finnhub API key")
    print("2. Set up Telegram notifications")
    print("3. Run: python tools/morning_brief.py")
    print("4. Import agents/ strategy YAMLs into OpenClaw")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())