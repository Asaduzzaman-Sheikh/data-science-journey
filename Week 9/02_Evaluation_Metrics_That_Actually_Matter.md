# Week 9 — Lesson 2: Evaluation Metrics That Actually Matter

> **The #1 mistake beginners make:** Using accuracy as their only metric. This lesson teaches you why that's dangerous and what to use instead.

---

## 1. Why Accuracy is a Trap

Imagine this scenario:

You build a model to detect credit card fraud. Your dataset:
- 9,950 legitimate transactions (99.5%)
- 50 fraudulent transactions (0.5%)

You build a "model" that **always predicts "Not Fraud"**. Its accuracy?

```
Accuracy = 9,950 / 10,000 = 99.5% 🎉
```

**99.5% accuracy!** But it catches **zero fraud**. It's completely useless.

This is the **accuracy paradox** — when classes are imbalanced, accuracy is misleading.

> **For your thesis:** If product launches succeed 80% of the time, a model that always predicts "success" gets 80% accuracy but has zero predictive value.

---

## 2. The Confusion Matrix — Your Diagnostic Tool

Every classification prediction falls into one of 4 categories:

```
                    Predicted
                 Positive  Negative
Actual Positive [   TP   |   FN   ]    ← Actual positives
Actual Negative [   FP   |   TN   ]    ← Actual negatives
```

| Term | Full Name | Meaning | Memory Trick |
|------|-----------|---------|-------------|
| **TP** | True Positive | Correctly predicted positive | "Hit" |
| **TN** | True Negative | Correctly predicted negative | "Correct rejection" |
| **FP** | False Positive | Incorrectly predicted positive | "False alarm" / **Type I Error** |
| **FN** | False Negative | Incorrectly predicted negative | "Missed" / **Type II Error** |

> **Connection to your stats knowledge (Week 8):** FP = Type I Error (α), FN = Type II Error (β). You already know this concept from hypothesis testing!

---

## 3. The Metrics That Matter

### Precision — "When the model says YES, how often is it right?"

```
Precision = TP / (TP + FP)
```

**Use when:** The cost of **false positives** is high.
- **Spam filter:** If you mark a real email as spam (FP), the user misses an important message
- **Product recommendations:** If you recommend irrelevant products (FP), users lose trust

### Recall (Sensitivity) — "Out of all actual positives, how many did the model catch?"

```
Recall = TP / (TP + FN)
```

**Use when:** The cost of **false negatives (missing things)** is high.
- **Cancer detection:** Missing a cancer case (FN) could be fatal
- **Fraud detection:** Missing fraud (FN) means financial loss
- **Your thesis:** If a product is going to fail, missing that prediction (FN) means wasted resources

### F1-Score — The Balanced Metric

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

The **harmonic mean** of precision and recall. Use when you need a single number that balances both.

**Why harmonic mean, not arithmetic mean?**
- Arithmetic mean of (0.99, 0.01) = 0.50 → hides the terrible recall
- Harmonic mean of (0.99, 0.01) = 0.02 → exposes the weakness

> **Clever Trick:** F1-score punishes extreme imbalances. If either precision or recall is very low, F1 drops dramatically. This is why interviewers ask about F1 specifically.

### Summary Table

| Metric | Formula | Optimize When |
|--------|---------|---------------|
| **Accuracy** | (TP+TN) / Total | Classes are balanced, costs are equal |
| **Precision** | TP / (TP+FP) | False positives are costly |
| **Recall** | TP / (TP+FN) | False negatives are costly |
| **F1-Score** | Harmonic mean of P & R | You need balance, classes may be imbalanced |

---

## 4. The Precision-Recall Tradeoff

Here's the uncomfortable truth: **You can't maximize both precision and recall simultaneously.**

### Why?
- To increase **recall** (catch more positives), you lower the threshold → more FPs → precision drops
- To increase **precision** (reduce false alarms), you raise the threshold → more FNs → recall drops

```
Threshold = 0.3 → Catches almost everything → High Recall, Low Precision
Threshold = 0.5 → Balanced (default)
Threshold = 0.8 → Only very confident predictions → High Precision, Low Recall
```

> **Clever Trick for your thesis:** Report results at multiple thresholds and let the business/domain context decide. Write: *"At a threshold of 0.4 (favoring recall), the model identifies 91% of failing product launches at the cost of a 23% false alarm rate."* This shows sophisticated understanding.

---

## 5. ROC Curve & AUC — The Gold Standard

### ROC Curve (Receiver Operating Characteristic)
Plots **True Positive Rate (Recall)** vs. **False Positive Rate** at every possible threshold.

```
TPR (Recall) = TP / (TP + FN)     → How many positives did you catch?
FPR = FP / (FP + TN)               → How many negatives did you wrongly flag?
```

### AUC (Area Under the ROC Curve)
- **AUC = 1.0** → Perfect classifier
- **AUC = 0.5** → Random guessing (diagonal line)
- **AUC < 0.5** → Worse than random (your labels might be flipped!)

### How to Interpret AUC

| AUC Range | Quality | Action |
|-----------|---------|--------|
| 0.90 – 1.00 | Excellent | Ship it |
| 0.80 – 0.90 | Good | Acceptable for most applications |
| 0.70 – 0.80 | Fair | Needs improvement, feature engineering |
| 0.60 – 0.70 | Poor | Reconsider features or model |
| 0.50 – 0.60 | Fail | Model is barely better than random |

> **Why AUC is the gold standard:** It's **threshold-independent**. It tells you how well the model separates classes across ALL thresholds, not just one. That's why Kaggle competitions and research papers almost always report AUC.

---

## 6. Classification Report in Python — Reading It Like a Pro

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Output example:
```
              precision    recall  f1-score   support

           0       0.85      0.90      0.87       200   ← Class 0 (e.g., Fail)
           1       0.88      0.82      0.85       180   ← Class 1 (e.g., Pass)

    accuracy                           0.86       380   ← Overall accuracy
   macro avg       0.86      0.86      0.86       380   ← Simple average across classes
weighted avg       0.86      0.86      0.86       380   ← Weighted by class size
```

### How to Read This:
1. **Look at the minority class first** (the one with fewer samples). That's where models usually struggle.
2. **Compare precision vs. recall** for each class. A big gap means the model is biased.
3. **"support"** tells you how many samples are in each class. If support is very low, the metrics for that class are unreliable.
4. **macro avg** treats all classes equally (use for balanced classes).
5. **weighted avg** accounts for class sizes (use for imbalanced classes).

---

## 7. Which Metric to Choose — Decision Framework

```
START HERE
    │
    ▼
Are your classes balanced?
    │
    ├── YES → Use Accuracy + F1 + AUC
    │
    └── NO → What's more costly?
              │
              ├── Missing positives (FN) → Optimize RECALL
              │   Examples: Cancer detection, fraud, security threats
              │
              └── False alarms (FP) → Optimize PRECISION
                  Examples: Spam filter, product recommendations, legal decisions
              │
              └── Both matter equally → Optimize F1-SCORE
              
    ALWAYS → Report AUC as a supplementary metric
```

---

## 8. Beyond Binary: Multi-Class Metrics

When you have 3+ classes, metrics are computed **per class** and then averaged:

| Average Type | How | When |
|-------------|-----|------|
| **Macro** | Average metric across all classes equally | Classes are equally important |
| **Weighted** | Weight each class by its sample count | Classes have different sizes |
| **Micro** | Aggregate all TP, FP, FN globally, then compute | Multi-label problems |

```python
from sklearn.metrics import f1_score

# Macro: treats each class equally
f1_score(y_test, y_pred, average='macro')

# Weighted: accounts for class imbalance
f1_score(y_test, y_pred, average='weighted')
```

---

## Quick Reference Card

| Question You're Answering | Metric | Python |
|--------------------------|--------|--------|
| Overall correctness (balanced data) | Accuracy | `accuracy_score()` |
| How many false alarms? | Precision | `precision_score()` |
| How many did I miss? | Recall | `recall_score()` |
| Balance of precision & recall | F1 | `f1_score()` |
| Rank quality across thresholds | AUC-ROC | `roc_auc_score()` |
| Visualize the full picture | Confusion Matrix | `confusion_matrix()` / `ConfusionMatrixDisplay` |

---

## Next Up: Lesson 3 — Hands-On Coding Notebook
We'll now put EVERYTHING together — build a Logistic Regression model on a real dataset, evaluate with all these metrics, and plot ROC curves.
