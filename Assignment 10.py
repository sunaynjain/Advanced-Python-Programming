import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("Sliced Array:", arr[2:7])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr * 2

print("After Broadcasting:", arr)
