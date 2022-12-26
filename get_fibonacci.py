def fibonacci(n: int) -> list:
    result = []
    a = 0
    b = 1
    while n > b:
        result.append(b)
        # a, b = b, a + b
        c = a + b
        a = b
        b = c
    return result


print(fibonacci(10))
