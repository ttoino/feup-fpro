from math import ceil


def is_prime(num):
    if (num == 2):
        return True

    elif (num % 2 != 0 and num > 2):
        for i in range(3, ceil(num**.5) + 1, 2):
            if (num % i == 0):
                return False

    else:
        return False

    return True


lower = int(input())
upper = int(input())
primes = ""

for i in range(lower, upper + 1):
    if (is_prime(i)):
        primes += " " + str(i)

print(f"Prime numbers between {lower} and {upper} are:{primes}")