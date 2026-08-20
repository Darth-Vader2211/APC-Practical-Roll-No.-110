'''13.	Shortest Word 
a.	Find the shortest word in a sentence. 
'''
str1 = input("Enter a sentence:").split()
shortest_word = min(str1, key=len)
print("Shortest word in the sentence is:", shortest_word)