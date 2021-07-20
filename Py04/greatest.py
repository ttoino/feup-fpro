def greatest(num):
    digits = list(str(num))
    digits.sort(reverse=True)
    return int("".join(digits))