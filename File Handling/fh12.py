with open("hello.txt", "r") as file:
    count = 0
    content = file.read()
    word = content.split()
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print("Word Frequency in hello.txt:")
    for key, value in dict.items():
        print(f"{key}: {value}")