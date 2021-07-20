from itertools import combinations

def groups(students):
    return tuple(combinations(students, 3))