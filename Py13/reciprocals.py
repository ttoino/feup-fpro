def reciprocals(l):
    r = []
    for i in l:
        try:
            r.append(1/i)
        except:
            pass
    return r