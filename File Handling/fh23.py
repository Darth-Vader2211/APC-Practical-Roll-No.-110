file1 = open("attendance.txt", "r")
file2 = open("student.txt", "r")

line_number = 1
different = False

while True:

    line1 = file1.readline()
    line2 = file2.readline()

    if line1 == "" and line2 == "":
        break

    if line1 != line2:
        print("Files are different.")
        print("First difference occurs at line:", line_number)
        different = True
        break

    line_number += 1

file1.close()
file2.close()

if not different:
    print("Files are identical.")