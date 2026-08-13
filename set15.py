#15.	Write a program to determine whether two sets have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

are_disjoint = set1.isdisjoint(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Do the two sets have no elements in common?:", are_disjoint)
