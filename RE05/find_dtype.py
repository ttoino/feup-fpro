def find_dtype(t, dt):
    l = list(t)

    for i in t:
        if type(i) != dt:
            l.remove(i)

    return tuple(l)