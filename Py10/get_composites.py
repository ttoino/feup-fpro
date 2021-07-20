def get_composites(n):
    yield from {i for i in range(4, n+1) for j in range(2, i) if not i % j}
