with open("student.txt",'r') as file:
    count = 0
    content = file.read()
    for words in content:
        if words == " ":
            count += 1
    print("Total number of words in student.txt:", count)