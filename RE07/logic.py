def logic(s: set, operations: dict):
    for operation, other in operations.items():
        s = {
            "and": lambda s, o: s & o,
            "or": lambda s, o: s | o,
            "xor": lambda s, o: s ^ o,
            "not": lambda s, o: o - s,
        }[operation](s, other)

    return s