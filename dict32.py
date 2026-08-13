#32.	Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15]
target = 9

seen = {}
pair = None

for num in numbers:
    complement = target - num
    if complement in seen:
        pair = (complement, num)
        break
    seen[num] = True

print(f"Numbers: {numbers}, Target: {target}")
if pair:
    print(f"Two numbers that sum to {target}: {pair[0]} and {pair[1]}")
else:
    print("No such pair found.")
