with open("student.txt", 'r') as file:
    count = 0
    while file.readline():
        count += 1
    print("Total number of lines in student.txt:", count)