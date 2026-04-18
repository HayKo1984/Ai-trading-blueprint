# Module 2: Trading Division

**14 Strategies for Every Market Condition**

*Duration: ~4 Stunden | Difficulty: Intermediate*

---

## Ziel dieses Moduls

Nach 4 Stunden hast du:
- ✅ Alle 14 Strategie-Agents konfiguriert
- ✅ Strategy Screener verstanden
- ✅ Kelly Criterion Sizing implementiert
- ✅ Trade Executor eingerichtet

---

## 2.1 Die 14 Strategien

### Momentum (1-2)
- **01 Momentum Breakout**: Price > 5% + Volume spike
- **02 Mean Reversion**: RSI < 30, bounce expected

### Growth (3-6)
- **03 Goldman Small Cap**: Market cap < $2B, strong fundamentals
- **04 Lynch Discovery**: PEG < 1.5, earnings growth > 20%
- **05 Social Arbitrage**: Sentiment spike, social volume
- **06 100 Bagger**: TAM ratio > 10x, moonshot potential

### Value (7-10)
- **07 Cathie Wood Innovation**: Disruption score > 8
- **08 Magic Formula**: ROC > 50%, earnings yield > 10%
- **09 Pabrai Asymmetric**: 3:1 upside/downside ratio
- **10 Howard Marks**: Fear gauge < 30, contrarian

### Special (11-14)
- **11 Nick Sleep Owner**: Owner earnings > 15%, management alignment
- **12 Burry Deep Value**: P/B < 0.7, NCA > 1.5x price
- **13 Insider/13F**: 3+ top funds accumulating
- **14 Wall Street Blind Spots**: Analyst coverage < 5

---

## 2.2 Strategy Screener

Der Screener bewertet jede Strategie:

```python
def score_symbol(symbol):
    scores = []
    
    for strategy in strategies:
        s = evaluate_strategy(strategy, symbol)
        scores.append((strategy.name, s))
    
    # Beste Strategie pro Symbol
    best = max(scores, key=lambda x: x[1])
    return best
```

---

## 2.3 Kelly Criterion

Position sizing mit Kelly:

```python
import math

def kelly_size(capital, win_rate, avg_win, avg_loss):
    """
    Kelly = W - (1-W)/R
    W = Win rate
    R = Win/Loss ratio
    """
    if avg_loss == 0:
        return 0
    
    R = avg_win / avg_loss
    kelly = win_rate - (1 - win_rate) / R
    
    # Max 25% of capital per trade
    return min(kelly, 0.25) * capital

# Beispiel
size = kelly_size(
    capital=10000,
    win_rate=0.60,
    avg_win=500,
    avg_loss=300
)
# → $1,500 (15% of capital)
```

---

## 2.4 Trade Executor

```python
# trade_executor.py

class TradeExecutor:
    def __init__(self, config):
        self.config = config
        self.min_score = 8.0
    
    def execute_buy(self, symbol, score, strategy):
        if score < self.min_score:
            return None
        
        position = calculate_position_size(symbol)
        
        log_trade(
            symbol=symbol,
            action="BUY",
            shares=position.shares,
            price=position.price,
            strategy=strategy,
            score=score
        )
        
        return position
    
    def execute_sell(self, symbol, reason):
        log_trade(
            symbol=symbol,
            action="SELL",
            reason=reason
        )
```

---

## 2.5 Consensus System

3-Agent Zustimmung für Trades:

```python
def consensus_trade(symbol):
    scores = {
        "Momentum": score_momentum(symbol),
        "MeanReversion": score_mean_reversion(symbol),
        "Growth": score_growth(symbol),
    }
    
    top_strategy = max(scores, key=scores.get)
    avg_score = sum(scores.values()) / len(scores)
    
    # Nur kaufen wenn Top-Strategie Score > 8.0
    if avg_score > 8.0:
        return execute_trade(symbol, top_strategy)
    
    return None
```

---

## Zusammenfassung

✅ 14 Strategie-Agents eingerichtet  
✅ Kelly Criterion implementiert  
✅ Trade Executor konfiguriert  
✅ Consensus System verstanden  

**Nächstes Modul:** Memory System (MemPalace)