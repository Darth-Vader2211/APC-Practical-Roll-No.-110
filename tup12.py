#12.	Accept five numbers from the user, store them in a list, and convert the list into a tuple.

numbers_list = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers_list.append(num)

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Converted Tuple:", numbers_tuple)
