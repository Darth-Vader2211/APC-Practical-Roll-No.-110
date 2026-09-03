words = ["apple", "computer", "cat", "python", "programming"]

result = list(filter(lambda word: len(word) > 5, words))

print(result)