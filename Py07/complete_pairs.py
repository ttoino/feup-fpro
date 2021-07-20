def complete_pairs(s1: set, s2: set):
    return {i + j for i in s1 for j in s2 if len(set(i+j)) == 26}