from functools import reduce

def map_filter_reduce(l, f1, f2, f3):
    return reduce(f3, map(f2, filter(f1, l)))