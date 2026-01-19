"""
Bar Charts for Categorical Data
================================
This script demonstrates how to create bar charts using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# Create Frequency Table
# =============================================================================
fruits = ['Apple', 'Banana', 'Apple', 'Orange', 'Apple', 'Banana', 'Mango', 
          'Apple', 'Orange', 'Banana', 'Apple', 'Mango', 'Banana', 'Apple', 
          'Orange', 'Banana', 'Apple', 'Mango', 'Banana', 'Apple', 'Orange', 
          'Apple', 'Banana', 'Mango', 'Apple', 'Orange', 'Banana', 'Mango', 
          'Apple', 'Orange']

df = pd.DataFrame({'Fruits': fruits})
frequency_table = df['Fruits'].value_counts().reset_index()
frequency_table.columns = ['Fruits', 'Count']

print("Frequency Table:")
print(frequency_table)
print()

# =============================================================================
# BAR CHART 1: Basic Vertical Bar Chart
# =============================================================================
plt.figure(figsize=(10, 6))

plt.bar(frequency_table['Fruits'], frequency_table['Count'], 
        color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
        edgecolor='black',
        linewidth=1.2)

# Add value labels on top of bars
for i, (fruit, count) in enumerate(zip(frequency_table['Fruits'], frequency_table['Count'])):
    plt.text(i, count + 0.3, str(count), ha='center', fontsize=12, fontweight='bold')

plt.xlabel('Fruit Type', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Bar Chart: Fruit Distribution', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('bar_chart_vertical.png', dpi=150)
print("Chart 1 saved: bar_chart_vertical.png")
plt.close()

# =============================================================================
# BAR CHART 2: Horizontal Bar Chart
# =============================================================================
plt.figure(figsize=(10, 6))

plt.barh(frequency_table['Fruits'], frequency_table['Count'],
         color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
         edgecolor='black',
         linewidth=1.2)

# Add value labels
for i, count in enumerate(frequency_table['Count']):
    plt.text(count + 0.3, i, str(count), va='center', fontsize=12, fontweight='bold')

plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Fruit Type', fontsize=12)
plt.title('Horizontal Bar Chart: Fruit Distribution', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('bar_chart_horizontal.png', dpi=150)
print("Chart 2 saved: bar_chart_horizontal.png")
plt.close()

# =============================================================================
# BAR CHART 3: With Percentage Labels
# =============================================================================
frequency_table['Percentage'] = (frequency_table['Count'] / frequency_table['Count'].sum() * 100).round(1)

plt.figure(figsize=(10, 6))

bars = plt.bar(frequency_table['Fruits'], frequency_table['Count'],
               color='steelblue', edgecolor='black', linewidth=1.2)

# Add count and percentage labels
for i, (count, pct) in enumerate(zip(frequency_table['Count'], frequency_table['Percentage'])):
    plt.text(i, count + 0.3, f'{count}\n({pct}%)', ha='center', fontsize=11)

plt.xlabel('Fruit Type', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Bar Chart with Percentages', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('bar_chart_with_percentage.png', dpi=150)
print("Chart 3 saved: bar_chart_with_percentage.png")
plt.close()

print("\n✅ All bar charts saved!")
