def gcd_rec(a, b):
    return a if b == 0 else gcd_rec(b, a % b)