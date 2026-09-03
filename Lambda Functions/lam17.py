students = [
    ("Yash", 85),
    ("Rahul", 70),
    ("Amit", 92),
    ("Riya", 78)
]


def average_marks(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)


average = average_marks(students)

above_75 = list(filter(lambda student: student[1] > 75, students))

sorted_students = sorted(students, key=lambda student: student[1])

print("Average:", average)
print("Above 75:", above_75)
print("Sorted:", sorted_students)