n = int(input())
s = ""

for i in range(n+1):
    if (i % 15 == 0):
        continue
    elif (i % 3 == 0):
        s += " Fizz"
    elif (i % 5 == 0):
        s += " Buzz"
    else:
        if (i != 1):
            s += " "
        s += str(i)

print(s)