def adigits(n0, n1, n2):
    ns = [n0, n1, n2]
    n = 0
    
    m = max(ns)
    ns.remove(m)
    n += m*100
    
    m = max(ns)
    ns.remove(m)
    n += m*10 + ns[0]
    
    return n