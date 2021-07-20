def last_man_standing(l, n):
    i = 0
    while len(l) > 1:
        i += n-1
        i %= len(l)
        l.pop(i)
    return l[0]