from functools import reduce

def reduce_map_filter(args):
    if type(args) is list:
        return args

    r = {
        "map": map,
        "filter": filter,
        "reduce": reduce
    }[args[0]](args[1], reduce_map_filter(args[2]))

    return r if type(r) is int else list(r)