from functools import reduce


def flatten(t):
    if type(t) == tuple:
        for i in t:
            yield from flatten(i)
    else:
        yield t


def greatest_member(tup):
    if len(tup) == 0:
        return tup

    l = map(flatten, tup)
    l = list(map(lambda x: reduce(lambda z, y: z +
                                  reduce(lambda w, c: w + ord(c), y, 0), x, 0), l))
    return tup[l.index(max(l))]