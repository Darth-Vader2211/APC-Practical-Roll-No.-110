with open("hello.txt", 'r') as file:
    content = file.read()
    print("Content of student.txt:", content)
    reversed_content = content[::-1]
    print("Reversed content of student.txt:", reversed_content)