#29.	Convert a tuple into a sorted tuple in ascending and descending order.

numbers = (42, 15, 88, 7, 31, 99, 23)

ascending_tuple = tuple(sorted(numbers))
descending_tuple = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Sorted in ascending order:", ascending_tuple)
print("Sorted in descending order:", descending_tuple)
