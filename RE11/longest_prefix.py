def prefix(w1, w2):
    for c1, c2 in zip(w1, w2):
        if c1 == c2:
            yield c1
        else:
            return

def longest_prefix(words):
    while len(words) != 1:
        words = ["".join(prefix(words[i], words[i+1])) for i in range(len(words)//2)]

    return words[0]