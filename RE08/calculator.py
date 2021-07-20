from operator import add, mul, sub

def calculator(a):
    if type(a) == int:
        return a

    return {
        "+": add,
        "-": sub,
        "*": mul
    }[a[1]](calculator(a[0]), calculator(a[2]))