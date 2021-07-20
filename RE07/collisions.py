from collections import Counter

def collisions(l):
    c = Counter()
    for i in l:
        c[sum(map(int, str(i))) % 8] += 1
    return c