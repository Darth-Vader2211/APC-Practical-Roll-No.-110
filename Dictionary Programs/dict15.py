#15.	Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence: ")
word_count = {}
words = sentence.split()
for word in words: 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)