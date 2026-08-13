#19.	Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

original_dict = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}

unique_dict = {}
for key, value in original_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print("Original dictionary:", original_dict)
print("Dictionary after removing duplicate values:", unique_dict)
