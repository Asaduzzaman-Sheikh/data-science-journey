# 📊 Chapter 3: Visualizing Distributions (with Python)

---

## 🎯 Why Visualize?

Numbers in a table are hard to read. Pictures make patterns obvious!

> **Visualization makes distributions easy to understand at a glance.**

---

## 🛠️ Python Setup

```python
import pandas as pd              # For data organization
import matplotlib.pyplot as plt  # For static charts
import plotly.express as px      # For interactive charts
```

---

## 📋 Building a Complete Frequency Table

### Step-by-Step Code

```python
import pandas as pd

# Raw data
fruits = ['Apple', 'Banana', 'Apple', 'Orange', 'Apple', 'Banana', 'Mango', 
          'Apple', 'Orange', 'Banana', 'Apple', 'Mango', 'Banana', 'Apple', 
          'Orange', 'Banana', 'Apple', 'Mango', 'Banana', 'Apple', 'Orange', 
          'Apple', 'Banana', 'Mango', 'Apple', 'Orange', 'Banana', 'Mango', 
          'Apple', 'Orange']

# Step 1: Create frequency table
df = pd.DataFrame({'Fruits': fruits})
frequency_table = df['Fruits'].value_counts().reset_index(name='Count')

# Step 2: Relative Frequency
frequency_table['Relative Frequency'] = frequency_table['Count'] / frequency_table['Count'].sum()
frequency_table['Relative Frequency'] = frequency_table['Relative Frequency'].round(2)

# Step 3: Percentage
frequency_table['Percentage'] = frequency_table['Relative Frequency'] * 100

# Step 4: Cumulative Frequency
frequency_table['Cumulative Frequency'] = frequency_table['Count'].cumsum()

# Step 5: Cumulative Relative Frequency
frequency_table['Cumulative Rel Freq'] = frequency_table['Cumulative Frequency'] / frequency_table['Count'].sum()

# Step 6: Add Total Row
frequency_table.loc[len(frequency_table)] = {
    'Fruits': 'Total',
    'Count': frequency_table['Count'].sum(),
    'Relative Frequency': 1.00,
    'Percentage': 100,
    'Cumulative Frequency': frequency_table['Count'].sum(),
    'Cumulative Rel Freq': 1.00
}

# Fix integer columns
frequency_table['Cumulative Frequency'] = frequency_table['Cumulative Frequency'].astype(int)
```

---

## 🔑 Key Pandas Methods

### `value_counts()` — Count Frequencies

```python
# Works on ANY data type
df['Fruits'].value_counts()     # Text/categorical ✅
df['Scores'].value_counts()     # Numbers ✅
df['Column'].value_counts()     # DataFrame column ✅
```

### `.map()` — Add Counts to Original DataFrame

```python
# Problem: Can't assign value_counts() directly (index mismatch)
df['Count'] = df['Fruits'].value_counts()  # ❌ Returns NaN!

# Solution: Use .map()
counts = df['Fruits'].value_counts()
df['Count'] = df['Fruits'].map(counts)     # ✅ Works!
```

### `.cumsum()` — Cumulative Sum

```python
df['Cumulative'] = df['Count'].cumsum()
```

### `.round()` — Round Numbers

```python
df['Value'].round(2)  # Round to 2 decimal places
```

### Adding Percentage Symbol

```python
# Option 1: String concatenation
df['Pct'] = df['Value'].round(1).astype(str) + '%'

# Option 2: Using apply with f-string
df['Pct'] = df['Value'].apply(lambda x: f'{x:.2f}%')
```

### Adding a New Row

```python
df.loc[len(df)] = {'Col1': 'Total', 'Col2': 100, 'Col3': '100%'}
```

---

## 📊 Static Visualization: Matplotlib

### Bar Chart vs Histogram — When to Use Which?

| Feature | Bar Chart | Histogram |
|---------|-----------|-----------|
| **Used for** | Categorical data | Quantitative data |
| **Bars** | Have gaps between them | Touch each other |
| **X-axis** | Category names | Number ranges (bins) |
| **Examples** | Fruits, Colors, Countries | Scores, Heights, Ages |

**Key Rule:** Can you do math on it?
- YES (numbers) → **Histogram**
- NO (categories) → **Bar Chart**

### Bar Chart (Categorical Data)

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(frequency_table['Fruits'], frequency_table['Count'],
        color='steelblue', edgecolor='black')

# Add value labels on bars
for i, count in enumerate(frequency_table['Count']):
    plt.text(i, count + 0.3, str(count), ha='center', fontweight='bold')

plt.xlabel('Fruit Type')
plt.ylabel('Frequency')
plt.title('Bar Chart: Fruit Distribution')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Histogram (Quantitative Data)

```python
scores = [72, 85, 91, 68, 75, 82, 88, 79, 94, 71, 83, 77, 86, 69, 90, 81]

plt.figure(figsize=(10, 6))
plt.hist(scores, bins=[60, 70, 80, 90, 100], edgecolor='black', color='steelblue', alpha=0.7)
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.title('Distribution of Test Scores')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## 🚀 Interactive Visualization: Plotly

### Why Plotly?

| Feature | Matplotlib | Plotly |
|---------|------------|--------|
| Interactivity | ❌ Static | ✅ Hover, zoom, pan |
| Output | PNG/PDF | HTML (browser) |
| Hover info | ❌ No | ✅ Yes |

### Bar Chart (Categorical Data)

```python
import plotly.express as px

fig = px.bar(
    frequency_table,
    x='Fruits',
    y='Count',
    color='Fruits',
    title='Fruit Distribution',
    text='Count',
    hover_data=['Percentage']
)
fig.update_traces(textposition='outside')  # Labels above bars
fig.show()
```

### Histogram (Quantitative Data) — Plotly

```python
import plotly.express as px
import pandas as pd

data = [45, 52, 67, 71, 73, 75, 78, 79, 80, 81,
        82, 83, 85, 86, 88, 89, 91, 93, 95, 98]

df = pd.DataFrame({'Scores': data})

# Let histogram create bins from raw data
fig = px.histogram(
    df, 
    x='Scores',
    nbins=6,                      # Number of bins
    title='Distribution of Scores',
    text_auto=True                # Show counts on bars
)

fig.update_traces(
    marker_line_color='black',
    marker_line_width=1
)

# No bargap! Histogram bars should touch
fig.show()
```

### Custom Bin Edges in Plotly

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Histogram(
    x=data,
    xbins=dict(start=40, end=100, size=10),  # Custom bins
    marker_line_color='black',
    marker_line_width=1
)])
fig.show()
```

### ⚠️ px.histogram vs px.bar

| If you have... | Use... |
|----------------|--------|
| Raw data: `[45, 52, 67, ...]` | `px.histogram(df, x='Scores')` |
| Pre-computed frequency table | `px.bar(frequency_table, x='Range', y='Frequency')` |

---

## 📏 Calculating Bin Width

### Formula

```
Bin Width = (Max - Min) / Number of Bins
         = Range / Number of Bins
```

### Rules of Thumb for Number of Bins

| Rule | Formula |
|------|---------|
| Square Root | `√n` (n = data points) |
| Sturges' | `1 + 3.322 × log₁₀(n)` |

| Data Points | Suggested Bins |
|-------------|----------------|
| 10-25 | 4-6 |
| 25-50 | 5-8 |
| 50-100 | 6-10 |

---

## 🔪 pd.cut() — Binning Data

### Syntax

```python
pd.cut(x, bins, labels=None, right=True)
```

### Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `x` | Data to bin | `df['Scores']` |
| `bins` | Bin edges | `[40, 50, 60, 70, 80, 90, 100]` |
| `labels` | Bin names | `['40-49', '50-59', ...]` |
| `right` | Include right edge? | `True`=(40,50], `False`=[40,50) |

### Complete Example

```python
import pandas as pd

data = [45, 52, 67, 71, 73, 75, 78, 79, 80, 81,
        82, 83, 85, 86, 88, 89, 91, 93, 95, 98]

df = pd.DataFrame({'Scores': data})

bins = [40, 50, 60, 70, 80, 90, 100]
labels = ['40-49', '50-59', '60-69', '70-79', '80-89', '90-99']

df['Range'] = pd.cut(df['Scores'], bins=bins, labels=labels, right=False)

frequency_table = df['Range'].value_counts().sort_index().reset_index(name='Frequency')
frequency_table['Relative Frequency'] = frequency_table['Frequency'] / frequency_table['Frequency'].sum()
frequency_table['Percentage'] = frequency_table['Relative Frequency'] * 100
frequency_table['Cumulative Frequency'] = frequency_table['Frequency'].cumsum()
```

---

## 🗂️ Practice Code Files

- [chapter3_visualization.py](./code/chapter3_visualization.py) — Static charts
- [interactive_visualization.py](./code/interactive_visualization.py) — Plotly charts
- [frequency_table_step_by_step.py](./code/frequency_table_step_by_step.py) — pd.cut() example
- [bar_charts.py](./code/bar_charts.py) — Bar chart examples

---

## 📌 Common Mistakes

1. **Assigning value_counts() directly** → Use `.map()` instead
2. **Multiplying strings** → Do math first, format last
3. **Mixed types in columns** → Keep numbers for calculations, strings for display
4. **Float instead of int** → Use `.astype(int)` after adding rows
5. **Using px.histogram on frequency table** → Use `px.bar` for pre-computed data
6. **Adding bargap to histogram** → Histogram bars should touch (bargap=0)
