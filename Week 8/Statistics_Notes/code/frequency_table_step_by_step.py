"""
Step-by-Step: Creating a Frequency Table with Bins
===================================================
This script demonstrates pd.cut() with output at each step.
"""

import pandas as pd

# =============================================================================
# STEP 1: Create your raw data
# =============================================================================
print("=" * 60)
print("STEP 1: Raw Data")
print("=" * 60)

data = [45, 52, 67, 71, 73, 75, 78, 79, 80, 81,
        82, 83, 85, 86, 88, 89, 91, 93, 95, 98]

print(f"Data: {data}")
print(f"Number of values: {len(data)}")
print(f"Min: {min(data)}, Max: {max(data)}")
print(f"Range: {max(data) - min(data)}")

# =============================================================================
# STEP 2: Define bins and labels
# =============================================================================
print("\n" + "=" * 60)
print("STEP 2: Define Bins and Labels")
print("=" * 60)

# Bin edges (boundaries)
bins = [40, 50, 60, 70, 80, 90, 100]
print(f"Bin edges: {bins}")
print("This creates 6 bins:")
print("  [40-50), [50-60), [60-70), [70-80), [80-90), [90-100)")

# Labels for each bin
labels = ['40-49', '50-59', '60-69', '70-79', '80-89', '90-99']
print(f"\nLabels: {labels}")

# =============================================================================
# STEP 3: Create DataFrame from raw data
# =============================================================================
print("\n" + "=" * 60)
print("STEP 3: Create DataFrame")
print("=" * 60)

df = pd.DataFrame({'Scores': data})
print("Created DataFrame with column 'Scores':")
print(df.head(10))
print("...")

# =============================================================================
# STEP 4: Apply pd.cut() to assign each score to a bin
# =============================================================================
print("\n" + "=" * 60)
print("STEP 4: Apply pd.cut() — Assign Scores to Bins")
print("=" * 60)

df['Bin'] = pd.cut(
    df['Scores'],      # Column to bin
    bins=bins,         # Bin edges
    labels=labels,     # Bin names
    right=False        # [40, 50) means 40 included, 50 excluded
)

print("Added 'Bin' column using pd.cut():")
print(df.head(10))
print("...")

# Show how each score was assigned
print("\nHow each score was binned:")
for score, bin_label in zip(df['Scores'].head(6), df['Bin'].head(6)):
    print(f"  Score {score} → Bin '{bin_label}'")

# =============================================================================
# STEP 5: Count frequencies using value_counts()
# =============================================================================
print("\n" + "=" * 60)
print("STEP 5: Count Frequencies with value_counts()")
print("=" * 60)

counts = df['Bin'].value_counts()
print("Raw value_counts() result (sorted by frequency):")
print(counts)

# =============================================================================
# STEP 6: Sort by bin order with sort_index()
# =============================================================================
print("\n" + "=" * 60)
print("STEP 6: Sort by Bin Order with sort_index()")
print("=" * 60)

counts_sorted = df['Bin'].value_counts().sort_index()
print("After sort_index() (sorted by bin name):")
print(counts_sorted)

# =============================================================================
# STEP 7: Convert to DataFrame with reset_index()
# =============================================================================
print("\n" + "=" * 60)
print("STEP 7: Convert to DataFrame with reset_index()")
print("=" * 60)

frequency_table = df['Bin'].value_counts().sort_index().reset_index()
print("After reset_index():")
print(frequency_table)

# =============================================================================
# STEP 8: Rename columns
# =============================================================================
print("\n" + "=" * 60)
print("STEP 8: Rename Columns")
print("=" * 60)

frequency_table.columns = ['Score Range', 'Frequency']
print("After renaming columns:")
print(frequency_table)

# =============================================================================
# STEP 9: Add additional columns (optional but useful)
# =============================================================================
print("\n" + "=" * 60)
print("STEP 9: Add Relative & Cumulative Frequency")
print("=" * 60)

# Relative Frequency
frequency_table['Relative Freq'] = frequency_table['Frequency'] / len(data)
frequency_table['Relative Freq'] = frequency_table['Relative Freq'].round(2)

# Percentage
frequency_table['Percentage'] = (frequency_table['Relative Freq'] * 100).astype(int)

# Cumulative Frequency
frequency_table['Cumulative Freq'] = frequency_table['Frequency'].cumsum()

print("Complete Frequency Table:")
print(frequency_table)

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("FINAL: Complete Frequency Table")
print("=" * 60)
print(frequency_table.to_string(index=False))
