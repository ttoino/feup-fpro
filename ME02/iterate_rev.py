def iterate_rev(names, numbers, emails):
    r = []

    for i in list(zip(names, numbers, emails))[::-1]:
        r.append(" - ".join(map(str, i)))

    return "\n".join(r)