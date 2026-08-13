#13.	Modify a tuple by converting it into a list and then back into a tuple.

original_tuple = ("Yash", "Prithvi", "Harsh")
temp_list = list(original_tuple)

temp_list.append("Ankit")
temp_list[0] = "Yash Joshi"

modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Modified tuple:", modified_tuple)
