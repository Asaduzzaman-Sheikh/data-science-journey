# 📘 Poisson & Related Distributions

---

## 1. Poisson Distribution — "Counting Events"

### What It Answers:

> *"How many events happen in a fixed time/space interval?"*

### Conditions:

| Condition | Meaning |
|-----------|---------|
| Known average rate | λ (lambda) = average events per interval |
| Independent events | One event doesn't cause another |
| No simultaneous events | Two events can't happen at the exact same instant |

### Formula:

> **P(X = k) = (e⁻λ × λᵏ) / k!**

| Symbol | Meaning |
|--------|---------|
| **λ** | Average events per interval |
| **k** | Exact count you're asking about |
| **e** | Euler's number (2.718...) |

### Unique Property:

> **Mean = Variance = λ**

If mean ≈ variance in your data, it might be Poisson.

---

## 2. Scaling Lambda

λ must match the interval of your question. Scale it proportionally:

> **λ_new = λ_original × (new interval / original interval)**

| Original Rate | New Interval | New λ |
|--------------|-------------|-------|
| 5 per 1ms | 3ms | 5 × 3 = **15** |
| 5 per 2ms | 1ms | 5 × (1/2) = **2.5** |
| 2 per week | 4 weeks | 2 × 4 = **8** |

> Shorter interval → λ shrinks. Longer interval → λ grows.

---

## 3. Poisson ↔ Binomial Connection

> **When n is large and p is small → Binomial ≈ Poisson** (with λ = n × p)

Poisson = "distribution of rare events" — many opportunities, tiny individual probability.

| Situation | Use |
|-----------|-----|
| Small n, moderate p | **Binomial** |
| Large n, small p | **Poisson** (simpler calculation) |

---

## 4. Exponential Distribution — "Time Between Events"

### The Partner of Poisson:

| Distribution | Question |
|-------------|---------|
| **Poisson** | **How many** events in a fixed time? |
| **Exponential** | **How long** until the next event? |

> If events follow Poisson with rate λ, then time between events follows Exponential with mean 1/λ.

### Formula:

> **P(X ≤ t) = 1 − e^(−λt)**

| Question | Formula |
|----------|---------|
| Event **within** time t | **1 − e^(−λt)** |
| **No** event for time t | **e^(−λt)** |

### Unit Matching Rule:

> **λ and t must be in the same unit.** Convert either one.

| λ = 2 per week, question about 2 days | |
|---------------------------------------|---|
| Option A: t = 2/7 weeks | P = 1 − e^(−2 × 2/7) |
| Option B: λ = 2/7 per day | P = 1 − e^(−2/7 × 2) |
| **Same answer either way** | |

### Python: scale = 1/λ

Python uses `scale` (average wait) instead of λ (rate):
- λ = 2 per week → scale = 1/2 = 0.5 weeks

### Memoryless Property:

> Past waiting doesn't affect future probability. If you've waited 10 minutes, the chance of waiting 5 more is the same as if you just started.

---

## 5. Weibull Distribution — "Flexible Failure Times"

### Why It Exists:

Exponential assumes **constant** failure rate. Real-world products age — failure rate changes over time. Weibull adds a **shape parameter (k)** to model this.

| Distribution | Failure Rate |
|-------------|-------------|
| **Exponential** | Constant (same at any age) |
| **Weibull** | Flexible (can increase, decrease, or stay constant) |

### The Shape Parameter (k):

| k value | Failure Rate | Example |
|---------|-------------|---------|
| **k < 1** | **Decreasing** — fails early, stabilizes | Software bugs, infant mortality |
| **k = 1** | **Constant** — same at any age | Random accidents (**= Exponential**) |
| **k > 1** | **Increasing** — more likely to fail with age | Light bulbs, engines, human aging |

### The Bathtub Curve:

Most products follow three phases:

| Phase | k | Pattern |
|-------|---|---------|
| Early life | k < 1 | Manufacturing defects cause early failures |
| Useful life | k = 1 | Random failures at constant rate |
| Wear-out | k > 1 | Parts age and break down |

### Formula:

> **P(X ≤ t) = 1 − e^(−(t/λ)^k)**

When k = 1, this simplifies to the Exponential formula.

| Parameter | Controls |
|-----------|----------|
| **λ (scale)** | How long things typically last |
| **k (shape)** | Whether failure rate increases, decreases, or stays flat |

---

## 6. Python Reference

```python
from scipy import stats

# --- Poisson ---
stats.poisson.pmf(k, λ)          # P(exactly k events)
stats.poisson.cdf(k, λ)          # P(k or fewer events)
1 - stats.poisson.cdf(k, λ)      # P(more than k events)

# --- Exponential ---
stats.expon.cdf(t, scale=1/λ)    # P(event within time t)
1 - stats.expon.cdf(t, scale=1/λ) # P(no event for time t)

# --- Weibull ---
stats.weibull_min.cdf(t, c=k, scale=λ)  # P(failure within time t)
```

---

## 7. Practical Applications

### Server Crashes (Poisson, λ = 2/week):

| Question | Answer |
|----------|--------|
| P(0 crashes this week) | **13.5%** |
| P(exactly 2 crashes) | **27.1%** |
| P(more than 4 crashes) | **5.3%** |
| P(more than 12 in a month, λ=8) | **6.4%** |

### Time Between Crashes (Exponential, λ = 2/week):

| Question | Answer |
|----------|--------|
| P(crash within 2 days) | **43.5%** |
| P(no crash for 1 week) | **13.5%** |

### Light Bulb Lifetime (Exponential vs. Weibull):

| Distribution | P(fail before 500 hours) |
|-------------|------------------------|
| Exponential (k=1) | **39.3%** — constant failure rate |
| Weibull (k=2) | **22.1%** — fewer early failures, more late failures |

---

## 8. Complete Distribution Summary

| Distribution | Question | Key Parameter |
|-------------|---------|---------------|
| **Poisson** | How many events in a period? | λ (rate) |
| **Exponential** | How long until next event? | λ (rate), constant failure |
| **Weibull** | How long until failure? | λ (scale) + k (shape) |
| **Binomial** | How many successes in n trials? | n, p |
| **Normal** | Where does a measurement fall? | μ, σ |
| **t** | Is this mean different? (small sample) | df |
| **Chi-Squared** | Do counts match expectations? | df |
| **F** | Are 3+ group means different? | df₁, df₂ |
