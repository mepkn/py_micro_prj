def count_info(string: str) -> tuple:
    lines = 0
    words = 0
    vowels = 0
    consonants = 0

    lines_list = string.splitlines()
    for line in lines_list:
        lines += 1
        words_list = line.split()
        for word in words_list:
            for char in word:
                if char in "aeiouAEIOU":
                    vowels += 1
                else:
                    consonants += 1
        words += len(words_list)

    return lines, words, vowels, consonants


string = """This is a string
with multiple lines
and multiple words"""
print(count_info(string))
