# Chapter 3: Visualizing Correlation with Scatter Plots

## 🎯 What is a Scatter Plot?

A **scatter plot** shows each data point as a dot on a graph:
- **X-axis** = One variable
- **Y-axis** = Other variable
- **Each dot** = One observation (one data pair)

---

## 📊 How to Read Scatter Plots

### Positive Correlation (↗️)
```
Points go from BOTTOM-LEFT to TOP-RIGHT

       •  •
      •  •
     •  •
    •  •
   • •
```
- As x increases, y increases
- Example: Study hours vs Exam score

### Negative Correlation (↘️)
```
Points go from TOP-LEFT to BOTTOM-RIGHT

• •
 •  •
  •  •
   •  •
    •  •
```
- As x increases, y decreases
- Example: Speed vs Travel time

### Zero Correlation (🔀)
```
Points scattered RANDOMLY - no pattern

  •    •
•     •   •
   •    •
 •   •     •
```
- No relationship between x and y
- Example: Shoe size vs IQ

---

## 🐍 Python Code for Scatter Plots

### Basic Setup
```python
import numpy as np
import matplotlib.pyplot as plt
```

### Creating Sample Data

#### Positive Correlation Data
```python
np.random.seed(42)  # For reproducibility
n = 50  # Number of data points

# X variable: random values
x = np.random.uniform(1, 10, n)

# Y variable: increases with x (plus noise)
y = 50 + 5 * x + np.random.normal(0, 5, n)
```

#### Negative Correlation Data
```python
# X variable
x = np.random.uniform(30, 100, n)

# Y variable: decreases with x (note the MINUS sign)
y = 200 - 1.5 * x + np.random.normal(0, 10, n)
```

#### Zero Correlation Data
```python
# X and Y are completely independent
x = np.random.uniform(6, 12, n)
y = np.random.uniform(85, 130, n)  # Doesn't use x at all!
```

### Creating the Scatter Plot
```python
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='green', alpha=0.7, s=80)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot Title')
plt.show()
```

---

## 🔧 Understanding the Code

### `np.random.uniform(low, high, size)`
- Generates random numbers where **every value is equally likely**
- Like spinning a fair wheel
- Example: `np.random.uniform(1, 10, 50)` → 50 random numbers between 1-10

### `np.random.normal(mean, std, size)`
- Generates random numbers following a **bell curve**
- Most values cluster around the mean
- Example: `np.random.normal(0, 5, 50)` → 50 numbers centered at 0, mostly within ±5

### Why Add Noise?
Real data is never perfect! The noise simulates:
- Natural variation
- Measurement errors
- Other factors we're not measuring

---

## 🎨 Scatter Plot Parameters

| Parameter | What It Does | Example |
|-----------|--------------|---------|
| `figsize=(8, 6)` | Width and height in inches | 8 wide, 6 tall |
| `color='green'` | Dot color | 'red', 'blue', '#FF5733' |
| `alpha=0.7` | Transparency (0-1) | 0.7 = slightly see-through |
| `s=80` | Dot size | Larger number = bigger dots |

---

## 🔑 Key Takeaways

1. **Scatter plots visualize relationships** between two variables
2. **Direction of points** shows correlation type:
   - ↗️ Bottom-left to top-right = Positive
   - ↘️ Top-left to bottom-right = Negative
   - 🔀 Random scatter = Zero
3. **Not all points follow the pattern** — that's normal (it's about tendency)
4. **Noise makes data realistic** — perfect lines don't exist in real world

---

## 📝 Self-Check Questions

1. If points go from top-left to bottom-right, what type of correlation is this?
2. What does `alpha=0.5` do in a scatter plot?
3. Why don't all points fall exactly on a line even with strong correlation?
4. How would you create data where y decreases as x increases?

---

*Next Chapter: The Correlation Coefficient (r) — Measuring Correlation with Numbers*
