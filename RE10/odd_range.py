def odd_range(start, stop, step):
    yield from range(start if start % 2 == 1 else start+1, stop, step*2)
