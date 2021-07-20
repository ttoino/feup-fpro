from functools import reduce

def map_reduce(n1, n2):
    return reduce(lambda x, y: x*y if x*y < 50 else x + y, map(lambda x: x*x, filter(lambda x: x % 2 == 1, range(n1, n2))))