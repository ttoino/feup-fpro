def dot(m, n):
    r = 0
    for i in range(len(m)):
        r += m[i]*n[i]

    return r


def column_vector(n, i):
    return [m[i] for m in n]


def mult(m, n):
    if len(m[0]) != len(n):
        return []

    r = []
    for i in range(len(m)):
        s = []
        r.append(s)
        for j in range(len(n[0])):
            s.append(dot(m[i], column_vector(n, j)))

    return r


def transpose(n):
    return [column_vector(n, i) for i in range(len(n))]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def is_orthogonal(n):
    return mult(n, transpose(n)) == identity(len(n))
