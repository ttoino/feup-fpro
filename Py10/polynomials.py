def evaluate(p, x):
    return sum(c*x**i for i, c in enumerate(p))
