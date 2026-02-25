# 📘 Binomial Distribution

---

## 1. What Is Binomial? — "The Two-Outcome World"

**Binomial** = **Bi** (two) + **nomial** (outcomes). Every trial has exactly **two** possibilities.

| Trial          | Success ✅ | Failure ❌  |
| -------------- | ---------- | ----------- |
| Free throw     | Make it    | Miss it     |
| Coin flip      | Heads      | Tails       |
| Customer visit | Buys       | Doesn't buy |
| Email sent     | Opened     | Not opened  |
| Medical test   | Positive   | Negative    |

---

## 2. The 4 Rules — "The Binomial Checklist"

For a situation to be Binomial, ALL four must be true:

| Rule                        | Meaning                                 | Example                        |
| --------------------------- | --------------------------------------- | ------------------------------ |
| 1. **Fixed trials (n)**     | You know how many attempts in advance   | 10 free throws                 |
| 2. **Two outcomes only**    | Each trial is success ✅ or failure ❌  | Make or miss                   |
| 3. **Same probability (p)** | Success rate stays constant every trial | Always 70%                     |
| 4. **Independent trials**   | One trial doesn't affect the next       | Shot #3 doesn't change shot #4 |

### ⚠️ Common Trap: Drawing Cards

Drawing 5 cards from a deck and counting aces is **NOT** Binomial — removing a card changes the probability of the next draw (violates Rules 3 & 4). That's called **Hypergeometric**.

---

## 3. The Formula — "Three Pieces of a Pizza" 🍕

**P(X = k) = C(n, k) × p^k × (1 − p)^(n − k)**

| Piece           | What It Means                                        | Basketball Example (n=10, p=0.7, k=8) |
| --------------- | ---------------------------------------------------- | ------------------------------------- |
| **C(n, k)**     | How many **ways** to arrange k successes in n trials | C(10,8) = 45 ways                     |
| **p^k**         | Probability of k **successes** happening             | 0.7⁸ = 0.057                          |
| **(1−p)^(n−k)** | Probability of the remaining **failures**            | 0.3² = 0.09                           |

**Result:** 45 × 0.057 × 0.09 = **0.2335 (23.3%)**

---

## 4. Combination vs. Permutation

|                       | Permutation                     | Combination          |
| --------------------- | ------------------------------- | -------------------- |
| **Order matters?**    | ✅ Yes                          | ❌ No                |
| **Formula**           | n! / (n−k)!                     | n! / (k! × (n−k)!)   |
| **Example**           | Ranking 1st, 2nd, 3rd in a race | Choosing a team of 3 |
| **Used in Binomial?** | ❌                              | ✅                   |

> Binomial uses **Combination** because we only care WHICH shots she made, not the ORDER she made them in. {1,3,5} = {5,1,3} — same 3 makes.

> **Combination = Permutation ÷ k!** (divides out the duplicate orderings)

---

## 5. PMF vs. PDF vs. CDF — "The Function Family"

| Function | Stands For                       | Data Type      | What It Answers                       |
| -------- | -------------------------------- | -------------- | ------------------------------------- |
| **PMF**  | Probability Mass Function        | **Discrete**   | P(X = k) — "exactly this?"            |
| **PDF**  | Probability Density Function     | **Continuous** | Density at a point (not probability!) |
| **CDF**  | Cumulative Distribution Function | **Both**       | P(X ≤ k) — "this or less?"            |

### The 1 − CDF Trick

> **P(X ≥ k) = 1 − CDF(k − 1)**

| Formula        | What It Gives                |
| -------------- | ---------------------------- |
| 1 − CDF(**5**) | P(X ≥ **6**) — includes 6 ✅ |
| 1 − CDF(**6**) | P(X ≥ **7**) — excludes 6 ❌ |

> **Why k−1?** Because CDF gives "k or LESS." To include k in the "or more" side, you must CDF up to k−1.

---

## 6. Expected Value — "The Center"

> **E(X) = n × p**

The expected number of successes. This is where the Binomial distribution is "centered."

| Example                               | n   | p     | Expected         |
| ------------------------------------- | --- | ----- | ---------------- |
| 10 shots, 70% shooter                 | 10  | 0.7   | **7 makes**      |
| 20 visitors, 5% conversion            | 20  | 0.05  | **1 sale**       |
| 10 Titanic passengers, 38.3% survival | 10  | 0.383 | **~4 survivors** |

---

## 7. Interpreting Probabilities

P(X = 8) = 0.2335 means:

> _"If this experiment is repeated many times, **exactly 8 successes** will occur about **23.3% of the time.**"_

Or in one shot: _"There's a 23.3% chance (roughly 1 in 4) of getting exactly 8 successes right now."_

---

## 8. Python Reference

```python
from scipy import stats

# Setup
n = 10       # number of trials
p = 0.7      # probability of success

# PMF: P(exactly 8)
stats.binom.pmf(8, n, p)

# CDF: P(8 or fewer)
stats.binom.cdf(8, n, p)

# 1 - CDF: P(at least 8)
1 - stats.binom.cdf(7, n, p)

# All probabilities at once
import numpy as np
all_k = np.arange(0, n+1)
all_probs = stats.binom.pmf(all_k, n, p)
```

---

## 9. Practical Application 1: Website Conversion 💻

**Scenario:** 5% conversion rate, 20 visitors. P(at least 3 buy)?

- n = 20, p = 0.05, want P(X ≥ 3)
- `1 - stats.binom.cdf(2, 20, 0.05)` = **0.076 (7.6%)**
- **Insight:** Only ~1 in 13 days will you get 3+ sales from 20 visitors at 5% conversion.

---

## 10. Practical Application 2: Titanic Survival 🚢

**Scenario:** 38.3% survival rate. Pick 10 random passengers. P(at least 6 survived)?

### Theoretical (Formula)

- `1 - stats.binom.cdf(5, 10, 0.383)` = **0.140 (14.0%)**

### Simulation (10,000 Experiments)

```python
number_of_survivors = []
for i in range(10000):
    random_pick = df.sample(n=10)
    survived = random_pick['survived'].sum()
    number_of_survivors.append(survived)

result = np.array(number_of_survivors)
simulated_probability = np.sum(result >= 6) / 10000
```

- Simulated result: **0.143 (14.3%)**

### Verification

| Method                  | Result |
| ----------------------- | ------ |
| Theoretical (Binomial)  | 14.0%  |
| Simulated (10,000 runs) | 14.3%  |

> The math matches reality — the Binomial model works! ✅

### Business Insight

> _"With only 38.3% survival rate, there's just a 14% chance that 6+ out of 10 random passengers survived. The expected number is ~4 survivors, so 6+ is well above average."_
