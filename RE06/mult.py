def dot(m, n):
    r = 0
    for i in range(len(m)):
        r += m[i]*n[i]

    return r


def mult(m, n):
    if len(m[0]) != len(n):
        return []

    r = []
    for i in range(len(m)):
        s = []
        r.append(s)
        for j in range(len(n[0])):
            c = [k[j] for k in n]
            s.append(dot(m[i], c))

    return r