def maximum_depth(l):
    return 1 + max(map(maximum_depth, l)) if l else 1