"""20. Count Occurrences of a Word 
a.	Count how many times a specific word appears in a sentence. """
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

count = sentence.split().count(word)

print("Occurrences:", count)