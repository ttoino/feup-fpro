num = int(input())

result = num + 1

for i in range(2, num//2+1):
    if num % i == 0:
        result += i

print(result)