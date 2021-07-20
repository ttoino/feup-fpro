n = int(input())

result = []

for i in range(n):
    result.append(str(i)*i)

print("\n".join(result))