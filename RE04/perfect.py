def is_perfect(n):
    s = 1
    for i in range(2, int(n/2 + 1)):
        if (n % i == 0):
            s += i

    return s == n