d = int(input())
num = input()

result = 0

for digit in num:
    digit = int(digit)
    if digit > d:
        result += digit**2

print(result)