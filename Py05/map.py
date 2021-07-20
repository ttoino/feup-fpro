def map(pos, steps):
    for i in steps.split("-"):
        step = (-1, 0) if i == "left" else (1, 0) if i == "right" else (0, 1) if i == "up" else (0, -1)
        pos = (pos[0] + step[0], pos[1] + step[1])

    return pos