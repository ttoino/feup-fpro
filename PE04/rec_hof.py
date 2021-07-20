def rec_hof(hofs, lst):
    if type(lst) != list:
        return lst
    for i, l in enumerate(lst):
        lst[i] = rec_hof(hofs[1:], l)
    f, op = hofs[0]
    return f(op, lst)