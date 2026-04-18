# Module 1: Foundation

**Your AI Trading System Starts Here**

*Duration: ~3 Stunden | Difficulty: Beginner*

---

## Ziel dieses Moduls

Nach 3 Stunden hast du:
- ✅ OpenClaw installiert und konfiguriert
- ✅ Gateway eingerichtet
- ✅ Ersten Agent erstellt
- ✅ Grundstruktur verstanden

---

## 1.1 Was ist OpenClaw?

OpenClaw ist ein AI-Agent-Framework, das verschiedene AI-Modelle (Ollama, Claude, Gemini) orchestriert.

**Kernfeatures:**
- Multi-Model Management
- Tool System (exec, browser, message, etc.)
- Agent Orchestration
- Cron/Scheduling
- Memory/Palace System

---

## 1.2 Installation

### Schritt 1: OpenClaw installieren

```bash
npm install -g openclaw
```

### Schritt 2: Gateway starten

```bash
openclaw gateway start
```

### Schritt 3: Web UI öffnen

```
http://localhost:18789
```

---

## 1.3 Grundstruktur

```
workspace/
├── agents/              # Agent Definitionen
│   ├── ceo_trading/
│   ├── strategy_screener/
│   └── trade_executor/
├── memory_palaces/      # Langzeitgedächtnis
│   ├── trading/
│   ├── research/
│   └── tech/
├── tools/               # Scripts
│   ├── screener.py
│   └── alert_screener.py
└── workspace/           # Arbeitsdateien
```

---

## 1.4 Dein erster Agent

### Agent Definition (YAML)

```yaml
# agents/mein_agent/AGENT.yaml
name: Mein Trading Agent
version: 1.0
description: Mein persönlicher Trading Agent

capabilities:
  - trading
  - analysis

tools:
  - exec
  - message

memory:
  palace: trading
```

### System Prompt

```markdown
# system-prompt.md

Du bist ein Trading Agent.
Deine Aufgabe:
1. Screen the market every 30 minutes
2. Evaluate opportunities with Score > 8.0
3. Log all trades with timestamp
4. Update memory after each trade

Trigger:
- Score > 8.0 → BUY signal
- Stop-Loss (-10%) → SELL signal
- Profit (+15%) → TAKE PROFIT
```

---

## 1.5 Gateway Konfiguration

```yaml
# .env Datei
OPENCLAW_MODEL=ollama/gemma4:31b
FINNHUB_API_KEY=dein_api_key
TELEGRAM_BOT_TOKEN=dein_token
```

---

## Zusammenfassung

✅ OpenClaw installiert  
✅ Gateway konfiguriert  
✅ Erster Agent erstellt  
✅ Ordnerstruktur verstanden  

**Nächstes Modul:** Trading Division (14 Strategien)