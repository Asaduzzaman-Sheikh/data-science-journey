# 📊 Chapter 8: Pie Charts & Donut Charts

---

## 🎯 What is a Pie Chart?

A **pie chart** is a circular chart divided into slices, where each slice represents a **proportion** (percentage) of the whole.

### When to Use Pie Charts

| ✅ Good For                        | ❌ Not Good For                |
| ---------------------------------- | ------------------------------ |
| Showing parts of a whole           | Comparing many categories (>6) |
| Proportions that sum to 100%       | Showing trends over time       |
| Highlighting one dominant category | Comparing exact values         |

---

## 💻 Complete Pie Chart Code (Line-by-Line)

```python
import matplotlib.pyplot as plt

# ============================================
# STEP 1: PREPARE THE DATA
# ============================================
categories = ['CS', 'Business', 'Arts', 'Engineering']  # Slice labels
values = [40, 30, 20, 10]  # Slice sizes (must match order)

# ============================================
# STEP 2: FIND THE MODE (LARGEST SLICE)
# ============================================
max_idx = values.index(max(values))  # Find position of largest value

# ============================================
# STEP 3: CREATE EXPLODE ARRAY (Highlight mode)
# ============================================
explode = [0.1 if i == max_idx else 0 for i in range(len(values))]
# Result: [0.1, 0, 0, 0] - pulls first slice out

# ============================================
# STEP 4: DEFINE CUSTOM COLORS
# ============================================
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

# ============================================
# STEP 5: CREATE FIGURE
# ============================================
fig, ax = plt.subplots(figsize=(10, 8))  # Width=10, Height=8 inches

# ============================================
# STEP 6: CREATE THE PIE CHART
# ============================================
wedges, texts, autotexts = ax.pie(
    values,                                    # Slice sizes
    labels=categories,                         # Slice names
    autopct='%1.1f%%',                        # Show percentages
    explode=explode,                          # Pull out slices
    colors=colors,                            # Custom colors
    shadow=True,                              # Add shadow effect
    startangle=90,                            # Start from top
    textprops={'fontsize': 12, 'fontweight': 'bold'}
)

# ============================================
# STEP 7: STYLE THE PERCENTAGE TEXT
# ============================================
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# ============================================
# STEP 8: FINAL TOUCHES
# ============================================
plt.title('Student Majors', fontsize=16, fontweight='bold', pad=20)
ax.axis('equal')      # Make it circular
plt.tight_layout()
plt.show()
```

---

## 🔑 Key Parameters Explained

| Parameter     | Example            | Purpose                     |
| ------------- | ------------------ | --------------------------- |
| `values`      | `[40, 30, 20, 10]` | Size of each slice          |
| `labels`      | Category names     | Text on each slice          |
| `autopct`     | `'%1.1f%%'`        | Show percentage (1 decimal) |
| `explode`     | `[0.1, 0, 0, 0]`   | Pull slices out from center |
| `colors`      | Hex codes          | Custom slice colors         |
| `shadow`      | `True`             | Add 3D shadow effect        |
| `startangle`  | `90`               | First slice at 12 o'clock   |
| `pctdistance` | `0.75`             | Position of % text          |

### autopct Format Options

| Format      | Output |
| ----------- | ------ |
| `'%1.0f%%'` | 40%    |
| `'%1.1f%%'` | 40.0%  |
| `'%1.2f%%'` | 40.00% |

---

## 🍩 Donut Chart

A donut chart is a pie chart with a **white circle in the center**.

```python
import matplotlib.pyplot as plt

categories = ['CS', 'Business', 'Arts', 'Engineering']
values = [40, 30, 20, 10]
colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']

fig, ax = plt.subplots(figsize=(10, 8))

# Create pie chart
wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    pctdistance=0.75  # Position % text inside the ring
)

# THE MAGIC: Add white circle in center
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax.add_artist(centre_circle)

# Add text in center
ax.text(0, 0, 'Total\n100%', ha='center', va='center',
        fontsize=14, fontweight='bold')

ax.axis('equal')
plt.title('Student Majors (Donut Style)')
plt.show()
```

### Donut Center Circle Explained

| Part                                  | Meaning                                  |
| ------------------------------------- | ---------------------------------------- |
| `plt.Circle((0,0), 0.50, fc='white')` | Circle at center, radius 50%, white fill |
| `ax.add_artist(centre_circle)`        | Place circle on chart                    |

---

## 📋 Pie Chart with Legend

Best for **6+ categories** (cleaner than labels on slices):

```python
import matplotlib.pyplot as plt

categories = ['CS', 'Business', 'Arts', 'Engineering', 'Medicine', 'Law']
values = [25, 20, 15, 15, 15, 10]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

fig, ax = plt.subplots(figsize=(10, 8))

# Pie chart WITHOUT labels
wedges, texts, autotexts = ax.pie(
    values,
    autopct='%1.0f%%',
    colors=colors,
    startangle=90
)

# Add legend outside
ax.legend(wedges, categories,
          title="Majors",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

ax.axis('equal')
plt.tight_layout()
plt.show()
```

---

## 🎨 Using Seaborn Color Palettes

```python
import matplotlib.pyplot as plt
import seaborn as sns

categories = ['CS', 'Business', 'Arts', 'Engineering']
values = [40, 30, 20, 10]

# Get Seaborn palette
colors = sns.color_palette('Set2')

plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%')
plt.title('Student Majors')
plt.show()
```

### Popular Seaborn Palettes

| Palette     | Best For              |
| ----------- | --------------------- |
| `'Set1'`    | Bold, distinct colors |
| `'Set2'`    | Pastel, soft colors   |
| `'Pastel1'` | Very soft pastels     |
| `'husl'`    | Many categories (6+)  |

---

## 📋 Summary Card

```
┌─────────────────────────────────────────────────────────┐
│                    PIE & DONUT CHARTS                   │
├─────────────────────────────────────────────────────────┤
│  PIE CHART: Circular chart showing proportions          │
│  DONUT CHART: Pie + white center circle                 │
│                                                         │
│  KEY PARAMETERS:                                        │
│    • autopct    → Show percentages                      │
│    • explode    → Highlight slices                      │
│    • colors     → Custom colors                         │
│    • startangle → Rotation (90 = top)                   │
│                                                         │
│  BEST FOR: Parts of whole, proportions                  │
│  AVOID FOR: 6+ categories, trends over time             │
└─────────────────────────────────────────────────────────┘
```

---

## 🔗 Related Topics

- [07_Binary_and_Categorical_Data.md](07_Binary_and_Categorical_Data.md) - Mode and categorical data basics
