#20.	Create a dictionary and display its elements in ascending order of keys.

data = {"banana": 3, "apple": 5, "cherry": 2, "date": 4}

sorted_keys = sorted(data.keys())

print("Elements in ascending order of keys:")
for key in sorted_keys:
    print(f"{key}: {data[key]}")
