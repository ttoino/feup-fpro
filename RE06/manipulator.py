def manipulator(l, cmds):
    r = []

    commands = {
        "insert": lambda x, y: x.insert(int(y[1]), int(y[2])),
        "print": lambda x, y: r.append(str(x)),
        "remove": lambda x, y: x.remove(int(y[1])),
        "append": lambda x, y: x.append(int(y[1])),
        "sort": lambda x, y: x.sort(),
        "pop": lambda x, y: x.pop(),
        "reverse": lambda x, y: x.reverse()
    }

    for c in cmds:
        c = c.split()
        commands[c[0]](l, c)

    return " ".join(r)