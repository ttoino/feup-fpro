def days_until_empty(c, l):
    i = -1
    water = c

    while water > 0:
        i += 1
        water = min(water + l, c)
        water -= i

    return i