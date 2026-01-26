# Chapter 5: Correlation with Real-World Datasets

## 📦 Why Real-World Data?
- Real datasets are larger, messier, and more complex than textbook examples.
- We use libraries like **Pandas** and **NumPy** to handle, explore, and analyze them efficiently.

---

## 🐼 Using Pandas for Correlation

### 1. Load Data
- From a CSV: `df = pd.read_csv('data.csv')`
- From a dictionary (for practice):
```python
data = {
    'hours_studied': [2, 4, 6, 8, 10, 12, 14, 16],
    'exam_score':    [55, 60, 65, 70, 75, 80, 85, 90],
    'sleep_hours':   [7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5],
    'coffee_cups':   [1, 1, 2, 2, 3, 3, 4, 4]
}
df = pd.DataFrame(data)
```

### 2. Explore Data
- `df.head()` — see the first few rows
- `df.info()` — check data types and missing values

### 3. Calculate Correlation Matrix
```python
corr_matrix = df.corr()
print(corr_matrix)
```
- Shows correlation between **all pairs** of numeric columns
- Values range from -1 (perfect negative) to +1 (perfect positive)

### 4. Interpret Results
- **Strongest positive correlation:** Highest value close to +1
- **Strongest negative correlation:** Lowest value close to -1
- **Zero correlation:** Value near 0

---

## 📝 Example Output
|                | hours_studied | exam_score | sleep_hours | coffee_cups |
|----------------|--------------|------------|-------------|-------------|
| hours_studied  | 1.00         | 1.00       | -1.00       | 1.00        |
| exam_score     | 1.00         | 1.00       | -1.00       | 1.00        |
| sleep_hours    | -1.00        | -1.00      | 1.00        | -1.00       |
| coffee_cups    | 1.00         | 1.00       | -1.00       | 1.00        |

---

## 🔑 Key Takeaways
- **Pandas** makes it easy to analyze real datasets
- Use `.corr()` for a quick overview of all relationships
- Always explore and visualize before interpreting results
- Real-world data may have missing values, outliers, or non-linear relationships

---

## 📝 Practice
1. Load a real CSV file with `pd.read_csv()`
2. Use `df.corr()` to find the strongest and weakest correlations
3. Visualize with `pd.plotting.scatter_matrix(df)` or `sns.heatmap(df.corr())`

---

*Next: Advanced topics — r², correlation vs causation, and limitations of correlation analysis.*
