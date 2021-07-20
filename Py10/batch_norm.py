from statistics import median

def batch_norm(l, size):
    for i in range(0, len(l), size):
        batch = l[i:i+size]
        m = median(batch)
        yield [i-m for i in batch]