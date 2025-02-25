import pandas as pd

# Read the CSV file
df = pd.read_csv('data/Furniture copy.csv')

# Print number of null values before filling
print("Null values before filling:")
print(df.isnull().sum())

# Calculate column-wise means for numeric columns only
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
column_means = df[numeric_cols].mean()

# Fill missing values with column means
df_filled = df.copy()
df_filled[numeric_cols] = df_filled[numeric_cols].fillna(column_means)

# Print number of null values after filling
print("\nNull values after filling:")
print(df_filled.isnull().sum())

# Save the filled dataset
df_filled.to_csv('data/Furniture_filled.csv', index=False)

# Print sample of rows that had null values to verify the filling
original_null_rows = df[df.isnull().any(axis=1)]
filled_null_rows = df_filled.loc[original_null_rows.index]
print("\nSample of filled rows (before and after):")
print("\nBefore filling:")
print(original_null_rows)
print("\nAfter filling:")
print(filled_null_rows)