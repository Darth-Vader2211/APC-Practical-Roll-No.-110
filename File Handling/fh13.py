with open("hello.txt", 'r') as file:
    words = file.readlines()

    word_count = 0
    line_numbers = []

    search_word = input("Enter the word to search: ")

    line_count = 0

    for line in words:
        line_count += 1
        word_list = line.split()

        if search_word in word_list:
            line_numbers.append(line_count)
            word_count += word_list.count(search_word)

    print("Total occurrences of", search_word, "in hello.txt:", word_count)
    print("Word found on line(s):", line_numbers)