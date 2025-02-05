import numpy as np

# Generate 100 random values between 0 and 1
arr = np.random.rand(100)

# Print original array
print("Original array:")
print(arr)
print("\nOriginal array min:", np.min(arr))
print("Original array max:", np.max(arr))

# Normalize the array values between 0 and 1
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

# Print normalized array
print("\nNormalized array:")
print(normalized_arr)
print("\nNormalized array min:", np.min(normalized_arr))
print("Normalized array max:", np.max(normalized_arr))