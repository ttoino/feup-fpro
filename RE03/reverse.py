num = int(input())

out = 0

while num > 0:
    temp = num % 10
    num //= 10
    
    out *= 10
    out += temp

print(out)