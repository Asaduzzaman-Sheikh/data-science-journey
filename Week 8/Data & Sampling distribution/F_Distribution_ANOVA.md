# 📘 F-Distribution & ANOVA

---

## 1. The Problem: Why Not Multiple t-Tests?

The t-test compares **2 groups**. With 3+ groups, you'd need many t-tests (3 groups = 3 tests, 5 groups = 10 tests). Each test carries a 5% false alarm risk — more tests = more false alarms.

**ANOVA** solves this by comparing **all groups at once** in a single test using the **F-distribution** (named after Ronald Fisher).

| Situation | Test |
|-----------|------|
| Compare 2 group means | t-test |
| Compare 3+ group means | **ANOVA (F-test)** |

---

## 2. How the F-Test Works

### Core Idea:

> **F = Variance BETWEEN groups / Variance WITHIN groups**

| Component | Measures |
|-----------|---------|
| **Between-group** | How far each group mean is from the **Grand Mean** |
| **Within-group** | How far individual values are from their **own group mean** |

### Interpreting F-Values:

| F-value | Meaning |
|---------|---------|
| **F ≈ 1** | Between ≈ Within → Groups are similar |
| **F >> 1** | Between >> Within → Groups are truly different |

> **F tells you how many times bigger the between-group differences are compared to the natural noise within groups.**

### Degrees of Freedom:

| df | Formula |
|----|---------|
| **df₁** | k − 1 (k = number of groups) |
| **df₂** | N − k (N = total observations) |

---

## 3. ANOVA Assumptions

| # | Assumption |
|---|-----------|
| 1 | **Independence** — observations don't influence each other |
| 2 | **Normality** — each group's data is roughly normally distributed |
| 3 | **Equal variance** — each group has roughly the same spread |

---

## 4. ANOVA's Limitation

ANOVA says *"at least one group is different"* but **NOT which groups differ**.

| Step | Tool | Answers |
|------|------|---------|
| **Step 1** | ANOVA | "Are ANY groups different?" (Yes/No) |
| **Step 2** | Post-hoc test (Tukey HSD) | "WHICH specific groups differ?" |

---

## 5. Reading Tukey HSD Output

| Column | Meaning |
|--------|---------|
| **group1, group2** | The two groups being compared |
| **meandiff** | Difference in means (group2 − group1) |
| **p-adj** | Adjusted p-value (accounts for multiple comparisons) |
| **lower** | Lower bound of 95% confidence interval for the difference |
| **upper** | Upper bound of 95% confidence interval for the difference |
| **reject** | True = significantly different, False = not different |

### Lower & Upper (Confidence Interval):

Same concept as margin of error, applied to the **difference between groups**:

| Interval | Meaning |
|----------|---------|
| Both positive | Group 2 tips MORE for sure ✅ |
| Both negative | Group 2 tips LESS for sure ✅ |
| Crosses zero (negative to positive) | Can't be sure ❌ |

---

## 6. Relationship to Other Tests

| Test | Compares | Data Type |
|------|---------|-----------|
| **t-test** | 2 group means | Numerical |
| **ANOVA (F-test)** | 3+ group means | Numerical |
| **Chi-Squared** | Proportions/counts | Categorical |

> With exactly 2 groups, ANOVA and t-test give the **same p-value** (F = t²).

---

## 7. Python Reference

```python
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Step 1: ANOVA
group1 = df[df['category'] == 'A']['value']
group2 = df[df['category'] == 'B']['value']
group3 = df[df['category'] == 'C']['value']

f_stat, p_value = stats.f_oneway(group1, group2, group3)

# Step 2: Post-hoc (only if ANOVA is significant)
tukey = pairwise_tukeyhsd(df['value'], df['category'], alpha=0.05)
print(tukey)
```

---

## 8. Practical Application: Tips by Party Size 🍽️

### ANOVA Result:

| Test | F-value | p-value | Significant? |
|------|---------|---------|-------------|
| Tips by Day | 1.67 | 0.174 | ❌ No |
| **Tips by Party Size** | **15.75** | **2.17 × 10⁻¹³** | **✅ Yes** |

### Tukey HSD Key Findings:

**Significantly different pairs (reject = True):**

| Pair | Mean Difference | p-adj |
|------|----------------|-------|
| Size 1 vs 3 | +$1.96 | 0.029 |
| Size 1 vs 4 | +$2.70 | 0.0005 |
| Size 1 vs 5 | +$2.59 | 0.020 |
| Size 1 vs 6 | +$3.79 | 0.0002 |
| Size 2 vs 3 | +$0.81 | 0.004 |
| Size 2 vs 4 | +$1.55 | 0.000 |
| Size 2 vs 6 | +$2.64 | 0.0003 |

### Business Insight:

> *"Party size significantly affects tip amounts. The key divide is between small parties (1-2) and large parties (3+). Among large parties, tips are similar. The day of the week does not affect tip amounts."*
