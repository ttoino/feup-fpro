def fib(n):
    if n == 1:
        return [0]

    r = [0, 1]
    while len(r) < n:
        r.append(r[-1] + r[-2])
    return r