# Module 3: Memory System

**MemPalace - Your Trading Brain**

*Duration: ~3 Stunden | Difficulty: Intermediate*

---

## 3.1 Was ist MemPalace?

MemPalace ist ein strukturiertes Langzeitgedächtnis für AI-Systeme.

**Problem:** Normale AI hat kein Gedächtnis zwischen Sessions.
**Lösung:** 6 Palace-Ordner mit strukturierten Rooms.

---

## 3.2 Die 6 Palaces

```
memory_palaces/
├── trading/     # Trades, Depot, Strategien
├── research/    # Opportunities, Sektoren
├── tech/        # Code, Infrastructure
├── office/      # Dokumente, Reports
├── monetize/    # Digital Products
└── system/      # Config, Backups
```

---

## 3.3 Knowledge Graph

```yaml
# mempalace.yaml
wing: trading
rooms:
  - name: depot
    keywords: [portfolio, positions, cash]
  - name: strategies
    keywords: [14_strategies, signals]

knowledge_graph:
  enabled: true
  retrieval: top_k=10
```

---

## 3.4 Retrieval

```python
# Suche in allen Palaces
mempalace search "NNE" --palace all

# Cross-Palace Query
mempalace query "trades_by_strategy"
```

---

## 3.5 Daily Workflow

**Morning (7:00):**
```bash
python tools/memory_update.py --time morning
```

**Evening (23:00):**
```bash
python tools/log_trades.py
python tools/memory_maintenance.py
```

---

## Zusammenfassung

✅ MemPalace Architektur  
✅ 6 Palace Struktur  
✅ Knowledge Graph  
✅ Daily Workflows  

**Nächstes Modul:** Automation (Alert-Only Mode)