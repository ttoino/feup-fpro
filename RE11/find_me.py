def find_me(f, limits):
    i = 1
    index = limits[0] + (limits[1] - limits[0])//2
    while True:
        k = f(index)
        if k == 0:
            return i
        elif k == 1:
            limits = (index, limits[1])
        elif k == -1:
            limits = (limits[0], index)

        index = limits[0] + (limits[1] - limits[0])//2

        i += 1