def count_exceptions(f, n1, n2):
    r = 0
    for i in range(n1, n2+1):
        try:
            f(i)
        except:
            r += 1
    return r