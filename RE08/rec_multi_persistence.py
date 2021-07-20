from functools import reduce
from operator import mul

def rec_multiplicative_persistence(n):
    if n < 10:
        return 0
    return 1 + rec_multiplicative_persistence(reduce(mul, map(int, str(n))))
