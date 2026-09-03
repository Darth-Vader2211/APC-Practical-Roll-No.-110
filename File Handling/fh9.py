with open("hello.txt", 'r') as file:
    content = file.read()
    vowels = "aeiouAEIOU"
    count = 0
    for c in content:
        if c in vowels:
            count += 1
    print("Total number of vowels in hello.txt:", count)