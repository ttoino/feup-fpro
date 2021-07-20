from math import floor

def juggler(n, p):
    if p == 0:
        return n
    
    next = juggler(n, p-1)
    return floor(next**(.5 if next % 2 == 0 else 1.5))