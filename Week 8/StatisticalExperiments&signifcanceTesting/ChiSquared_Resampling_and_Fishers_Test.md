# 📘 Chi-Squared Resampling & Fisher's Exact Test

---

## 1. Chi-Squared: Three Approaches

| Approach | How It Works | Assumptions |
|----------|-------------|-------------|
| **Statistical Theory** | χ² formula → look up χ² distribution | Expected counts ≥ 5 |
| **Resampling** | χ² formula → shuffle labels 10,000 times | **None** |
| **Fisher's Exact** | Calculates exact probability | **None** (best for small samples) |

> All three answer the same question: *"Is the difference in categories real or random?"*

---

## 2. Chi-Squared Resampling Approach

### How It Works:

| Step | Action |
|------|--------|
| 1 | Calculate observed χ² from real data |
| 2 | Pool all outcomes together |
| 3 | Shuffle group labels randomly |
| 4 | Build new contingency table from shuffled data |
| 5 | Calculate χ² for shuffled table |
| 6 | Repeat 10,000 times |
| 7 | p-value = proportion of shuffled χ² ≥ observed χ² |

### Python Code:

```python
import numpy as np
from scipy import stats

# Observed chi-squared
observed = np.array([[50, 950], [65, 935]])
observed_chi2 = stats.chi2_contingency(observed)[0]

# Resampling
all_outcomes = np.array(["buy"]*115 + ["no"]*1885)
n_perm = 10000
count = 0

for i in range(n_perm):
    np.random.shuffle(all_outcomes)
    grpA = all_outcomes[:1000]
    grpB = all_outcomes[1000:]
    countA = np.sum(grpA == "buy")
    countB = np.sum(grpB == "buy")
    table = np.array([[countA, 1000-countA],
                      [countB, 1000-countB]])
    chi2_perm = stats.chi2_contingency(table)[0]
    if chi2_perm >= observed_chi2:
        count += 1

p_value = count / n_perm
```

### Practical Result:

| Method | p-value |
|--------|---------|
| Statistical theory | 0.179 |
| Resampling | 0.180 |

> Both agree — when data is well-behaved, both give the same answer. When data is weird, trust resampling.

---

## 3. Fisher's Exact Test

### When to Use:

> **If any expected count in your contingency table is less than 5 → use Fisher's instead of Chi-Squared.**

The Chi-Squared formula divides by Expected. Small Expected values inflate χ² artificially, making the approximation unreliable.

### Python Code:

```python
table = np.array([[5, 1],
                  [1, 5]])

# Fisher's Exact Test
odds_ratio, p_value = stats.fisher_exact(table)
```

### Output:

| Column | Meaning |
|--------|---------|
| **odds_ratio** | How many times more likely one group succeeds vs the other |
| **p_value** | Exact probability (no approximation) |

### Practical Result (Rare Disease Treatment):

| Test | Statistic | p-value |
|------|----------|---------|
| Chi-Squared | χ² = 3.0 | 0.083 |
| Fisher's Exact | OR = 25.0 | 0.080 |

Both say not significant (p > 0.05) — despite 5/6 vs 1/6 cure rates. **Small sample = low power.**

> A non-significant result doesn't mean "no effect." It means "not enough evidence."

---

## 4. Complete Decision Guide

```
Categorical Data?
  │
  ├── Expected counts ≥ 5?
  │     ├── Yes → Chi-Squared (statistical theory)
  │     └── No  → Fisher's Exact Test
  │
  └── Want no assumptions?
        └── Chi-Squared Resampling (always works)
```

---

## 5. All Testing Methods Summary

| Test | Data Type | Best For |
|------|-----------|----------|
| **t-test** | Numerical, 2 groups | Comparing 2 means |
| **ANOVA** | Numerical, 3+ groups | Comparing 3+ means |
| **Chi-Squared** | Categorical, large sample | Independence/Goodness of Fit |
| **Fisher's Exact** | Categorical, small sample | When expected counts < 5 |
| **Permutation** | Any | No distribution assumptions |
| **Chi-Squared Resampling** | Categorical | No distribution assumptions |
