def nth_lowest(l, n):
    r = 0
    for i in range(n):
        r = min(l)
        l.remove(r)
    return r
