# 📊 Chapter 5: Box Plots & Density Plots

---

## 📦 Part 1: Box Plots

### What is a Box Plot?

A box plot is a visual summary showing the **five-number summary**:

| Number  | What It Is      |
| ------- | --------------- |
| Minimum | Smallest value  |
| Q1      | 25th percentile |
| Median  | 50th percentile |
| Q3      | 75th percentile |
| Maximum | Largest value   |

### Anatomy of a Box Plot

```
            ┌─────────────────┐
    ├───────┤        │        ├───────┤
            └─────────────────┘
    │       │        │        │       │
   Min     Q1     Median     Q3     Max
            ◄───── IQR ─────►
```

---

## 📐 Calculating Quartiles

### Step-by-Step Method

1. **Sort the data**
2. **Find Median (Q2)**: Middle value
3. **Find Q1**: Median of lower half
4. **Find Q3**: Median of upper half

### IQR (Interquartile Range)

```
IQR = Q3 - Q1
```

The IQR measures the spread of the middle 50% of data.

---

## 🚨 Outlier Detection (1.5 × IQR Rule)

```
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

**Any value outside these fences is an outlier!**

---

## 📊 Interpreting Box Plots

| Question   | What to Look At            |
| ---------- | -------------------------- |
| Center?    | Median line in box         |
| Spread?    | Width of box (IQR)         |
| Symmetric? | Is median centered in box? |
| Outliers?  | Dots beyond whiskers       |
| Range?     | Total span (min to max)    |

### Shapes in Box Plots

```
SYMMETRIC:           RIGHT-SKEWED:        LEFT-SKEWED:
    ┌──┼──┐              ┌┼────┐            ┌────┼┐
Median in center    Median left         Median right
```

---

## 🐍 Python Code: Box Plot

```python
import plotly.express as px

data = [55, 62, 68, 72, 75, 78, 80, 82, 85, 88, 92, 95]
fig = px.box(x=data, title='Box Plot', points='all')
fig.show()
```

---

## 📈 Part 2: Density Plots

### What is a Density Plot?

> A density plot is a **smoothed histogram** — bars become a continuous curve.

```
Histogram:              Density Plot:
   ██                         ╱╲
  ████                      ╱    ╲
 ██████                   ╱        ╲
████████                ╱            ╲
```

### Key Rule

> **Higher the curve = More data in that region**

---

## 📊 Interpreting Density Plots

| Question               | What to Look At |
| ---------------------- | --------------- |
| Most common values?    | Highest peak    |
| One group or multiple? | Count the peaks |
| Symmetric or skewed?   | Tail direction  |
| Spread?                | Width of curve  |

### Shapes in Density Plots

```
SYMMETRIC:          RIGHT-SKEWED:       LEFT-SKEWED:
    ╱╲                  ╱╲                     ╱╲
  ╱    ╲              ╱   ╲___              __╱   ╲
╱        ╲          ╱         →          ←        ╲
```

---

## 🐍 Python Code: Density Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

data = [55, 62, 68, 72, 75, 78, 80, 82, 85, 88, 92, 95]

# Histogram with density curve
sns.histplot(data, kde=True)
plt.show()

# Density curve only
sns.kdeplot(data, fill=True)
plt.show()
```

---

## 🔄 Comparison

| Feature                   | Box Plot        | Density Plot  |
| ------------------------- | --------------- | ------------- |
| Shows center              | Median line     | Peak location |
| Shows spread              | Box width (IQR) | Curve width   |
| Shows outliers            | Dots            | Extreme tails |
| Shows full shape          | No              | Yes (smooth)  |
| Good for comparing groups | Yes             | Yes           |

---

## 📋 Quick Reference Checklists

### Box Plot Checklist

- [ ] Where is the median line?
- [ ] Is the box wide or narrow?
- [ ] Is median centered in box?
- [ ] Are whiskers equal length?
- [ ] Any outlier dots?

### Density Plot Checklist

- [ ] How many peaks?
- [ ] Where is the highest peak?
- [ ] Is it symmetric?
- [ ] Which way does the tail go?
- [ ] Is the curve narrow or wide?
