def evaluate(p, x):
    return sum(map(lambda c: c[1] * x**c[0], enumerate(p)))