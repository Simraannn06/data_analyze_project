
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('shopping_data.csv')

# Handle missing values
data.fillna(0, inplace=True)

# Analyze top-performing products
top_products = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

# Analyze sales trends over time
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Handle date parsing errors
sales_trend = data.groupby(data['Date'].dt.to_period('M')).sum()['Revenue']

# Identify popular categories
popular_categories = data.groupby('Category')['Revenue'].sum().sort_values(ascending=False)

# Analyze average revenue per transaction
avg_revenue = data['Revenue'].mean()

# Plotting results
plt.figure(figsize=(12, 8))

# Plot top products
plt.subplot(2, 1, 1)
top_products.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Products by Revenue')
plt.ylabel('Revenue')

# Plot sales trends
plt.subplot(2, 1, 2)
sales_trend.plot(kind='line', marker='o', color='orange')
plt.title('Sales Trend Over Time')
plt.ylabel('Revenue')
plt.xlabel('Month')

plt.tight_layout()
plt.show()

