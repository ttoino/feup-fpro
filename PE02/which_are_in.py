def which_are_in(l1, l2):
    r = set()
    for i in l1:
        for j in l2:
            if i in j:
                r.add(i)
                
    return sorted(r)