from functools import reduce

def nested_fmr(f, m, r, l):
    for i, v in enumerate(l):
        if type(v) == list:
            l[i] = nested_fmr(f, m, r, v)
            
    return reduce(r, map(m, filter(f, l)))