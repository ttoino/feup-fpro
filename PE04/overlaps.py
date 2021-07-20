from itertools import combinations

def overlaps(segments):
    r = set()
    d = dict()
    for i, (s, e) in enumerate(segments):
        for j in range(s, e+1):
            if j not in d:
                d[j] = []
            d[j].append(i)
    for v in d.values():
        r.update(combinations(v, 2))
    return r