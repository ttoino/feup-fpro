def pattern_hunting(l1, l2, p):
    r = []
    for s1, s2 in zip(l1, l2):
        if p in s1:
            r.append(s2)
        if p in s2:
            r.append(s1)

    return sorted(r, reverse=True)
