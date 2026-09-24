import numpy as np

a = np.array([45, 12, 78, 23, 9, 56, 34])

print("Original array:")
print(a)

print("Ascending order:")
print(np.sort(a))

print("Descending order:")
print(np.sort(a)[::-1])