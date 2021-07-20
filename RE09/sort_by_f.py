def sort_by_f(l):
    return sorted(l, key=lambda x: 5-x if x >= 5 else x)