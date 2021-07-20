import math


def digits_average(n):
    while (n//10 > 0):
        temp = n
        n = 0
        while (temp//10 > 0):
            n1 = temp % 10
            temp //= 10
            n2 = temp % 10

            average = math.ceil((n1+n2)/2)
            n += average * 10**int(math.log(temp, 10))

    return n