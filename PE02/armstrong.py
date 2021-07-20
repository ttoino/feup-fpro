def is_armstrong(n):
    return sum(map(lambda x: int(x)**3, str(n))) == n