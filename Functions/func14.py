def count_occurrence(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count += 1

    return count

numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element: "))

print("Occurrences:", count_occurrence(numbers, element))