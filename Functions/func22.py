def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n

    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, avg = calculate(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", avg)