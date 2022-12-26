def factorial(n: int) -> int:
    result = 1

    # iterate from 1 to n and multiply the result by i
    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))
