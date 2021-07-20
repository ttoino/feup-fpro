def bubble_sort(l):
    s = True
    while s:
        s = False
        for i in range(len(l) - 1):
            x, y = l[i], l[i+1]
            if x > y:
                l[i], l[i+1] = y, x
                s = True
    return l