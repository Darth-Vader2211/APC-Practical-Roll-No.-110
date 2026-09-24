from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter text: ")

text = remove_punctuation(text)
text = remove_extra_spaces(text)

words = tokenize(text)

frequency = word_frequency(words)

print("\nCleaned Text:", text)
print("Tokens:", words)
print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)