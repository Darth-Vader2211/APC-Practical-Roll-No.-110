import numpy as np

a = np.array([10, 65, 30, 75, 45, 90, 25, 55, 40, 80])

print("Original array:")
print(a)

a[a > 50] = 0

print("After replacing values greater than 50:")
print(a)