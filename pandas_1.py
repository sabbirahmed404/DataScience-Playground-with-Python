import pandas as pd

df = pd.read_csv('data/Furniture.csv')

revenue_by_product = df.groupby('category').agg({
    'revenue': 'sum',
    'sales': 'sum',
}).round(2)

print("\nDetailed Summary by Product Category:")
print(revenue_by_product)

print(df[df.isnull()])