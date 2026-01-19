"""
Chapter 3: Visualizing Distributions
=====================================
This script demonstrates how to create frequency tables and histograms in Python.
"""

# =============================================================================
# SETUP: Import the required libraries
# =============================================================================
import pandas as pd              # For data organization
import matplotlib.pyplot as plt  # For creating charts
import numpy as np               # For numerical operations

# =============================================================================
# EXAMPLE 1: Simple Frequency Table
# =============================================================================
print("=" * 50)
print("EXAMPLE 1: Simple Frequency Table")
print("=" * 50)

# Create our data: test scores from 16 students
scores = [72, 85, 91, 68, 75, 82, 88, 79, 94, 71, 83, 77, 86, 69, 90, 81]

# Convert to pandas Series and count each value
scores_series = pd.Series(scores)
frequency = scores_series.value_counts().sort_index()

print("\nEach score and how often it appears:")
print(frequency)

# =============================================================================
# EXAMPLE 2: Grouped Frequency Table (with bins)
# =============================================================================
print("\n" + "=" * 50)
print("EXAMPLE 2: Grouped Frequency Table")
print("=" * 50)

# Define bins (ranges) and labels
bins = [60, 70, 80, 90, 100]
labels = ['60-69', '70-79', '80-89', '90-99']

# Group scores into bins
score_bins = pd.cut(scores, bins=bins, labels=labels, right=False)
frequency_table = score_bins.value_counts().sort_index()

print("\nScores grouped by range:")
print(frequency_table)

# =============================================================================
# EXAMPLE 3: Histogram (Visual Frequency Table)
# =============================================================================
print("\n" + "=" * 50)
print("EXAMPLE 3: Creating a Histogram")
print("=" * 50)

# Create the figure
plt.figure(figsize=(10, 6))

# Create the histogram
plt.hist(scores, 
         bins=[60, 70, 80, 90, 100],  # Bin edges
         edgecolor='black',            # Black border on bars
         color='steelblue',            # Bar color
         alpha=0.7)                    # Slight transparency

# Add labels and title
plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Frequency (Number of Students)', fontsize=12)
plt.title('Distribution of Test Scores', fontsize=14)

# Add gridlines
plt.grid(axis='y', alpha=0.3)

# Add value labels on top of each bar
counts, bin_edges, _ = plt.hist(scores, bins=[60, 70, 80, 90, 100], 
                                 edgecolor='black', color='steelblue', alpha=0.7)
for i, count in enumerate(counts):
    plt.text((bin_edges[i] + bin_edges[i+1]) / 2, count + 0.1, 
             str(int(count)), ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('histogram_test_scores.png', dpi=150)
print("\nHistogram saved as 'histogram_test_scores.png'")
plt.show()

# =============================================================================
# YOUR TURN: Practice Exercise
# =============================================================================
print("\n" + "=" * 50)
print("YOUR TURN: Practice Exercise")
print("=" * 50)

# Here are ages of 12 customers at a store
ages = [25, 34, 42, 28, 31, 45, 38, 29, 33, 41, 27, 36]

print("\nCustomer ages:", ages)
print("\nTry to:")
print("1. Create a frequency table with bins: 25-29, 30-34, 35-39, 40-45")
print("2. Create a histogram of the ages")
print("\nUncomment the code below and fill in the blanks!")

# -----------------------------------------------------------------------------
# UNCOMMENT AND COMPLETE THIS CODE:
# -----------------------------------------------------------------------------
# bins = [25, 30, 35, 40, 46]  # Note: 46 to include 45
# labels = ['25-29', '30-34', '35-39', '40-45']
# 
# # Create frequency table
# age_bins = pd.cut(ages, bins=bins, labels=labels, right=False)
# age_frequency = age_bins.value_counts().sort_index()
# print("\nAge Distribution:")
# print(age_frequency)
# 
# # Create histogram
# plt.figure(figsize=(10, 6))
# plt.hist(ages, bins=bins, edgecolor='black', color='coral', alpha=0.7)
# plt.xlabel('Age Range')
# plt.ylabel('Frequency')
# plt.title('Distribution of Customer Ages')
# plt.grid(axis='y', alpha=0.3)
# plt.show()
