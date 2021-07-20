def interleave(f1, f2):
    return "".join(map("".join, zip(open(f1), open(f2))))