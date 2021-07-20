a = int(input())
b = int(input())

i = a
while i < b:
    n = i

    if i**2 > (b/2)**2:
        i = b

    if not(i**2 > (b/2)**2 or (i % 3 == 0 and i % 5 == 0)):
        if i % 2 == 0:
            n //= 2
            n //= 2
            n //= 2

        if not(i % 2 == 0):
            n += 1

        print(n)
    
    i += 3