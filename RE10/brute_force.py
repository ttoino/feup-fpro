def brute_force(f, l):
    return [s for s in [i + j + k for i in l for j in l for k in l] if f(s)]