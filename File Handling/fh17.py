file = open("student1.txt", "r")

students = []

file.readline()  # Skip header

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append([int(roll), name, int(marks)])

file.close()

# Display all records
print("All Student Records:")
for student in students:
    print(student[0], student[1], student[2])

# Highest marks
highest = max(students, key=lambda x: x[2])

print("\nHighest Marks:")
print(highest[1], "-", highest[2])

# Average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage Marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student[1], "-", student[2])