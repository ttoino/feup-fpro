def bagdiff(xs, ys):
    for y in ys:
        if y in xs:
            xs.remove(y)
    return xs