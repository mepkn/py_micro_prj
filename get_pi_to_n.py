import math


def generate_pi(n: int) -> str:
    return str(math.pi)[: n + 2]


print(generate_pi(5))
