file = open("attendance.txt", "r")

students = []

for line in file:
    roll, name, present, total = line.strip().split(",")

    percentage = (int(present) / int(total)) * 100

    students.append([int(roll), name, percentage])

file.close()

print("Attendance Records:")

for student in students:
    print(student[0], student[1], student[2], "%")

print("\nStudents having attendance below 75%:")

for student in students:
    if student[2] < 75:
        print(student[1], "-", student[2], "%")