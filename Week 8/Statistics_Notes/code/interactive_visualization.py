"""
Interactive Visualization with Plotly
======================================
This script demonstrates interactive bar charts for frequency tables.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

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

# Add percentage
frequency_table['Percentage'] = (frequency_table['Count'] / frequency_table['Count'].sum() * 100).round(2)

print("Frequency Table:")
print(frequency_table)

# =============================================================================
# CHART 1: Simple Interactive Bar Chart
# =============================================================================
fig1 = px.bar(
    frequency_table,
    x='Fruits',
    y='Count',
    color='Fruits',
    title='🍎 Fruit Distribution (Interactive!)',
    text='Count',
    hover_data={'Percentage': True, 'Count': True}
)

fig1.update_traces(textposition='outside')
fig1.update_layout(
    xaxis_title='Fruit Type',
    yaxis_title='Frequency',
    showlegend=False
)
fig1.write_html('interactive_bar_chart.html')
print("\nChart 1 saved: interactive_bar_chart.html")

# =============================================================================
# CHART 2: Pie Chart (Interactive)
# =============================================================================
fig2 = px.pie(
    frequency_table,
    values='Count',
    names='Fruits',
    title='🥧 Fruit Distribution (Pie Chart)',
    hole=0.3  # Makes it a donut chart
)

fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.write_html('interactive_pie_chart.html')
print("Chart 2 saved: interactive_pie_chart.html")

# =============================================================================
# CHART 3: Horizontal Bar Chart with Cumulative Line
# =============================================================================
frequency_table['Cumulative'] = frequency_table['Count'].cumsum()
frequency_table['Cumulative Percentage'] = (frequency_table['Cumulative'] / frequency_table['Count'].sum() * 100).round(2)

fig3 = go.Figure()

# Add bar chart
fig3.add_trace(go.Bar(
    x=frequency_table['Count'],
    y=frequency_table['Fruits'],
    orientation='h',
    name='Count',
    text=frequency_table['Count'],
    textposition='outside',
    marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
))

fig3.update_layout(
    title='📊 Horizontal Bar Chart',
    xaxis_title='Count',
    yaxis_title='Fruit',
    showlegend=False
)
fig3.write_html('interactive_horizontal_bar.html')
print("Chart 3 saved: interactive_horizontal_bar.html")

print("\n✅ All charts saved! Open the HTML files in your browser.")
print("You can hover, zoom, and interact with the charts!")
