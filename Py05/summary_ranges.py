def summary_ranges(s):
    s = list(map(int, s.split(",")))

    start = s[0]
    intervals = []

    for i in range(len(s) - 1):
        x = s[i]
        y = s[i+1]

        if x != y-1:
            intervals.append((start, x))
            start = y
    else:
        intervals.append((start, s[len(s)-1]))

    return ",".join(map(lambda x: str(x[0]) if x[0] == x[1] else f"{x[0]}->{x[1]}", intervals))