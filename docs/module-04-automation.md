# Module 4: Automation

**Alert-Only Mode für emotionsfreies Trading**

*Duration: ~3 Stunden | Difficulty: Intermediate*

---

## 4.1 Alert-Only Mode

**Vorher (Spam):**
- Jede Stunde: "ASTS -0.5%"
- Resultat: ignored

**Nachher (Nur Alerts):**
- ASTS -10% → ALERT: Stop-Loss!
- NNE Score 8.2 → ALERT: Kaufempfehlung!

---

## 4.2 Trigger-Regeln

```yaml
# HEARTBEAT.md
## Nur melden bei:

1. Stop-Loss (-10% oder mehr)
2. Profit Target (+15% oder mehr)
3. Momentum (>5% in 10min)
4. Score > 8.0
5. Manuelle Anfrage
```

---

## 4.3 Cron Jobs

```bash
# Alert Screener: Alle 30 Min während Marktstunden
*/30 14-22 * * 1-5 python tools/alert_screener.py

# Morning Brief: 7:00 Uhr
0 7 * * 1-5 python tools/morning_brief.py
```

---

## 4.4 Telegram Integration

```python
def send_alert(message, action="HOLD"):
    payload = {
        "chat_id": CHAT_ID,
        "text": f"ALERT: {message}",
    }
    requests.post(TELEGRAM_API, json=payload)
```

---

## 4.5 Error Handling

```python
class CircuitBreaker:
    def __init__(self, max_failures=3):
        self.failures = 0
        self.state = "closed"
    
    def call(self, func):
        if self.state == "open":
            return None
        try:
            return func()
        except:
            self.failures += 1
            if self.failures >= self.max_failures:
                self.state = "open"
            return None
```

---

## Zusammenfassung

✅ Alert-Only Mode  
✅ Cron Jobs  
✅ Telegram Notifications  
✅ Error Handling  

**Nächstes Modul:** Scale (Agency Agents)