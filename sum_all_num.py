def sum_numbers(numbers: list) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_numbers([1, 2, 3, 4, 5]))
