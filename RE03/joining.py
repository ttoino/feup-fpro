n1 = int(input())
n2 = int(input())

result = n1
temp = n2

while (temp > 0):
    temp //= 10
    result *= 10

result += n2

print(result)