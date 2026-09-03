with open("hello.txt", 'r') as file:
    count = 0
    content = file.read()
    for char in content:
        if char:
            count += 1
    print("Total number of Characters in student.txt:", count)