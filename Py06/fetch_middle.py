def fetch_middle(ll):
    r = []
    for l in ll:
        if len(l) % 2 == 0:
            r.append((l[len(l)//2] + l[len(l)//2-1])/2)
        else:
            r.append(l[len(l)//2])
    return r