def roman_to_integer(s: str):
    roman_to_decimal = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }

    acc = 0
    for k, v in roman_to_decimal.items():
        while k in s:
            acc += v
            index = s.index(k)
            if index != 0:
                for i in s[:index]:
                    acc -= roman_to_decimal[i]

            s = s[index + 1:]

    return acc