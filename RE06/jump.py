def jump(l):
    index = l[0]
    count = 0
    while index != -1:
        index = l[index]
        count += 1
    return count