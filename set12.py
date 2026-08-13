#12.	Create two sets of numbers and find the elements that are present in either set but not in both.

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

sym_diff = set1.symmetric_difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Elements present in either set but not in both (Symmetric Difference):", sym_diff)
