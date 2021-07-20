def isomorphic(s1: str, s2: str):
    d = dict()
    for i, j in zip(s1, s2):
        if i in d:
            if d[i] == j:
                continue

            return f"'{s1}' and '{s2}' are not isomorphic"
        else:
            d[i] = j

    d1 = dict()
    for i, j in zip(s2, s1):
        if i in d1:
            if d1[i] == j:
                continue

            return f"'{s1}' and '{s2}' are not isomorphic"
        else:
            d1[i] = j

    return f"'{s1}' and '{s2}' are isomorphic because we can map: {list(d.items())}"