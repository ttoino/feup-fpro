from collections import Counter

def most_frequent(l):
    l.sort(reverse=True)
    c = Counter()
    for i in l:
        c[i] += 1
    return c.most_common()[0][0]