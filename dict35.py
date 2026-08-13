#35.	Accept a paragraph and create a dictionary where:
#	•	Key = word length 
#	•	Value = number of words having that length.

paragraph = input("Enter a paragraph: ")
words = paragraph.split()

length_count = {}
for word in words:
    clean_word = word.strip(".,!?;:\"'")
    if clean_word:
        length = len(clean_word)
        length_count[length] = length_count.get(length, 0) + 1

print("Word length count:", length_count)
