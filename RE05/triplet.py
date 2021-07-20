from itertools import combinations


def triplet(t):
    for i in combinations(t, 3):
        if sum(i) == 0:
            return tuple(i)

    return ()