# 📊 Chapter 1.5: Types of Variables

Before we explore how data is distributed, we need to know: **What KIND of data are we dealing with?**

---

## 🌳 The Big Picture: Two Main Types

```
                    VARIABLES
                        │
          ┌─────────────┴─────────────┐
          │                           │
    CATEGORICAL                 QUANTITATIVE
    (Qualitative)                (Numerical)
          │                           │
    ┌─────┴─────┐             ┌───────┴───────┐
    │           │             │               │
  Nominal    Ordinal      Discrete      Continuous
```

---

## 1️⃣ Categorical Variables (Qualitative)

### 🎯 Simple Definition

> **Categorical variables** describe **qualities or categories** — things you can NAME but not meaningfully measure with numbers.

### Examples

| Variable | Possible Values |
|----------|-----------------|
| Eye color | Brown, Blue, Green, Hazel |
| Blood type | A, B, AB, O |
| Country | USA, India, Japan, Brazil |
| Marital status | Single, Married, Divorced |

### Key Insight

You can **count** how many fall into each category, but you **cannot calculate an average**.

❌ *"The average blood type is B.5"* — Makes no sense!

---

### Two Subtypes of Categorical:

#### a) **Nominal** (No natural order)

> Categories have **no meaningful order**.

| Variable | Values | Can you rank them? |
|----------|--------|-------------------|
| Eye color | Brown, Blue, Green | ❌ No |
| Blood type | A, B, AB, O | ❌ No |
| Favorite fruit | Apple, Banana, Orange | ❌ No |

#### b) **Ordinal** (Has natural order)

> Categories have a **meaningful order**, but the distance between them isn't measurable.

| Variable | Values | Ordered? |
|----------|--------|----------|
| Education level | High School < Bachelor's < Master's < PhD | ✅ Yes |
| Survey rating | Poor < Fair < Good < Excellent | ✅ Yes |
| T-shirt size | S < M < L < XL | ✅ Yes |

**Important:** We know Master's > Bachelor's, but we can't say "how much more."

---

## 2️⃣ Quantitative Variables (Numerical)

### 🎯 Simple Definition

> **Quantitative variables** are **measured with numbers** — you can perform mathematical operations on them.

### Examples

| Variable | Example Values |
|----------|----------------|
| Height | 165 cm, 178 cm, 152 cm |
| Temperature | 72°F, 85°F, 68°F |
| Income | $45,000, $72,000, $58,000 |
| Age | 25, 42, 18, 67 |

### Key Insight

You **CAN** calculate averages, sums, and differences.

✅ *"The average height is 168 cm"* — Makes perfect sense!

---

### Two Subtypes of Quantitative:

#### a) **Discrete** (Countable, gaps between values)

> Values are **countable** — often whole numbers.

| Variable | Example Values | Why discrete? |
|----------|----------------|---------------|
| Number of children | 0, 1, 2, 3... | Can't have 2.5 children |
| Number of cars | 0, 1, 2, 3... | Can't own 1.7 cars |
| Shoes owned | 3, 5, 12, 20... | Always whole numbers |

**Trick:** Usually answers "How many?"

#### b) **Continuous** (Can take ANY value in a range)

> Values can be **any number** within a range — including decimals.

| Variable | Example Values | Why continuous? |
|----------|----------------|-----------------|
| Height | 165.3 cm, 178.92 cm | Any value possible |
| Weight | 68.5 kg, 72.125 kg | Any value possible |
| Time | 3.7 seconds, 10.456 min | Any value possible |

**Trick:** Usually answers "How much?" or "How long?"

---

## 🧠 Quick Decision Flowchart

```
Is it a NUMBER you can do math with?
    │
    ├── NO → CATEGORICAL
    │           │
    │           └── Is there a natural ORDER?
    │                   ├── NO → Nominal
    │                   └── YES → Ordinal
    │
    └── YES → QUANTITATIVE
                │
                └── Can it take ANY value (including decimals)?
                        ├── NO → Discrete
                        └── YES → Continuous
```

---

## 🚨 Common Mistake: Numbers ≠ Quantitative!

**Zip codes: 10001, 90210, 60614**
- These are NUMBERS...
- But can you calculate the "average zip code"? ❌ NO!
- They're just **labels** → **Categorical (Nominal)**

**Phone numbers, jersey numbers, student IDs** — all categorical!

> **Rule:** If arithmetic (add, subtract, average) doesn't make sense, it's categorical!

---

## 📋 Summary Table

| Type | Subtype | Order? | Math? | Examples |
|------|---------|--------|-------|----------|
| Categorical | Nominal | ❌ | ❌ | Blood type, Eye color |
| Categorical | Ordinal | ✅ | ❌ | Education level, Ratings |
| Quantitative | Discrete | ✅ | ✅ | # of children, # of cars |
| Quantitative | Continuous | ✅ | ✅ | Height, Weight, Time |

---

## ✅ Practice Problems

Classify each variable (Categorical/Quantitative + Subtype):

1. **Temperature in Celsius** → ?
2. **Movie rating (⭐ out of 5)** → ?
3. **Number of pets owned** → ?
4. **Nationality** → ?
5. **Area code (212, 310, 415)** → ?

### Answers:

1. Temperature → **Quantitative, Continuous**
2. Movie rating → **Categorical, Ordinal** (ordered categories)
3. Number of pets → **Quantitative, Discrete** (whole numbers)
4. Nationality → **Categorical, Nominal** (no order)
5. Area code → **Categorical, Nominal** (numbers used as labels!)
