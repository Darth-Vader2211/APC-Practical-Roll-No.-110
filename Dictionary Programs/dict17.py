#17.	Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 20, "c": 30, "e": 50}

common_keys = dict1.keys() & dict2.keys()

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Common keys:", list(common_keys))
