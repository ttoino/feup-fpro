from collections import Counter

def academy_awards(awards):
    c = Counter()
    for (_, movie) in awards:
        c[movie] += 1
    return c