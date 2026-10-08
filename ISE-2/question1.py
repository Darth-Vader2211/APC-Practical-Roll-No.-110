n = int(input("Enter no. of students:"))
marks = []
for i in range(n):
    mark = int(input("Enter marks of students :"))
    marks.append(mark)
maximum = max(marks)
minimum = min(marks)
average = sum(marks) / n

above_avg = 0

for i in marks:
    if i > average:
        above_avg += 1
    else:
        break

print("Maximum marks = ",maximum)
print("Minimum marks = ",minimum)
print("Average marks = ",average)
print("Student with marks above average:",above_avg)