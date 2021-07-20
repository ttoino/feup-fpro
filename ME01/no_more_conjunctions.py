a = int(input())
b = int(input())
count = 0
for i in range(a, b):
    if i % 105 == 0:
        count += 1
    elif i % 77 == 0:
        count += 1
    elif i+a > b:
        if i % 2 == 0:
            count += 1
        else:
            count -= 1
    else:
        count -= 1
print(count)