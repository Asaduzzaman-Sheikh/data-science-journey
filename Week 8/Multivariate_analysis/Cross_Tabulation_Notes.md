# Cross-Tabulation (Crosstab) - Complete Guide

> **From Basics to Expert-Level Application**

---

## 1. What is a Crosstab?

A **Crosstab** (short for Cross-tabulation) is a statistical tool used to analyze the **relationship between two or more categorical variables**.

### Key Insight

- A **standard frequency table** tells you **how many** → _"We sold 100 shirts"_
- A **crosstab** tells you the **intersection** → _"We sold 20 red shirts to men and 80 blue shirts to women"_

> **💡 The "Aha!" Moment:** A crosstab transforms raw data into a matrix that reveals patterns, trends, and probabilities that are otherwise invisible in a simple list.

---

## 2. Anatomy of a Crosstab

| Component            | Description                                         | Example            |
| -------------------- | --------------------------------------------------- | ------------------ |
| **Row Variable**     | Category listed down the left side                  | Gender             |
| **Column Variable**  | Category listed across the top                      | Product Preference |
| **Cells**            | Intersection points containing counts (frequencies) | 20, 80, etc.       |
| **Margins (Totals)** | Row totals and column totals                        | Sum of frequencies |

---

## 3. Concrete Example: Coffee vs. Time of Day

**Scenario:** You run a cafe and want to know if time of day affects coffee size preference.  
**Data:** 200 customers

### Raw Crosstab

|           | Small | Large | **Total** |
| --------- | :---: | :---: | :-------: |
| Morning   |  20   |  80   |    100    |
| Afternoon |  70   |  30   |    100    |
| **Total** |  90   |  110  |    200    |

### Analysis

- **Morning:** Large coffees dominate (80 vs 20)
- **Afternoon:** Trend flips completely (30 Large vs 70 Small)
- **Marginal Totals:** 110 Large total > 90 Small total

---

## 4. The "Deep Knowledge": Percentages

> ⚠️ **Novices look at counts; Experts look at percentages.**

There are **three specific ways** to calculate percentages. Choosing the wrong one yields the **wrong insight**.

---

### A. Row Percentage (The "Who" Focus)

$$\text{Row \%} = \frac{\text{Cell Count}}{\text{Row Total}} \times 100$$

**Example:**

- Morning Large: $\frac{80}{100} = 80\%$

**Insight:**

> _"If a customer comes in the morning, there is an **80% chance** they want a Large."_

---

### B. Column Percentage (The "Product" Focus)

$$\text{Column \%} = \frac{\text{Cell Count}}{\text{Column Total}} \times 100$$

**Example:**

- Large Coffee sold in Morning: $\frac{80}{110} \approx 72.7\%$

**Insight:**

> _"If looking at all Large coffees sold today, **73% of them** were sold in the morning."_

---

### C. Total Percentage (The "Big Picture")

$$\text{Total \%} = \frac{\text{Cell Count}}{\text{Grand Total}} \times 100$$

**Example:**

- Morning Large: $\frac{80}{200} = 40\%$

**Insight:**

> _"**40% of all transactions** today were Morning Large coffees."_

---

### Quick Reference: Which Percentage to Use?

| Question Type                               | Use This % | Focus               |
| ------------------------------------------- | ---------- | ------------------- |
| "Given X, what's the probability of Y?"     | Row %      | Customer behavior   |
| "Of all Y, how much came from X?"           | Column %   | Product analysis    |
| "What portion of total does X+Y represent?" | Total %    | Overall composition |

---

## 5. Advanced Statistics: Chi-Square Test (χ²)

A crosstab shows you a **pattern**, but doesn't tell you if it's **statistically significant** or just a coincidence.

### Chi-Square Test of Independence

**Purpose:** Compare **Observed data** (actual crosstab) against **Expected data** (mathematical probability if no relationship existed)

### Formula

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Where:

- $O_i$ = **Observed frequency** (actual numbers in your crosstab)
- $E_i$ = **Expected frequency** (what numbers would be if no relationship existed)

### Interpretation

- If χ² value is **high enough** (crosses critical value threshold) → Variables **ARE related**
- If χ² value is **low** → Relationship may be due to **chance**

---

## 6. Summary Checklist

### ✅ When to Use Crosstab

- You have **two categorical variables**
  - Examples: Yes/No, Red/Blue, Low/Medium/High, Male/Female

### ❌ When NOT to Use Crosstab

- You have **continuous numerical data** (e.g., Height vs. Weight)
- **Exception:** You can group continuous data into buckets (e.g., 0-10, 11-20)

### 🔑 The Golden Rule

> **Always check Row % vs. Column %** to ensure you are answering the **right business question**.

---

## Visual Summary

```
┌─────────────────────────────────────────────────────────┐
│                    CROSSTAB STRUCTURE                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│              │  Column Var A  │  Column Var B  │ TOTAL  │
│  ────────────┼────────────────┼────────────────┼──────  │
│  Row Var 1   │     Cell 1     │     Cell 2     │  Row   │
│              │   (Count/%)    │   (Count/%)    │ Total  │
│  ────────────┼────────────────┼────────────────┼──────  │
│  Row Var 2   │     Cell 3     │     Cell 4     │  Row   │
│              │   (Count/%)    │   (Count/%)    │ Total  │
│  ────────────┼────────────────┼────────────────┼──────  │
│    TOTAL     │  Column Total  │  Column Total  │ Grand  │
│              │                │                │ Total  │
└─────────────────────────────────────────────────────────┘
```

---

## Next Steps

1. **Practice:** Create crosstabs with real datasets
2. **Calculate:** Expected frequencies for Chi-Square test
3. **Interpret:** Always ask "What business question am I answering?"
4. **Visualize:** Use heatmaps to represent crosstab patterns

---

_Notes created: January 27, 2026_  
_Topic: Multivariate Analysis - Week 8_
