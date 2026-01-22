# 📊 Chapter 9: Frequency Tables

---

## 🎯 What is a Frequency Table?

A **frequency table** counts how many times each category appears in your data.

---

## Types of Frequencies

| Type                     | What It Measures     | Example            |
| ------------------------ | -------------------- | ------------------ |
| **Absolute Frequency**   | Raw count            | Alice got 5 votes  |
| **Relative Frequency**   | Proportion (decimal) | 0.50 of votes      |
| **Percentage**           | Proportion × 100     | 50% of votes       |
| **Cumulative Frequency** | Running total        | Up to Bob: 8 total |

---

## 💻 Python: Creating Frequency Tables

### Basic Frequency Count

```python
import pandas as pd

majors = ['CS', 'Business', 'CS', 'Arts', 'CS', 'Business']
data = pd.Series(majors)

# Absolute Frequency
freq = data.value_counts()
print(freq)

# Relative Frequency (proportions)
rel_freq = data.value_counts(normalize=True)
print(rel_freq)
```

### Complete Frequency Table

```python
import pandas as pd

data = pd.Series(['CS', 'Business', 'CS', 'Arts', 'CS', 'Business'])

# Create complete table
freq_table = pd.DataFrame({
    'Frequency': data.value_counts(),
    'Proportion': data.value_counts(normalize=True),
    'Percentage': data.value_counts(normalize=True) * 100
})

# Add cumulative columns
freq_table['Cumulative Freq'] = freq_table['Frequency'].cumsum()
freq_table['Cumulative %'] = freq_table['Percentage'].cumsum()

print(freq_table)
```

**Output**:

```
          Frequency  Proportion  Percentage  Cumulative Freq  Cumulative %
CS                3        0.50        50.0                3          50.0
Business          2        0.33        33.3                5          83.3
Arts              1        0.17        16.7                6         100.0
```

---

## Column Purposes

| Column         | Purpose          | Example                    |
| -------------- | ---------------- | -------------------------- |
| **Frequency**  | Raw count        | "3 chose CS"               |
| **Proportion** | For calculations | 0.50                       |
| **Percentage** | Easy to read     | "50%"                      |
| **Cumulative** | Running total    | "83% chose CS or Business" |

---

## 📊 Visualizing with Bar Chart

```python
import matplotlib.pyplot as plt

freq = data.value_counts()
freq.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Frequency Distribution')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## 📋 Summary Card

```
┌─────────────────────────────────────────────────────────┐
│                   FREQUENCY TABLE                       │
├─────────────────────────────────────────────────────────┤
│  PURPOSE: Count occurrences of each category            │
│                                                         │
│  KEY FUNCTION: data.value_counts()                      │
│  WITH PROPORTIONS: data.value_counts(normalize=True)    │
│                                                         │
│  COLUMNS:                                               │
│    • Frequency    → Raw count                           │
│    • Proportion   → Decimal (0-1)                       │
│    • Percentage   → Easy to read                        │
│    • Cumulative   → Running total                       │
└─────────────────────────────────────────────────────────┘
```

---

## 🔗 Related Topics

- [07_Binary_and_Categorical_Data.md](07_Binary_and_Categorical_Data.md) - Mode basics
- [08_Pie_Charts_Donut_Charts.md](08_Pie_Charts_Donut_Charts.md) - Visualizations
