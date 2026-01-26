# Chapter 4: The Correlation Coefficient (r)

## 🎯 Why Do We Need a Number?

Looking at scatter plots, you can **see** correlation visually. But you can't:
- Measure it precisely
- Compare strengths objectively
- Communicate it clearly

**Solution:** The correlation coefficient (**r**) — a single number that captures both direction and strength.

---

## 📏 The Range of r

```
   -1 ←――――――――――――0――――――――――――→ +1
    │              │              │
 Perfect         No           Perfect
 Negative    Correlation     Positive
```

### Interpretation Guide

| r value | Strength | Direction |
|---------|----------|-----------|
| -1.0 | Perfect | Negative |
| -0.9 to -0.7 | Strong | Negative |
| -0.7 to -0.4 | Moderate | Negative |
| -0.4 to -0.1 | Weak | Negative |
| -0.1 to +0.1 | None/Negligible | — |
| +0.1 to +0.4 | Weak | Positive |
| +0.4 to +0.7 | Moderate | Positive |
| +0.7 to +0.9 | Strong | Positive |
| +1.0 | Perfect | Positive |

### Two Components of r

```
r = -0.75
    │  │
    │  └── Magnitude (0.75) → STRENGTH
    │
    └───── Sign (-) → DIRECTION
```

---

## 📐 The Two Formulas

### Version 1: Conceptual/Deviation Formula

$$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}$$

**Best for:** Understanding WHY correlation works

### Version 2: Computational/Raw Score Formula

$$r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

**Best for:** Exam calculations (fewer steps!)

---

## 📖 Symbol Meanings

### Version 1 Symbols

| Symbol | Meaning |
|--------|---------|
| $x_i$ | Each individual x value |
| $y_i$ | Each individual y value |
| $\bar{x}$ | Mean (average) of all x values |
| $\bar{y}$ | Mean (average) of all y values |
| $(x_i - \bar{x})$ | Deviation: how far x is from its mean |

### Version 2 Symbols

| Symbol | How to Calculate |
|--------|------------------|
| $n$ | Count of data pairs |
| $\sum x$ | Add all x values |
| $\sum y$ | Add all y values |
| $\sum xy$ | Multiply each pair, then add all |
| $\sum x^2$ | Square each x, then add all |
| $(\sum x)^2$ | Add all x first, then square the sum |

---

## ⚠️ CRITICAL: Common Mistake

### $\sum x^2$ vs $(\sum x)^2$ — NOT THE SAME!

| Notation | Steps | Example (x = 2, 3, 5) |
|----------|-------|----------------------|
| $\sum x^2$ | Square FIRST, then add | $4 + 9 + 25 = 38$ |
| $(\sum x)^2$ | Add FIRST, then square | $(10)^2 = 100$ |

**This is the #1 mistake on exams!**

---

## 🎓 When to Use Which Formula?

| Situation | Use | Why |
|-----------|-----|-----|
| **Exam (by hand)** | Version 2 | Fewer calculations |
| **Given means already** | Version 1 | Skip calculating means |
| **Understanding concept** | Version 1 | Shows deviations from average |
| **Coding manually** | Either | Both work |
| **Real-world/Industry** | Built-in functions | `df['x'].corr(df['y'])` |

---

## 📝 Step-by-Step Calculation (Version 2)

### Step 1: Create a Table

| Point | x | y | xy | x² | y² |
|-------|---|---|----|----|-----|
| 1 | | | | | |
| 2 | | | | | |
| **Sum** | Σx | Σy | Σxy | Σx² | Σy² |

### Step 2: Calculate Each Cell
- xy = x × y for each row
- x² = x × x for each row
- y² = y × y for each row

### Step 3: Sum Each Column

### Step 4: Plug Into Formula
$$r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

### Step 5: Interpret Result
- Sign → Direction
- Magnitude → Strength

---

## 📊 Worked Example

**Data:** Study Hours (x) vs Exam Score (y)

| Student | x | y |
|---------|---|---|
| A | 2 | 65 |
| B | 3 | 70 |
| C | 5 | 80 |
| D | 7 | 85 |
| E | 8 | 90 |

### Step 1: Build Table

| Student | x | y | xy | x² | y² |
|---------|---|---|----|----|-----|
| A | 2 | 65 | 130 | 4 | 4225 |
| B | 3 | 70 | 210 | 9 | 4900 |
| C | 5 | 80 | 400 | 25 | 6400 |
| D | 7 | 85 | 595 | 49 | 7225 |
| E | 8 | 90 | 720 | 64 | 8100 |
| **Sum** | **25** | **390** | **2055** | **151** | **30850** |

### Step 2: Identify Values
- n = 5
- Σx = 25
- Σy = 390
- Σxy = 2055
- Σx² = 151
- Σy² = 30850

### Step 3: Calculate Numerator
$$n(\sum xy) - (\sum x)(\sum y) = 5(2055) - (25)(390) = 10275 - 9750 = 525$$

### Step 4: Calculate Denominator

First bracket:
$$n\sum x^2 - (\sum x)^2 = 5(151) - (25)^2 = 755 - 625 = 130$$

Second bracket:
$$n\sum y^2 - (\sum y)^2 = 5(30850) - (390)^2 = 154250 - 152100 = 2150$$

Square root:
$$\sqrt{130 \times 2150} = \sqrt{279500} = 528.77$$

### Step 5: Final Answer
$$r = \frac{525}{528.77} = 0.993$$

### Step 6: Interpretation
- **Sign:** Positive (+) → Same direction
- **Magnitude:** 0.993 → Very strong
- **Conclusion:** Very strong positive correlation

---

## 🐍 Python Code for Correlation

### Using Built-in Functions (Recommended)
```python
# NumPy
r = np.corrcoef(x, y)[0, 1]

# Pandas
r = df['column1'].corr(df['column2'])

# SciPy (also gives p-value)
from scipy.stats import pearsonr
r, p_value = pearsonr(x, y)
```

### Manual Implementation (Version 2)
```python
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)
sum_y2 = np.sum(y**2)

numerator = n * sum_xy - sum_x * sum_y
denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

r = numerator / denominator
```

---

## 🔑 Key Takeaways

1. **r ranges from -1 to +1**
2. **Sign = Direction**, **Magnitude = Strength**
3. **Two formulas exist** — same result, different purposes
4. **Version 2 is easier for exams** — make a table, sum columns
5. **Watch out for $\sum x^2$ vs $(\sum x)^2$** — #1 mistake!
6. **In practice, use built-in functions** — but understand the concept

---

## 📝 Self-Check Questions

1. What does r = -0.85 tell you about direction and strength?
2. Which is stronger: r = +0.3 or r = -0.6?
3. Calculate Σx² and (Σx)² for x = [1, 2, 3, 4]
4. Why do professionals use `df['x'].corr(df['y'])` instead of the formula?

---

## 📋 Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│            PEARSON CORRELATION COEFFICIENT (r)              │
├─────────────────────────────────────────────────────────────┤
│  RANGE: -1 ≤ r ≤ +1                                         │
│                                                             │
│  SIGN: + positive, - negative                               │
│  MAGNITUDE: closer to 1 = stronger                          │
├─────────────────────────────────────────────────────────────┤
│  FORMULA (for exams):                                       │
│                                                             │
│         n(Σxy) - (Σx)(Σy)                                   │
│    r = ─────────────────────────────────────                │
│        √[nΣx² - (Σx)²][nΣy² - (Σy)²]                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  STEPS:                                                     │
│  1. Make table: x, y, xy, x², y²                            │
│  2. Sum each column                                         │
│  3. Plug into formula                                       │
│  4. Interpret: sign + magnitude                             │
├─────────────────────────────────────────────────────────────┤
│  ⚠️ REMEMBER: Σx² ≠ (Σx)²                                   │
└─────────────────────────────────────────────────────────────┘
```

---

*Next Chapter: Practice Problems and Advanced Topics*
