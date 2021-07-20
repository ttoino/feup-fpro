def matches(s):
    ng = 0
    ns = 0
    prev = None
    for ss in s:
        if prev:
            ng += prev < ss
            ns += prev > ss
        prev = ss

    return ng == ns


def subpatterns(s):
    r = 0
    for i in range(len(s) - 2):
        for j in range(i + 3, len(s) + 1):
            r += matches(s[i:j])

    return f"The string '{s}' contains {r} substring patterns."