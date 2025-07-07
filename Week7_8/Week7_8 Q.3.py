import numpy as np

# Create, sort, and reshape the array
arr = np.sort(np.random.randint(1, 101, 10))

print("Sorted Array:", arr)
print("2x5 Matrix:\n", arr.reshape(2, 5))
print("5x2 Matrix:\n", arr.reshape(5, 2))
