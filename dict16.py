#16.	Create two dictionaries and merge them into a single dictionary.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = d1 | d2
print("Merged dictionary:", d3)