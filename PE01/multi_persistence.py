num = input()

result = 0

while len(num) > 1:
    result += 1
    inum = 1
    for d in num:
        inum *= int(d)
    num = str(inum)

print(result)