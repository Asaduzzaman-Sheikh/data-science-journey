# Week 9 — Lesson 1: From Regression to Classification

> **The Big Picture:** In Week 8, you predicted *how much* (regression). Now you'll predict *which category* (classification). This single shift opens the door to 60%+ of all ML applications in industry.

---

## 1. Why Classification Matters More Than You Think

Every time you interact with technology, a classifier is working behind the scenes:

| What You See | What the Model Predicts | Type |
|---|---|---|
| Gmail moves an email to spam | Spam or Not Spam? | Binary Classification |
| Netflix recommends a movie | Which genre will you watch? | Multi-class Classification |
| A bank approves/denies your loan | Default or No Default? | Binary Classification |
| A doctor reads an X-ray scan | Healthy / Pneumonia / Tumor? | Multi-class Classification |
| Your thesis: Will a product launch succeed? | Success or Failure? | Binary Classification |

> **For your thesis:** Your product launch prediction problem is fundamentally a **classification problem**. Everything you learn this week directly feeds into your research.

---

## 2. Regression vs. Classification — The Core Difference

### What You Already Know (Regression — Week 8)
```
Input → Model → Continuous Number
Example: Student's GPA → Model → Predicted Salary ($52,340)
```

### What You're Learning Now (Classification)
```
Input → Model → Category/Class
Example: Email features → Model → "Spam" or "Not Spam"
```

### The Key Insight
- **Regression** answers: "How much?" / "How many?"
- **Classification** answers: "Which one?" / "Yes or No?"

But here's the clever connection: **Classification is actually regression in disguise.** Instead of predicting a number directly, we predict the **probability** of belonging to a class, and then decide based on a threshold.

```
Input → Model → P(Spam) = 0.87 → Since 0.87 > 0.5 → "Spam"
Input → Model → P(Spam) = 0.12 → Since 0.12 < 0.5 → "Not Spam"
```

This is the bridge from regression to classification. And the model that makes this bridge explicit is **Logistic Regression**.

---

## 3. Logistic Regression — Your First Classifier

### Why Start Here?
Most courses jump to "cool" algorithms like Random Forest or Neural Networks. That's a mistake. Here's why Logistic Regression comes first:

1. **It extends what you already know** — Linear Regression + one extra function
2. **It's still used in production** — Banks, hospitals, and tech companies use it daily
3. **It's interpretable** — You can explain *why* the model made a decision (critical for your thesis)
4. **Interview favorite** — "Explain Logistic Regression" is the #1 most-asked ML interview question (Glassdoor, 2024)

### The Problem with Using Linear Regression for Classification

Imagine you want to predict: **Will a student pass (1) or fail (0)?** based on their study hours.

If you use Linear Regression:
```
ŷ = β₀ + β₁ × (study_hours)
```

The output could be:
- `ŷ = 1.3` → What does this mean? More than pass?
- `ŷ = -0.5` → Negative passing? Makes no sense.

**The problem:** Linear Regression outputs any number from -∞ to +∞, but we need a number between **0 and 1** (a probability).

### The Solution: The Sigmoid Function

The **sigmoid function** (also called the logistic function) squashes any number into the range (0, 1):

```
σ(z) = 1 / (1 + e^(-z))
```

**How it works:**
| Input z | σ(z) | Interpretation |
|---------|------|----------------|
| -∞ | → 0 | Almost certainly Class 0 |
| -2 | 0.12 | Unlikely Class 1 |
| 0 | 0.50 | Coin flip — uncertain |
| +2 | 0.88 | Likely Class 1 |
| +∞ | → 1 | Almost certainly Class 1 |

**The shape:** An S-curve that smoothly transitions from 0 to 1.

### Putting It Together

**Linear Regression:**
```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ     → output: any number
```

**Logistic Regression:**
```
z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ       → linear combination (same as before)
P(y=1|x) = σ(z) = 1 / (1 + e^(-z))       → output: probability between 0 and 1
```

> **The only difference is wrapping the linear equation inside the sigmoid function.** That's it. That's the "trick" that turns regression into classification.

### The Decision Boundary

Once we have a probability, we need a **threshold** to make a decision:

```
If P(y=1|x) ≥ 0.5 → Predict Class 1 (e.g., "Pass")
If P(y=1|x) < 0.5 → Predict Class 0 (e.g., "Fail")
```

> **Clever Trick:** The 0.5 threshold is just the *default*. In real-world applications (medical diagnosis, fraud detection), you often change this threshold based on the **cost of being wrong**. We'll explore this when we learn about ROC curves.

---

## 4. How Logistic Regression Learns — The Loss Function

### Why Can't We Use MSE (Mean Squared Error)?

In Linear Regression, you minimized MSE:
```
MSE = (1/n) Σ (yᵢ - ŷᵢ)²
```

For Logistic Regression, MSE creates a **non-convex** surface (multiple local minima) because of the sigmoid function. The optimizer would get stuck.

### The Solution: Log Loss (Binary Cross-Entropy)

```
Log Loss = -(1/n) Σ [yᵢ · log(ŷᵢ) + (1 - yᵢ) · log(1 - ŷᵢ)]
```

**Why this works — intuition:**

| Actual | Predicted P(y=1) | Penalty |
|--------|---------|---------|
| y = 1 | ŷ = 0.99 | Very small (good prediction!) |
| y = 1 | ŷ = 0.01 | **Huge** (you were confident and wrong!) |
| y = 0 | ŷ = 0.01 | Very small (good prediction!) |
| y = 0 | ŷ = 0.99 | **Huge** (you were confident and wrong!) |

> **Key Insight:** The log loss function punishes **confident wrong predictions** much more than uncertain ones. This is exactly the behavior we want — the model learns to be cautious when it's unsure.

### Optimization: Gradient Descent

Logistic Regression uses the same **gradient descent** algorithm you saw in Linear Regression:
1. Start with random weights (β₀, β₁, ..., βₙ)
2. Calculate the loss
3. Compute gradients (direction of steepest descent)
4. Update weights: `βₙ = βₙ - α × ∂Loss/∂βₙ`
5. Repeat until convergence

The difference: the gradient formula includes the sigmoid function, but sklearn handles this for you.

---

## 5. Multi-Class Classification

What if you have more than 2 classes? (e.g., predicting product category: Electronics, Fashion, Food)

### Two Strategies:

**One-vs-Rest (OvR):** Train K separate binary classifiers, one per class.
```
Classifier 1: Electronics vs. Everything Else
Classifier 2: Fashion vs. Everything Else  
Classifier 3: Food vs. Everything Else
→ Pick the class with the highest probability
```

**Softmax Regression (Multinomial):** Generalize sigmoid to K classes simultaneously.
```
P(y=k|x) = e^(zₖ) / Σⱼ e^(zⱼ)    → all K probabilities sum to 1
```

> In sklearn, `LogisticRegression(multi_class='multinomial')` uses softmax automatically.

---

## 6. Assumptions of Logistic Regression

| # | Assumption | What It Means | How to Check |
|---|-----------|---------------|--------------|
| 1 | **Binary/Ordinal outcome** | The target is categorical | Check `y.unique()` |
| 2 | **Independence of observations** | Each data point is independent | Domain knowledge |
| 3 | **No multicollinearity** | Features shouldn't be highly correlated with each other | Check VIF or correlation matrix |
| 4 | **Linear relationship between features and log-odds** | The log(P/(1-P)) is linear in X | Plot log-odds vs features |
| 5 | **Large enough sample size** | Rule of thumb: 10+ events per predictor variable | Check dataset size |

> **Clever Trick for interviews:** Logistic Regression does NOT assume normal distribution of features, unlike what many textbooks wrongly state. Knowing this shows depth.

---

## 7. Interpreting Logistic Regression — Odds and Log-Odds

This is where your statistics knowledge from Week 8 becomes a superpower.

### Odds
```
Odds = P(event) / P(no event) = P / (1-P)
```
- If P = 0.8, Odds = 0.8/0.2 = 4:1 (event is 4x more likely than not)
- If P = 0.5, Odds = 1:1 (coin flip)

### Log-Odds (Logit)
```
log(Odds) = log(P / (1-P)) = β₀ + β₁x₁ + β₂x₂ + ...
```

### Interpreting Coefficients
- **β₁ = 0.5** means: A 1-unit increase in x₁ increases the **log-odds** by 0.5
- In terms of **odds**: e^0.5 = 1.65, so the odds increase by **65%** for each unit increase in x₁

> **For your thesis:** If a feature like "social media sentiment score" has β = 0.8, you can write: *"A one-unit increase in social media sentiment is associated with a 123% increase in the odds of product launch success (e^0.8 = 2.23)."* That's a powerful, publishable finding.

---

## 8. When to Use (and NOT Use) Logistic Regression

### ✅ Use When:
- You need **interpretable** results (thesis, business reporting)
- You have a **binary or multi-class** target
- The relationship between features and log-odds is roughly **linear**
- You need a **baseline model** to compare other algorithms against
- The dataset is **small to medium** sized

### ❌ Don't Use When:
- The decision boundary is highly **non-linear** (use trees or neural nets)
- You have **very high dimensional data** with complex interactions (use ensemble methods)
- You need **maximum predictive accuracy** at the cost of interpretability

---

## 9. The Sklearn Workflow — Production Pattern

```python
# THE PATTERN YOU'LL USE FOR EVERY ML MODEL
# (Memorize this — it's the same structure for all sklearn models)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

# Step 1: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify keeps class balance!
)

# Step 2: Build pipeline (THE CLEVER TRICK — most beginners skip this)
pipe = Pipeline([
    ('scaler', StandardScaler()),         # Always scale for Logistic Regression
    ('classifier', LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

# Step 3: Train
pipe.fit(X_train, y_train)

# Step 4: Predict
y_pred = pipe.predict(X_test)
y_prob = pipe.predict_proba(X_test)[:, 1]  # probabilities for positive class

# Step 5: Evaluate
print(classification_report(y_test, y_pred))
```

> **Why pipelines matter:** They prevent **data leakage** (fitting the scaler on test data), they make your code **reproducible**, and they show interviewers that you think like an engineer, not just an analyst.

---

## Summary — What You Learned in This Lesson

| Concept | One-Line Summary |
|---------|-----------------|
| Classification | Predicting categories instead of numbers |
| Sigmoid | Squashes any number to (0, 1) — the bridge from regression to classification |
| Log Loss | Punishes confident wrong predictions — the training objective |
| Decision Boundary | The threshold (usually 0.5) that converts probability to class |
| Odds & Log-Odds | How to interpret coefficients — your thesis writing tool |
| Pipelines | Professional ML workflow — scaler + model in one object |

---

## Next Up: Lesson 2 — Hands-On Coding
We'll build a Logistic Regression classifier from scratch on a real dataset, evaluate it properly, and learn the metrics that actually matter (hint: accuracy is NOT one of them).
