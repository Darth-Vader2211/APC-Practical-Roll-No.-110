file1 = open("attendance.txt", "r")
file2 = open("student.txt", "r")
file3 = open("combined.txt", "w")

content1 = file1.read()
content2 = file2.read()

file3.write(content1)
file3.write("\n")
file3.write(content2)

file1.close()
file2.close()
file3.close()

print("Files combined successfully.")