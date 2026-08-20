"""12.	Longest Word 
a.	Find the longest word in a given sentence. 
"""
s1 = input("Enter a String: ")
words = s1.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word in the string: ", longest_word)