def order_digits(n):
    return tuple(sorted(map(int, str(n)), reverse=True))
