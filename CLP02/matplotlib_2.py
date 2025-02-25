import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('data/apple_sales_2024.csv')

# Calculate mean iPhone sales for each region
regional_sales = data.groupby('Region')['Mac Sales (in million units)'].mean()

# Create bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(regional_sales.index, regional_sales.values)

# Customize the chart
plt.title('Average Mac Sales by Region', fontsize=14, pad=20)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average Mac Sales (Million Units)', fontsize=12)

# Set y-axis limits
plt.ylim(5, 6)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}M',
             ha='center', va='bottom')

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
