"""Load a CSV file of sales data and compute
   total revenue per product."""
import pandas as pd

df = pd.read_csv('data.csv')
df['Total Revenue'] = df['Quantity Sold'] * df['Price per Unit']
total_revenue_per_product = df.groupby('Product')['Total Revenue'].sum()
print(total_revenue_per_product)
