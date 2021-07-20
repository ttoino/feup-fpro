def sparse_dot_product(v1, v2):
    acc = 0
    for i in v1.keys():
        if i in v2:
            acc += v1[i]*v2[i]
    return acc
