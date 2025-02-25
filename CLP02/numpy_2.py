import numpy as np

arr = np.random.rand(100)

print("Original array:")
print(arr)
print("\nOriginal array min:", np.min(arr))
print("Original array max:", np.max(arr))

normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("\nNormalized array:")
print(normalized_arr)
print("\nNormalized array min:", np.min(normalized_arr))
print("Normalized array max:", np.max(normalized_arr))