from collections import Counter

def sum_dicts(l):
    c = Counter()
    for d in l:
        for k, v in d.items():
            c[k] += v
    return c