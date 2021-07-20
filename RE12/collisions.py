from itertools import combinations

def number_of_collisions(l):
    n = 0
    for b1, b2 in combinations(l, 2):
        if b1["x1"] > b2["x2"] or b2["x1"] > b1["x2"] or b1["y1"] > b2["y2"] or b2["y1"] > b1["y2"]:
            continue
        n += 1
    return n