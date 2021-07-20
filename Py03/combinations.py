def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)


def C(n, r):
    return round((factorial(n) / (factorial(r)*factorial(n-r)))//1)