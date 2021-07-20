def local_minima(l, n):
    r = []
    last_minimum = (l[0], 0)

    for x, v in enumerate(l):
        # neighborhood = l[max(x - n//2, 0):x]
        # if last_minimum[0] in neighborhood:
        #     continue
        if x >= n//2+1 and last_minimum[0] == l[x - n//2 - 1]:
            r.append(last_minimum)
            last_minimum = (v, x)
        # or last_minimum[0] == l[max(x - n//2 - 1, 0)]:
        if v < last_minimum[0]:
            last_minimum = (v, x)

    r.append(last_minimum)

    return r