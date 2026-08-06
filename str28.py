"""28.	Word Frequency Dictionary 
•	Count the frequency of every word in a paragraph."""
text = input("Enter paragraph: ")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)