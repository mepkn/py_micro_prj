def is_palindrome(s: str) -> bool:
    # convert to lowercase and remove space
    s = s.lower().replace(" ", "")

    return s == s[::-1]


print(is_palindrome("racecar"))
