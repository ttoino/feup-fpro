def solver(a, b, c):
    # x = (-b +-sqrt(b^2 - 4ac))/2a

    delta = (b**2 - 4*a*c)**.5
    if (type(delta) == complex):
        return []

    results = {(-b+delta)/(2*a), (-b-delta)/(2*a)}
    return sorted(results)