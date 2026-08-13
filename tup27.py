#27.	Merge two tuples and remove duplicate elements.

tup1 = (1, 2, 3, 4, 5)
tup2 = (4, 5, 6, 7, 8)

merged_tuple = tuple(set(tup1 + tup2))

print("Tuple 1:", tup1)
print("Tuple 2:", tup2)
print("Merged tuple without duplicates:", merged_tuple)
