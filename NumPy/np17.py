import numpy as np

marks = np.array([65, 78, 89, 92, 56, 74, 81, 95, 68, 87,
                  72, 91, 63, 85, 77, 88, 54, 96, 70, 83])

average = np.mean(marks)

print("Class average:", average)
print("Students scoring above average:")
print(marks[marks > average])