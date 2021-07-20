def diff(n1, n2):
    if (n1 == 9 and n2 == 0) or (n1 == 0 and n2 == 9):
        return 1

    return abs(n1 - n2)


def is_looping(num):
    for i in range(len(num) - 1):
        n1 = int(num[i])
        n2 = int(num[i + 1])
        if (diff(n1, n2) != 1):
            return False

    return True


num = input()
print("Looping number" if is_looping(num) else "Not a looping number")