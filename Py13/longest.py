def longest(file):
    return max(open(file).read().split(), key=len)
