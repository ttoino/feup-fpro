from collections import deque

def last_man_standing(l, s):
    if type(l) is list:
        l = deque(l)
    if len(l) == 1:
        return l.pop()

    l.rotate(-s)
    l.pop()
    return last_man_standing(l, s)
