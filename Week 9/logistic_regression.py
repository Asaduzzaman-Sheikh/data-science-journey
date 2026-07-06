"""
Week 9 — Hands-On: Logistic Regression on the Breast Cancer Wisconsin Dataset

WHY THIS DATASET?
- Real medical data (not a toy dataset)
- Binary classification: Malignant (1) vs Benign (0)
- 569 samples, 30 features — realistic but manageable
- Slightly imbalanced — teaches you to handle real-world data
- Built into sklearn — no downloading needed

WHAT YOU'LL LEARN:
1. The complete sklearn ML workflow (you'll reuse this pattern for EVERY model)
2. Proper train-test splitting with stratification
3. Building a Pipeline (the professional way)
4. Evaluating with the metrics that actually matter
5. Visualizing ROC curves and confusion matrices
6. Interpreting model coefficients
"""

# ============================================================
# SECTION 1: IMPORTS & SETUP
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

# Sklearn imports — organized by purpose
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, ConfusionMatrixDisplay,
    roc_curve, roc_auc_score, precision_recall_curve, RocCurveDisplay
)

# Plot styling
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("✅ All imports successful!")

# ============================================================
# SECTION 2: LOAD & EXPLORE DATA
# ============================================================
print("\n" + "="*60)
print("📊 SECTION 2: LOADING & EXPLORING THE DATA")
print("="*60)

# Load dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# Check it out
print(f"\n📐 Dataset Shape: {X.shape}")
print(f"   → {X.shape[0]} patients, {X.shape[1]} features")

print(f"\n🏷️  Classes:")
for i, name in enumerate(data.target_names):
    count = (y == i).sum()
    pct = count / len(y) * 100
    print(f"   {i} = {name}: {count} ({pct:.1f}%)")

print(f"\n🔍 First 5 features: {list(X.columns[:5])}")
print(f"   ... and {X.shape[1] - 5} more")

# Check for missing values
print(f"\n❓ Missing values: {X.isnull().sum().sum()}")

# Quick statistics
print("\n📈 Feature Statistics (first 5 features):")
print(X.iloc[:, :5].describe().round(2))

# ============================================================
# EXERCISE 1: YOUR TURN 🧠
# ============================================================
"""
EXERCISE 1: Explore the data further
1. Print the full list of feature names
2. Check if there are any highly correlated features (hint: X.corr())
3. Create a histogram of any one feature, colored by class
   (hint: use plt.hist() with y==0 and y==1 separately)

Your code here:
"""


# ============================================================
# SECTION 3: TRAIN-TEST SPLIT
# ============================================================
print("\n" + "="*60)
print("✂️  SECTION 3: TRAIN-TEST SPLIT")
print("="*60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,       # 80% train, 20% test
    random_state=42,      # Reproducibility
    stratify=y            # ← CLEVER TRICK: maintains class proportions in both sets
)

print(f"\n📊 Training set: {X_train.shape[0]} samples")
print(f"   Class distribution: {dict(y_train.value_counts().sort_index())}")
print(f"\n📊 Test set: {X_test.shape[0]} samples")
print(f"   Class distribution: {dict(y_test.value_counts().sort_index())}")

# Verify stratification worked
train_ratio = y_train.mean()
test_ratio = y_test.mean()
original_ratio = y.mean()
print(f"\n✅ Stratification check (% positive class):")
print(f"   Original: {original_ratio:.3f} | Train: {train_ratio:.3f} | Test: {test_ratio:.3f}")

# ============================================================
# SECTION 4: BUILD THE PIPELINE
# ============================================================
print("\n" + "="*60)
print("🔧 SECTION 4: BUILDING THE PIPELINE")
print("="*60)

# THE PROFESSIONAL WAY — use Pipeline
# This ensures the scaler is fit ONLY on training data (prevents data leakage)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(
        max_iter=10000,
        random_state=42,
        C=1.0,           # Regularization strength (1/λ). Smaller = more regularization
        penalty='l2',     # L2 regularization (Ridge). Prevents overfitting
        solver='lbfgs'    # Optimization algorithm (good default for small-medium datasets)
    ))
])

print("Pipeline created:")
print(pipeline)

# ============================================================
# SECTION 5: TRAIN THE MODEL
# ============================================================
print("\n" + "="*60)
print("🏋️ SECTION 5: TRAINING THE MODEL")
print("="*60)

pipeline.fit(X_train, y_train)
print("✅ Model trained successfully!")

# ============================================================
# SECTION 6: PREDICTIONS
# ============================================================
print("\n" + "="*60)
print("🎯 SECTION 6: MAKING PREDICTIONS")
print("="*60)

# Class predictions
y_pred = pipeline.predict(X_test)

# Probability predictions (this is what makes logistic regression special)
y_prob = pipeline.predict_proba(X_test)

print("\n📋 Sample predictions (first 10 patients):")
print(f"{'Actual':>8} {'Predicted':>10} {'P(Benign)':>10} {'P(Malign)':>11} {'Correct?':>9}")
print("-" * 52)
for i in range(10):
    actual = data.target_names[y_test.iloc[i]]
    predicted = data.target_names[y_pred[i]]
    p_malignant = y_prob[i][0]
    p_benign = y_prob[i][1]
    correct = "✅" if y_test.iloc[i] == y_pred[i] else "❌"
    print(f"{actual:>8} {predicted:>10} {p_benign:>10.4f} {p_malignant:>11.4f} {correct:>9}")

# ============================================================
# SECTION 7: EVALUATION — THE METRICS THAT MATTER
# ============================================================
print("\n" + "="*60)
print("📊 SECTION 7: EVALUATION METRICS")
print("="*60)

# --- 7a: Classification Report ---
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# --- 7b: Individual Metrics ---
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_prob[:, 1])

print("📈 Key Metrics Summary:")
print(f"   Accuracy:  {accuracy:.4f}  — Overall correctness")
print(f"   Precision: {precision:.4f}  — When we say 'benign', how often are we right?")
print(f"   Recall:    {recall:.4f}  — Out of all benign cases, how many did we catch?")
print(f"   F1-Score:  {f1:.4f}  — Balanced metric")
print(f"   AUC-ROC:   {auc_score:.4f}  — Rank quality (threshold-independent)")

# --- 7c: Confusion Matrix Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Raw counts
cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=data.target_names).plot(
    ax=axes[0], cmap='Blues', colorbar=False
)
axes[0].set_title('Confusion Matrix (Counts)', fontweight='bold', fontsize=13)

# Normalized (percentages)
cm_norm = confusion_matrix(y_test, y_pred, normalize='true')
ConfusionMatrixDisplay(cm_norm, display_labels=data.target_names).plot(
    ax=axes[1], cmap='Oranges', colorbar=False, values_format='.2%'
)
axes[1].set_title('Confusion Matrix (Normalized)', fontweight='bold', fontsize=13)

plt.tight_layout()
plt.savefig('e:/DataScience/Week 9/confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Confusion matrix saved!")

# ============================================================
# SECTION 8: ROC CURVE & PRECISION-RECALL CURVE
# ============================================================
print("\n" + "="*60)
print("📈 SECTION 8: ROC & PRECISION-RECALL CURVES")
print("="*60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- ROC Curve ---
fpr, tpr, thresholds_roc = roc_curve(y_test, y_prob[:, 1])
axes[0].plot(fpr, tpr, color='#E74C3C', linewidth=2.5,
             label=f'Logistic Regression (AUC = {auc_score:.3f})')
axes[0].plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Random Guess (AUC = 0.500)')
axes[0].fill_between(fpr, tpr, alpha=0.1, color='#E74C3C')
axes[0].set_xlabel('False Positive Rate', fontsize=12)
axes[0].set_ylabel('True Positive Rate (Recall)', fontsize=12)
axes[0].set_title('ROC Curve', fontweight='bold', fontsize=14)
axes[0].legend(loc='lower right', fontsize=10)
axes[0].set_xlim([0, 1])
axes[0].set_ylim([0, 1.02])

# --- Precision-Recall Curve ---
precision_vals, recall_vals, thresholds_pr = precision_recall_curve(y_test, y_prob[:, 1])
axes[1].plot(recall_vals, precision_vals, color='#3498DB', linewidth=2.5,
             label='Logistic Regression')
axes[1].axhline(y=y_test.mean(), color='k', linestyle='--', alpha=0.5,
                label=f'Baseline (P={y_test.mean():.2f})')
axes[1].set_xlabel('Recall', fontsize=12)
axes[1].set_ylabel('Precision', fontsize=12)
axes[1].set_title('Precision-Recall Curve', fontweight='bold', fontsize=14)
axes[1].legend(loc='lower left', fontsize=10)
axes[1].set_xlim([0, 1])
axes[1].set_ylim([0, 1.02])

plt.tight_layout()
plt.savefig('e:/DataScience/Week 9/roc_pr_curves.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ ROC & PR curves saved!")

# ============================================================
# SECTION 9: CROSS-VALIDATION — THE RIGHT WAY TO EVALUATE
# ============================================================
print("\n" + "="*60)
print("🔄 SECTION 9: CROSS-VALIDATION")
print("="*60)

"""
WHY CROSS-VALIDATION?
A single train-test split is like rolling a dice once. You might get lucky or unlucky.
Cross-validation rolls the dice K times and averages the results.

HOW IT WORKS (5-Fold):
[Fold1=Test | Fold2 | Fold3 | Fold4 | Fold5 ]  → Score 1
[Fold1 | Fold2=Test | Fold3 | Fold4 | Fold5 ]  → Score 2
[Fold1 | Fold2 | Fold3=Test | Fold4 | Fold5 ]  → Score 3
[Fold1 | Fold2 | Fold3 | Fold4=Test | Fold5 ]  → Score 4
[Fold1 | Fold2 | Fold3 | Fold4 | Fold5=Test ]  → Score 5
                                                  → Final = Average
"""

# StratifiedKFold maintains class balance in each fold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Score with multiple metrics
for metric in ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']:
    scores = cross_val_score(pipeline, X, y, cv=cv, scoring=metric)
    print(f"   {metric:>12}: {scores.mean():.4f} ± {scores.std():.4f}  {scores.round(3)}")

print("\n💡 The ± value is the standard deviation across folds.")
print("   Small std = consistent model. Large std = unstable model.")

# ============================================================
# SECTION 10: INTERPRETING THE MODEL
# ============================================================
print("\n" + "="*60)
print("🔬 SECTION 10: MODEL INTERPRETATION")
print("="*60)

# Get coefficients from the pipeline
model = pipeline.named_steps['classifier']
coefs = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0],
    'Abs_Coefficient': np.abs(model.coef_[0]),
    'Odds_Ratio': np.exp(model.coef_[0])
}).sort_values('Abs_Coefficient', ascending=False)

print("\n🔝 Top 10 Most Important Features:")
print(f"{'Feature':<30} {'Coefficient':>12} {'Odds Ratio':>12} {'Direction':>10}")
print("-" * 68)
for _, row in coefs.head(10).iterrows():
    direction = "↑ Benign" if row['Coefficient'] > 0 else "↑ Malignant"
    print(f"{row['Feature']:<30} {row['Coefficient']:>12.4f} {row['Odds_Ratio']:>12.4f} {direction:>10}")

# Visualize feature importance
fig, ax = plt.subplots(figsize=(10, 8))
top_features = coefs.head(15)
colors = ['#2ECC71' if c > 0 else '#E74C3C' for c in top_features['Coefficient']]
ax.barh(top_features['Feature'], top_features['Coefficient'], color=colors, edgecolor='white')
ax.set_xlabel('Coefficient Value', fontsize=12)
ax.set_title('Top 15 Feature Coefficients\n(Green = ↑ Benign, Red = ↑ Malignant)',
             fontweight='bold', fontsize=14)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('e:/DataScience/Week 9/feature_importance.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Feature importance plot saved!")

# ============================================================
# SECTION 11: THRESHOLD ANALYSIS
# ============================================================
print("\n" + "="*60)
print("⚙️  SECTION 11: THRESHOLD ANALYSIS")
print("="*60)

"""
CLEVER TRICK: Don't just use the default 0.5 threshold.
In medical diagnosis, you might want to lower it to catch more diseases (higher recall).
"""

thresholds_to_try = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

print(f"\n{'Threshold':>10} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("-" * 54)

for t in thresholds_to_try:
    y_pred_t = (y_prob[:, 1] >= t).astype(int)
    print(f"{t:>10.1f} "
          f"{accuracy_score(y_test, y_pred_t):>10.4f} "
          f"{precision_score(y_test, y_pred_t, zero_division=0):>10.4f} "
          f"{recall_score(y_test, y_pred_t, zero_division=0):>10.4f} "
          f"{f1_score(y_test, y_pred_t, zero_division=0):>10.4f}")

print("\n💡 Notice how lowering the threshold increases recall but decreases precision.")
print("   In cancer detection, we'd prefer threshold=0.3 to catch more cancer cases.")

# ============================================================
# EXERCISE 2: YOUR TURN 🧠
# ============================================================
"""
EXERCISE 2: Build it yourself
1. Try changing the regularization strength C to [0.01, 0.1, 1, 10, 100]
   and see how it affects the metrics.

2. Try using only the top 5 features (based on coefficient magnitude)
   and compare the results to using all 30 features.

3. For your thesis connection: If this were a product launch prediction model,
   which threshold would you choose and why? Write your reasoning as a comment.

Your code here:
"""


# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "="*60)
print("🎓 SESSION SUMMARY")
print("="*60)
print("""
What you built today:
✅ Loaded and explored a real medical dataset
✅ Split data with stratification (no data leakage!)
✅ Built a professional sklearn Pipeline
✅ Trained a Logistic Regression classifier
✅ Evaluated with 5 different metrics
✅ Plotted ROC curve and Precision-Recall curve
✅ Performed 5-fold cross-validation
✅ Interpreted model coefficients (odds ratios)
✅ Analyzed threshold impact on metrics

KEY TAKEAWAYS:
1. Pipeline = Scaler + Model in one object (prevents leakage)
2. Accuracy alone is NOT enough — always check precision, recall, F1, AUC
3. The threshold is a business decision, not a statistical one
4. Cross-validation > single train-test split
5. Coefficients tell you WHICH features matter and in WHICH direction

NEXT: Decision Trees & Random Forests — models that handle non-linear
relationships and are even more powerful for tabular data.
""")
