def bisect(f, n):
    limits = (0, 1)
    midpoint = 0
    for _ in range(n):
        midpoint = limits[0] + (limits[1] - limits[0])/2
        if f(limits[0])*f(midpoint) < 0:
            limits = limits[0], midpoint
        else:
            limits = midpoint, limits[1]

    return round(midpoint, 5)