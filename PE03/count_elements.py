from collections import Counter

def rec_count(l, d=Counter()):
    if type(l) is list:
        for i in l:
            rec_count(i, d)
            
    else:
        d[l] += 1
    
    return d