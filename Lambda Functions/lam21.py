words = ["apple", "computer", "cat", "python", "programming", "dog"]


def word_lengths(words):
    return list(map(lambda word: len(word), words))


def long_words(words):
    return list(filter(lambda word: len(word) > 5, words))


def sort_words(words):
    return sorted(words, key=lambda word: len(word))


print("Lengths:", word_lengths(words))
print("Words with more than 5 characters:", long_words(words))
print("Sorted words:", sort_words(words))