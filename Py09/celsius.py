def to_celsius(t):
    return list(map(lambda t: round((t-32)*5/9, 1), t))