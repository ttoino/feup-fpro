def binary_tree(key, tree):
    k, v, l, r = tree

    if key > k:
        return binary_tree(key, r())
    elif key < k:
        return binary_tree(key, l())
    else:
        return v