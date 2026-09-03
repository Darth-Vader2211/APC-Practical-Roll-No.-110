with open("hello.txt", "r") as file:
    content = file.read()
    longest_word = ""
    words = content.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print("Longest word :", longest_word)