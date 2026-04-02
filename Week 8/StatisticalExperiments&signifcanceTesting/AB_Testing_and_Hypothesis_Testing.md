# 📘 A/B Testing & Hypothesis Testing

---

## 1. What Is Hypothesis Testing?

### The Framework Behind ALL Statistical Tests

> **"Assume nothing is happening. If the data is too weird to happen by chance, then SOMETHING is happening."**

### The Steps (Always the Same):

| Step | Action |
|------|--------|
| 1 | State H₀ (nothing special is happening) |
| 2 | State H₁ (something IS different) |
| 3 | Collect data |
| 4 | Calculate test statistic |
| 5 | Get p-value |
| 6 | p < 0.05 → reject H₀; p > 0.05 → fail to reject H₀ |

### Why We Need It:

> **Human intuition cannot tell the difference between a real pattern and random noise. The math can.**

Without hypothesis testing, businesses waste money, doctors approve bad drugs, and decisions are based on luck.

---

## 2. Every Test You Know Follows This Framework

| Test | H₀ (Default Assumption) | Data Type |
|------|------------------------|-----------|
| **t-test** | "These 2 group means are the same" | Numerical |
| **ANOVA** | "All 3+ group means are the same" | Numerical |
| **Chi-Squared** | "These categories are independent" | Categorical |
| **Z-test** | "These 2 proportions are the same" | Proportions |

> **Hypothesis testing = the recipe. t-test, Chi-Squared, ANOVA = different dishes made with the same recipe.**

---

## 3. Type I and Type II Errors

### Two Ways to Be Wrong:

| | H₀ Actually TRUE | H₀ Actually FALSE |
|---|-----------------|-------------------|
| **Reject H₀** | **Type I (α)** — False Alarm 🚨 | ✅ Correct |
| **Fail to reject H₀** | ✅ Correct | **Type II (β)** — Missed It 😴 |

### Memory Trick:

| Error | You Said | Reality | Example |
|-------|---------|---------|---------|
| **Type I** | "Something is happening!" | Nothing was happening | Fire alarm but no fire |
| **Type II** | "Nothing is happening" | Something WAS happening | Cancer test says "fine" but cancer exists |

### Which Is Worse? Depends on Context:

| Context | Worse Error | Why |
|---------|------------|-----|
| Drug testing | Type I | Approving a harmful drug |
| Cancer screening | Type II | Missing real cancer |
| A/B testing | Type I | Wasting money on useless change |

---

## 4. Statistical Power

> **Power = 1 − β = Probability of detecting a real difference when one exists**

| Power | Meaning |
|-------|---------|
| 0.80 (80%) | Industry standard — catches real effects 80% of the time |
| 0.50 | Coin flip — misses real differences half the time |
| 0.95 | Very strong — almost guaranteed to catch real differences |

### What Increases Power:

| Factor | Effect |
|--------|--------|
| **Larger sample size** | More data = clearer signal |
| **Larger effect size** | Big differences are easier to spot |
| **Higher α** | Easier to reject H₀, but more false alarms |

### The Trade-Off:

> Reducing Type I risk (lower α) → Increases Type II risk (lower power)
> Reducing Type II risk → Need more data or accept more false alarms

---

## 5. What Is A/B Testing?

A **controlled experiment** where you split users into two groups:

- **Group A (Control):** The original version
- **Group B (Treatment):** The new version

Then use hypothesis testing to determine if the difference is real.

> **A/B testing isn't a new test — it's a framework that USES the tests you already know.**

### Which Test to Use:

| Data Type | Test |
|-----------|------|
| Proportions (buy/don't buy) | Chi-Squared or Z-test |
| Continuous values (average revenue) | t-test |
| 3+ variants (A/B/C) | ANOVA |

---

## 6. Practical Application: Checkout Page A/B Test

### Scenario:

Testing two checkout page designs — same 1.5% improvement (5.0% vs 6.5%).

### Results by Sample Size:

| Sample Size | χ² | p-value | Significant? |
|------------|-----|---------|-------------|
| 1,000/group | 1.81 | 0.179 | ❌ No |
| **5,000/group** | **10.10** | **0.001** | **✅ Yes** |

### Key Insight:

> **The difference was real BOTH times. But with 1,000 visitors, the test lacked power to detect it. With 5,000, it had enough power.**

### Python Code:

```python
import numpy as np
from scipy import stats

# Create contingency table
observed = np.array([
    [250, 4750],   # Group A: [bought, didn't buy]
    [325, 4675]    # Group B: [bought, didn't buy]
])

# Run Chi-Squared test
chi2, p_value, dof, expected = stats.chi2_contingency(observed)
print(f"Chi-squared: {chi2:.3f}")
print(f"p-value: {p_value:.3f}")
```

---

## 7. Summary: The Complete Decision Framework

```
Start
  │
  ▼
State H₀ and H₁
  │
  ▼
Collect Data
  │
  ▼
Choose Test (t-test / Chi-Squared / ANOVA)
  │
  ▼
Calculate test statistic + p-value
  │
  ▼
p < 0.05? ──Yes──▶ Reject H₀ (evidence of a difference)
  │                    ⚠️ Risk: Type I error (false alarm)
  No
  │
  ▼
Fail to reject H₀ (not enough evidence)
  ⚠️ Risk: Type II error (missed real difference)
  💡 Solution: Get more data (increase power)
```
