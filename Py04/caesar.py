from math import sqrt


def caesar(message):
    result = ""

    for i in range(len(message)):
        c = message[i]

        if not c.isalpha():
            result += c
            continue

        f = ((1 + sqrt(5))**i - (1 - sqrt(5))**i)//(2**i * sqrt(5))

        n = ord(c) - 65 - f

        c = chr(int(n % 26 + 65))
        result += c

    return result