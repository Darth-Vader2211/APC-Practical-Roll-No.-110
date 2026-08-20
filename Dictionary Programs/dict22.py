#22.	Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

even_squares = {num: num**2 for num in range(1, 21) if num % 2 == 0}

print("Even numbers and their squares (1 to 20):")
print(even_squares)
