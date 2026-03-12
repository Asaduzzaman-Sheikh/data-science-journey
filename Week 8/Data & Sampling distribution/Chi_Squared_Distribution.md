# 📘 Chi-Squared (χ²) Distribution

---

## 1. What Is Chi-Squared? — "The Quality Inspector" 🔍

Chi-Squared tests whether **observed counts** match **expected counts**. It answers:

> *"Is the difference between what I EXPECTED and what I OBSERVED big enough to be suspicious? Or is it just random noise?"*

- **Small χ²** → Differences are tiny → Probably random chance ✅
- **Large χ²** → Differences are too big → Something real is happening ⚠️

---

## 2. Chi-Squared vs. t-Test — "When to Use Which"

| Feature | t-Test | Chi-Squared (χ²) |
|---------|--------|------------------|
| **Data type** | Numbers (tips, heights, prices) | **Categories** (colors, yes/no, gender) |
| **You're looking at** | How much? (averages) | How many? (counts in groups) |
| **Question** | "Is the **mean** different?" | "Are the **proportions** different?" |
| **Analogy** | Weighing scale 🏋️ | Pie chart 🥧 |

> **t-Test** = *"Is this person heavier than average?"* (a number)
> **Chi-Squared** = *"Are the pie slices the right size?"* (proportions)

---

## 3. The Formula — "Measuring Suspicion"

**χ² = Σ (Observed − Expected)² / Expected**

### Breaking It Down

| Step | What It Does | Why |
|------|-------------|-----|
| **(O − E)** | How far off is each group? | Raw difference |
| **(O − E)²** | Square it | Makes all positive + punishes big differences more |
| **÷ Expected** | Normalize by size | 5 off from 20 (25% error) is worse than 5 off from 1,000 (0.5% error) |
| **Σ (sum)** | Add up all categories | Total "suspicion score" |

---

## 4. Understanding p-value — "The Courtroom" ⚖️

The p-value answers: *"If nothing special is happening, how likely is it to see results this extreme just by random chance?"*

| p-value | Verdict |
|---------|---------|
| **< 0.05** | Strong **evidence** something is different/suspicious |
| **> 0.05** | **Not enough evidence** to say it's different |

### ⚠️ Critical Distinction

- p < 0.05 does NOT **prove** guilt — it provides **strong evidence**
- p > 0.05 does NOT **prove** innocence — it means **not enough evidence** (like "not guilty" ≠ "innocent")

---

## 5. Interpreting χ² Values

| χ² Value | Meaning |
|----------|---------|
| **~0** | Reality matches expectations → **Independent / No pattern** |
| **Small** | Slight differences → Probably random noise |
| **Large** | Huge differences → **Dependent / Real pattern exists** |

> **χ² close to 0 → Independent. χ² far from 0 → Dependent.**
> Always confirm with p-value.

---

## 6. Degrees of Freedom

| Test Type | Formula |
|-----------|---------|
| **Goodness of Fit** | df = categories − 1 |
| **Test of Independence** | df = (rows − 1) × (columns − 1) |

---

## 7. Two Types of Chi-Squared Tests

### Type 1: Goodness of Fit 🧩

> *"Does my data FIT the expected pattern?"*

- **One variable**, compared to a known expected distribution
- Examples: Is a die fair? Are candy colors equally distributed?

### Type 2: Test of Independence 🔗

> *"Are these two variables CONNECTED or INDEPENDENT?"*

- **Two variables**, checking if one affects the other
- Uses a cross-tabulation (contingency table)
- Examples: Does gender affect survival? Is smoking related to cancer?

| | Goodness of Fit | Test of Independence |
|---|----------------|---------------------|
| **Variables** | 1 | 2 |
| **Question** | "Does this match the pattern?" | "Are these two things related?" |
| **Python function** | `stats.chisquare()` | `stats.chi2_contingency()` |

---

## 8. Python Reference

```python
from scipy import stats
import pandas as pd

# --- Goodness of Fit ---
observed = np.array([62, 19, 87, 76])
expected = np.array([61, 61, 61, 61])
chi2, p_value = stats.chisquare(observed, expected)

# --- Test of Independence ---
crosstab = pd.crosstab(df['variable1'], df['variable2'])
chi2, p_value, dof, expected_freq = stats.chi2_contingency(crosstab)
```

---

## 9. Practical Application 1: Customer Distribution (Goodness of Fit) 🍽️

**Question:** Do customers visit the restaurant equally across all four days?

| Day | Expected | Actual |
|-----|----------|--------|
| Thur | 61 | 62 |
| Fri | 61 | **19** |
| Sat | 61 | **87** |
| Sun | 61 | 76 |

**Result:** χ² = 43.7, p-value = 1.74 × 10⁻⁹

**Verdict:** Customer visits are **NOT** equally distributed. Weekends (Sat & Sun) are much busier. Friday is dramatically slower.

---

## 10. Practical Application 2: Titanic Gender vs. Survival (Independence) 🚢

**Question:** Did gender affect survival on the Titanic?

### Contingency Table

| | Died | Survived | Survival Rate |
|---|-----|---------|--------------|
| **Female** | 81 | 233 | **74.2%** |
| **Male** | 468 | 109 | **18.9%** |

**Result:** χ² = 260.7, p-value = 1.2 × 10⁻⁵⁸

**Verdict:** Gender and survival are **strongly dependent**. Women survived at nearly 4× the rate of men. The "women and children first" protocol had a measurable, statistically significant impact.

---

## 11. Summary: All Tests Compared

| Test | Data Type | Question | Key Output |
|------|-----------|----------|------------|
| **t-Test** | Numbers | "Is the mean different?" | t-stat + p-value |
| **χ² Goodness of Fit** | Categories (1 var) | "Does this match the pattern?" | χ² + p-value |
| **χ² Independence** | Categories (2 vars) | "Are these related?" | χ² + p-value |
| **Binomial** | Binary outcomes | "How likely is k successes?" | Probability |
