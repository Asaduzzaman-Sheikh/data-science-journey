# 📊 Chapter 4: Shapes of Distributions

---

## 🎯 Why Shape Matters

The shape of a distribution tells you:

- Where most values cluster
- Which statistical measures to use
- Whether your data has problems (outliers, mixed groups)

---

## 🔑 The Five Main Shapes

| Shape            | Visual         | Key Feature      |
| ---------------- | -------------- | ---------------- |
| **Symmetric**    | ⛰️ Bell-shaped | Mean ≈ Median    |
| **Right-Skewed** | 📈 Tail right  | Mean > Median    |
| **Left-Skewed**  | 📉 Tail left   | Mean < Median    |
| **Bimodal**      | 🏔️🏔️ Two peaks | Two groups mixed |
| **Uniform**      | ▬ Flat         | All values equal |

---

## 📐 Three Methods to Determine Shape

### Method 1: Visualize It (Best Method!)

Create a histogram and look at it:

- Where is the peak?
- Where does the tail extend?

```python
import matplotlib.pyplot as plt
plt.hist(data, bins='auto', edgecolor='black')
plt.show()
```

### Method 2: Compare Mean vs Median

| If...         | Shape is...  |
| ------------- | ------------ |
| Mean ≈ Median | Symmetric    |
| Mean > Median | Right-Skewed |
| Mean < Median | Left-Skewed  |

```python
import numpy as np
mean = np.mean(data)
median = np.median(data)
print(f"Mean: {mean}, Median: {median}")
```

### Method 3: Calculate Skewness

```python
from scipy import stats
skewness = stats.skew(data)
```

| Skewness Value | Shape                   |
| -------------- | ----------------------- |
| -0.5 to 0.5    | Symmetric               |
| 0.5 to 1.0     | Moderately right-skewed |
| > 1.0          | Highly right-skewed     |
| -1.0 to -0.5   | Moderately left-skewed  |
| < -1.0         | Highly left-skewed      |

---

## 📊 Shape Examples

### 1. Symmetric (Marathon Times)

```
Data: 235, 238, 242, 245, 248, 250, 252, 255, 258, 262, 265, 268
Mean: 251.5, Median: 251.0, Skewness: 0.024
→ Use Mean or Median (both similar)
```

### 2. Right-Skewed (House Prices)

```
Data: 150, 165, 175, 180, 190, 195, 205, 210, 220, 850
Mean: 254, Median: 192.5, Skewness: 2.62
→ Use MEDIAN (mean inflated by $850K outlier)
```

### 3. Left-Skewed (Test Scores)

```
Data: 45, 52, 67, 71, 73, 75, 78, 79, 80, 81, 82, 83, 85, 86, 88, 89, 91, 93, 95, 98
Mean: 76.55, Median: 81.5, Skewness: -1.11
→ Use MEDIAN (mean pulled down by low scores)
```

### 4. Bimodal (Mixed Heights)

```
Group A: 152, 155, 157, 160, 162, 165 (females)
Group B: 178, 180, 182, 185, 188, 190 (males)
Mean: 171.2, Median: 171.5
→ Average represents NO ONE! Report separately.
```

### 5. Uniform (Dice Rolls)

```
Each value (1-6) appears 10 times
Mean: 3.5, Median: 3.5
→ All values equally likely, no peak
```

---

## 🚨 The Key Rule

> **"The Tail Tells the Tale"**
>
> - Tail points RIGHT → Right-skewed → Mean > Median
> - Tail points LEFT → Left-skewed → Mean < Median

---

## 📋 When to Use Mean vs Median

| Shape                  | Use            | Why                           |
| ---------------------- | -------------- | ----------------------------- |
| Symmetric              | Mean or Median | Both are similar              |
| Skewed (any direction) | **MEDIAN**     | Mean is pulled by outliers    |
| Bimodal                | Neither alone  | Report both groups separately |
| Uniform                | Mean or Median | Both are center               |

---

## 🧠 Real-World Applications

| Situation          | Why Shape Matters                 |
| ------------------ | --------------------------------- |
| Salary negotiation | Median salary is more realistic   |
| House hunting      | Median price is typical           |
| Medical research   | Choose correct statistical tests  |
| Quality control    | Detect data problems              |
| Machine learning   | May need to transform skewed data |

---

## 📝 Practice Problems Completed

1. ✅ Symmetric - Marathon times (skewness ≈ 0)
2. ✅ Left-skewed - Test scores (skewness = -1.11)
3. ✅ Right-skewed - House prices (skewness = 2.62)
4. ✅ Bimodal - Mixed heights (two peaks)
5. ✅ Uniform - Dice rolls (flat, no peak)
