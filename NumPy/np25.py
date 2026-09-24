import numpy as np

# Create a random 3D array
a = np.random.randint(1, 101, size=(3, 4, 5))

# Flatten the array
b = a.flatten()

# Calculate average
average = np.mean(b)

print("Original 3D Array:")
print(a)

print("\nFlattened Array:")
print(b)

print("\nElements greater than 50:")
print(b[b > 50])

print("\nEven numbers:")
print(b[b % 2 == 0])

print("\nAverage:", average)
print("Elements less than average:")
print(b[b < average])