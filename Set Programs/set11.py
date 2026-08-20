#11.	Create two sets and find:
#	•	Elements present in the first set but not the second 
#	•	Elements present in the second set but not the first

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

diff1 = set1 - set2
diff2 = set2 - set1

print("Set 1:", set1)
print("Set 2:", set2)
print("Elements in Set 1 but not in Set 2:", diff1)
print("Elements in Set 2 but not in Set 1:", diff2)
