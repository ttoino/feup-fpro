def generator(il):
    for start, end in il:
        yield from range(start, end+1)
