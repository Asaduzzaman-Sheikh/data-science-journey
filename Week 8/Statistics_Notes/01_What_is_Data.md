# 📊 Chapter 1: What is Data?

---

## 🌱 The Intuition

Imagine you're a teacher who just gave a test to 30 students. After grading, you have 30 numbers (scores):

```
72, 85, 91, 68, 75, 82, 88, 79, 94, 71, 
83, 77, 86, 69, 90, 81, 74, 87, 93, 76, 
80, 84, 78, 89, 70, 92, 73, 85, 81, 88
```

**These numbers are DATA.**

Data is simply **a collection of observations, measurements, or facts** that we gather about something we're interested in.

---

## 🎯 Why Do We Need Data?

- A doctor measures your blood pressure to understand your health
- A business tracks sales to understand customer behavior
- A weather station records temperature to predict tomorrow's weather

**Data helps us make sense of the world around us.**

But raw data is messy and hard to understand — that's why we need to explore the data distribution!

---

## 📝 Formal Definition

> **Data** is a collection of facts, measurements, or observations that can be analyzed to gain insights or make decisions.

- **Data point / Observation**: One single measurement (e.g., score of 85)
- **Dataset**: All measurements together (e.g., all 30 scores)
- **Variable**: What we're measuring (e.g., test scores)

---

## 🔑 Key Vocabulary

| Term | Simple Meaning | Example |
|------|----------------|---------|
| **Data point** | One single measurement | Score of 85 |
| **Dataset** | All measurements together | All 30 scores |
| **Variable** | What we're measuring | Test scores |

---

## 🚨 Common Misconception: What Does "Variable" Mean?

### ❌ The Misconception
> *"A variable is something that changes over time."*

### ✅ The Correct Understanding
> **A variable changes ACROSS OBSERVATIONS (different people, things, or cases) — NOT necessarily over time.**

### Example: Student Heights

| Student | Height (cm) |
|---------|-------------|
| Alice | 160 |
| Bob | 175 |
| Carol | 168 |
| David | 182 |
| Emma | 155 |

- All measured at the **same moment** (10:00 AM)
- Time didn't change at all!
- Height **varies across students** — that's why it's a variable

### The Core Idea

Think of data as a table:

| Observation | Variable 1 | Variable 2 |
|-------------|------------|------------|
| Person 1 | value | value |
| Person 2 | value | value |
| Person 3 | value | value |

- **Rows** = Observations (the "who" or "what" we measured)
- **Columns** = Variables (the "what we measured")
- Variables vary **down the column** (across rows)

---

## ✅ Practice Questions

1. If a hospital records the height of 100 patients:
   - What is the variable? → **Height**
   - What would ONE data point look like? → **One patient's height (e.g., 170 cm)**
   - What would the dataset be? → **All 100 heights together**

2. A researcher records blood type (A, B, AB, O) of 50 patients at 9:00 AM:
   - Is "blood type" a variable? → **Yes!** It varies across patients
   - Does this involve time changing? → **No!** All measured at same time
