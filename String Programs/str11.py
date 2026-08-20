s1 = input("Enter a String: ")
word_count = 0
for i in s1:
    if i == " ":
        word_count += 1
print("Number of words in the string: ", word_count + 1)