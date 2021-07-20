from math import factorial


def pascal(n):
    result = ""

    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(f"{factorial(i)/(factorial(j)*factorial(i-j)):1.0f}")

        result += " ".join(row) + "\n"

    return result