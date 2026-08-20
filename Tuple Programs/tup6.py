#6.	Create a tuple with repeated numbers and count how many times a particular number appears.

numbers = (10, 20, 10, 30, 10, 40, 20, 50, 10)
target = 10
count_target = numbers.count(target)

print("Tuple:", numbers)
print(f"Number {target} appears {count_target} times in the tuple.")
