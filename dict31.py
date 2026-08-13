#31.	Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.

words = ["apple", "bat", "car", "elephant", "dog", "banana"]

by_length = {}
for word in words:
    length = len(word)
    if length not in by_length:
        by_length[length] = []
    by_length[length].append(word)

print("Words list:", words)
print("Grouped by length:", by_length)
