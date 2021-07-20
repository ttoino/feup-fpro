def flatten(l):
    if type(l) != list:
        return [l]

    if len(l) == 1:
        return flatten(l[0])

    if len(l) > 1:
        return flatten(l[0]) + flatten(l[1:])

    return l