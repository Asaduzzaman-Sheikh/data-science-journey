# Bootstrap Method -- Complete Notes

---

## What is Bootstrap?

Bootstrap is a **resampling technique** that lets you estimate the uncertainty of a statistic using only the data you already have.

**The core problem it solves:** You have one sample. You cannot go collect more data. How do you know if your estimate (mean, median, etc.) is reliable?

**The solution:** Treat your sample as if it were the population. Resample from it repeatedly **with replacement** to simulate taking many new samples.

---

## Why It's Called "Bootstrap"

The name comes from the phrase "pulling yourself up by your own bootstraps" -- doing something seemingly impossible using only what you already have.

In statistics: estimating what many samples would look like, using only one sample.

---

## The Algorithm -- Step by Step

```
Step 1:  You have ONE original sample of size n
         Example: [12, 8, 22, 5, 31, 14, 9, 7, 19, 11] (n = 10)

Step 2:  Draw n values FROM this sample WITH REPLACEMENT
         Resample 1: [12, 5, 5, 22, 12, 31, 8, 8, 19, 12]
         (notice: 12 appears 3 times, some values missing)

Step 3:  Calculate your statistic (e.g., mean) on this resample
         Mean of Resample 1 = 15.4

Step 4:  Repeat Steps 2-3 many times (typically 1,000 to 10,000)
         Resample 2 mean = 13.8
         Resample 3 mean = 16.1
         ...
         Resample 1000 mean = 14.2

Step 5:  You now have 1,000 bootstrap statistics
         Analyze their distribution -- this approximates the
         sampling distribution of your statistic
```

---

## The Key Idea: Resampling WITH Replacement

### Why "with replacement"?

If you draw n values from n values **without** replacement, you just get the same n values in a different order. The mean would always be the same. Nothing new is learned.

**With replacement**, each draw is independent. Some values get picked multiple times, others get skipped entirely. This creates natural variation between resamples.

### Example

Original sample: `[5, 12, 8, 3, 20]`

```
Resample 1: [12, 5, 5, 20, 12]    -- 5 and 12 repeated; 8 and 3 missing
Resample 2: [3, 8, 20, 20, 5]     -- 20 repeated
Resample 3: [8, 8, 8, 12, 3]      -- 8 appears three times
```

Each resample tells a slightly different story. The spread of their means tells you how uncertain your estimate is.

---

## Bootstrap vs CLT Simulation -- The Critical Difference

This is the most common confusion. Both use `replace=True`. The difference is **where you resample from**.

```
CLT Simulation:
   Population (10,000 values)  -->  draw samples of 50
   You HAVE the full population (educational exercise)

Bootstrap:
   Sample (30 values)  -->  draw resamples of 30
   You DON'T have the population (real-world scenario)
```

| | CLT Simulation | Bootstrap |
|---|---|---|
| **Resample from** | The population | The sample |
| **You have access to** | Full population | Only one sample |
| **Purpose** | Prove a theorem (educational) | Solve a real problem (practical) |
| **When to use** | Teaching/simulation | Real data analysis |

---

## What Bootstrap Gives You

### 1. Bootstrap Standard Error

The standard deviation of the bootstrap statistics = the **standard error** of your estimate.

```
1,000 bootstrap means --> np.std(bootstrap_means, ddof=1) = Standard Error
```

This tells you: "If I could take many real samples, how much would the mean vary?"

### 2. Bootstrap Confidence Interval (Percentile Method)

No formula needed. Just use percentiles:

```
95% CI:
   Lower = 2.5th percentile of bootstrap statistics
   Upper = 97.5th percentile of bootstrap statistics

90% CI:
   Lower = 5th percentile
   Upper = 95th percentile
```

In Python:
```python
lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)
```

### 3. Bootstrap Distribution

The histogram of your 1,000 bootstrap statistics approximates the **sampling distribution** -- the same thing the CLT describes theoretically.

---

## Bootstrap vs Classical (z-score) Confidence Interval

| | Classical CI | Bootstrap CI |
|---|---|---|
| Assumes normality? | Yes (or relies on CLT) | No |
| Needs formula? | Yes (`z * std / sqrt(n)`) | No, just percentiles |
| Works for any statistic? | Only mean (easily) | Mean, median, variance, anything |
| Needs population std? | Estimates it | No |
| Requires large sample? | Yes (for CLT to kick in) | Works with moderate samples |

---

## When to Use Bootstrap

### Use Bootstrap when:

1. **Your statistic is not the mean** -- median, correlation, ratio, regression coefficient, etc.
   - There's no simple formula for the SE of a median. Bootstrap handles it.

2. **Distribution is weird** -- skewed, bimodal, heavy-tailed
   - Classical CI assumes normality. Bootstrap doesn't.

3. **Sample size is small** -- n < 30
   - CLT may not apply yet. Bootstrap is safer.

4. **You want a formula-free CI**
   - No z-scores, no t-tables. Just percentiles.

### Don't bother with Bootstrap when:

1. You have the full population (just compute the exact answer)
2. You want the mean's CI with a large sample (classical CI works fine and is simpler)

---

## Why Bootstrap Works

Your sample is the **best available approximation** of the population. If the sample is representative, then resampling from it mimics what would happen if you resampled from the population.

**Conditions for it to work well:**
- Sample is reasonably large (n >= 20-30)
- Sample is representative of the population (no severe bias)
- The statistic is "smooth" (small changes in data = small changes in statistic)

**When it can fail:**
- Very small samples (n < 10) -- not enough data to represent the population
- Heavy outlier influence -- one extreme value dominates
- The statistic is unstable (e.g., the maximum of the sample)

---

## Types of Bootstrap

### 1. Non-parametric Bootstrap (Standard)

Resample directly from the data. No assumptions about the distribution.

This is what we've been discussing and is the most common type.

### 2. Parametric Bootstrap

Assume the data follows a specific distribution (e.g., normal), estimate its parameters from the sample, then generate resamples from that fitted distribution.

```
Example:
   Sample mean = 15, Sample std = 4
   Assume population is Normal(15, 4)
   Generate resamples from Normal(15, 4)
```

Use this when you're confident about the distribution shape.

---

## How Many Bootstrap Resamples?

| Number of Resamples | Use Case |
|---|---|
| 1,000 | Standard error estimation (usually enough) |
| 5,000 - 10,000 | Confidence intervals (more precision in the tails) |
| 10,000+ | Publication-quality results |

More resamples = more stable results, but diminishing returns after ~10,000.

---

## The ddof Question in Bootstrap

| What you compute std of | ddof | Reason |
|---|---|---|
| One bootstrap resample (to estimate population spread) | `ddof=1` | It's a sample estimating something bigger |
| The 1,000 bootstrap means (to get SE) | `ddof=1` | They're a sample of all possible bootstrap means |
| Your full original population (if you have it) | `ddof=0` | You have everything |

**Practical note:** With 1,000+ values, the difference between ddof=0 and ddof=1 is negligible.

---

## Bootstrap Confidence Interval Methods

There are several ways to build a CI from bootstrap results. The three most common:

### 1. Percentile Method (Simplest)

```
95% CI = [2.5th percentile, 97.5th percentile]
```

Pros: Simple, intuitive
Cons: Can be biased if the bootstrap distribution is skewed

### 2. Basic (Reverse Percentile) Method

```
95% CI = [2 * original_stat - 97.5th percentile,
          2 * original_stat - 2.5th percentile]
```

Adjusts for bias in the bootstrap distribution.

### 3. BCa (Bias-Corrected and Accelerated)

The most sophisticated. Corrects for both bias and skewness. Used in `scipy.stats.bootstrap`.

**For most practical purposes, the percentile method is sufficient.**

---

## Common Mistakes

1. **Resampling from the population instead of the sample** -- That's simulation, not bootstrap.

2. **Resampling without replacement** -- You just get the same data shuffled. No new information.

3. **Using too few resamples** -- 100 is not enough. Use at least 1,000.

4. **Applying bootstrap to tiny samples (n < 10)** -- The sample doesn't represent the population well enough.

5. **Forgetting that bootstrap has limits** -- It cannot fix a biased sample. If your original sample is biased, bootstrap resamples will also be biased.

---

## Summary Table

| Concept | Description |
|---|---|
| **Bootstrap resample** | n values drawn with replacement from the original sample |
| **Bootstrap statistic** | The statistic computed on one resample |
| **Bootstrap distribution** | The distribution of all bootstrap statistics |
| **Bootstrap standard error** | `std(bootstrap_statistics)` |
| **Bootstrap CI (percentile)** | `[2.5th percentile, 97.5th percentile]` for 95% |
| **Number of resamples** | Typically 1,000 to 10,000 |
| **Key requirement** | Resample WITH replacement FROM the sample |

---

## One-Liners to Remember

1. **What it does:** "Estimates uncertainty using only the data you have"
2. **How it works:** "Resample with replacement from your sample, many times"
3. **Why it works:** "Your sample is the best approximation of the population"
4. **When to use it:** "When formulas don't exist or assumptions don't hold"
5. **The tradeoff:** "It's flexible and assumption-free, but needs a decent sample size"
6. **vs Classical CI:** "Classical = formula + assumptions; Bootstrap = resampling + no assumptions"

---

*Notes created: February 11, 2026*
*Topic: Bootstrap Method*
*Week 8 - Data Science Journey*
