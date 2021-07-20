def comprehensions(i, j):
    return (
        [n for n in range(i, j+1) if str(n).endswith(("3", "8"))],
        tuple(round(n**.5, 2) for n in range(i, j+1)),
        {n: chr(n) for n in range(i, j+1)}
    )