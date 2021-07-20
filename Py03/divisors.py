num = int(input())

result = num

for i in range(1, num):
    if (num % i == 0):
        result += i

print(result)