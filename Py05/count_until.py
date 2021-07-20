def count_until(tup):
    for i, j in enumerate(tup):
        if type(j) == tuple:
            return i

    return -1