#26.	Create two tuples and find the common elements between them.

tup1 = (10, 20, 30, 40, 50)
tup2 = (30, 40, 50, 60, 70)

common_elements = tuple(set(tup1) & set(tup2))

print("Tuple 1:", tup1)
print("Tuple 2:", tup2)
print("Common elements:", common_elements)
