#20.	Accept a number from the user and determine whether it exists in the tuple.

numbers = (10, 25, 30, 45, 50, 65, 70)
search_num = int(input("Enter a number to search: "))

if search_num in numbers:
    print(f"Number {search_num} exists in the tuple.")
else:
    print(f"Number {search_num} does not exist in the tuple.")
