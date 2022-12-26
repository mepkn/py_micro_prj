def spell_out_number(n: int) -> str:
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    # if the number is in the dictionary return the corresponding english word
    if n in numbers:
        return numbers[n]

    # check if the number is between 21 and 99
    elif n > 20 and n < 100:
        tens = n // 10
        ones = n % 10
        return f"{numbers[tens * 10]} {numbers[ones]}"

    # check if the number is between 100 and 999
    elif n >= 100 and n < 1000:
        hundreds = n // 100
        tens = (n // 10) % 10
        ones = n % 10
        return f"{numbers[hundreds]} hundred {numbers[tens * 10]} {numbers[ones]}"

    else:
        return "Number out of range"


print(spell_out_number(459))
