# 📘 Permutation Test

---

## 1. Why Permutation Test Exists

Traditional tests (t-test, ANOVA) **assume Normal distribution**. When your data is skewed, tiny, or weirdly shaped, those assumptions break and results become unreliable.

> **The Permutation Test makes ZERO assumptions about data shape.** It builds its own distribution by shuffling the data.

| | Traditional Tests | Permutation Test |
|---|------------------|-----------------|
| Assumes distribution? | Yes (Normal) | **No** |
| Works with small samples? | Risky | **Yes** |
| Works with weird data? | Risky | **Yes** |
| Speed | Fast (formula) | Slower (simulation) |

---

## 2. How It Works — "Shuffling Labels"

### The Logic:

If the treatment has **no effect**, then it doesn't matter who's in which group. Shuffling group labels should produce similar differences.

### The Steps:

| Step | Action |
|------|--------|
| 1 | Calculate the **observed difference** between groups |
| 2 | Combine all data into one pool |
| 3 | **Shuffle** randomly and split into two groups |
| 4 | Calculate the difference for this random split |
| 5 | Repeat 10,000 times |
| 6 | Count how many shuffled differences ≥ observed difference |
| 7 | p-value = count / 10,000 |

### Decision:

- **Few shuffles** match the observed gap → the effect is real (p < 0.05)
- **Many shuffles** match → the gap is just random (p > 0.05)

> **If scrambling labels changes nothing → the labels don't matter → no real effect.**
> **If scrambling labels destroys the difference → the labels DO matter → real effect.**

---

## 3. When to Use Which

| Situation | Best Test |
|-----------|----------|
| Normal data, large sample | t-test (faster) |
| Skewed/weird data, small sample | **Permutation test** (safer) |
| Not sure about distribution | **Permutation test** (always works) |

When data IS normal, both give similar results.

---

## 4. Python Code

```python
import numpy as np

drug = [2, 3, 1, 4, 2]
placebo = [5, 6, 4, 7, 5]

# Observed difference
observed_diff = np.mean(placebo) - np.mean(drug)

# Combine and shuffle
all_scores = np.array(drug + placebo)
n_permutations = 10000
count = 0

for i in range(n_permutations):
    np.random.shuffle(all_scores)
    perm_diff = np.mean(all_scores[5:]) - np.mean(all_scores[:5])
    if perm_diff >= observed_diff:
        count += 1

p_value = count / n_permutations
print(f"Permutation p-value: {p_value}")
```

---

## 5. Practical Application: Drug vs. Placebo

| Group | Pain Scores | Mean |
|-------|------------|------|
| Drug | [2, 3, 1, 4, 2] | 2.4 |
| Placebo | [5, 6, 4, 7, 5] | 5.4 |
| **Difference** | | **3.0** |

### Results:

| Method | p-value | Verdict |
|--------|---------|---------|
| Permutation test | 0.010 | ✅ Drug works |
| t-test | 0.003 | ✅ Drug works |

Both agree — the drug significantly reduces pain.
