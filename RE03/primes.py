from math import ceil

num = int(input())
is_prime = True

if (num == 2):
    pass

elif (num % 2 != 0 and num > 2):
    for i in range(3, ceil(num**.5), 2):
        if (num % i == 0):
            is_prime = False
            break

else:
    is_prime = False

print(is_prime)