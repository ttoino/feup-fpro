num = float(input())

x0 = 0.001
x1 = (x0 + num/x0)/2

while (abs(x1 - x0) >= 0.01):
    x0 = x1
    x1 = (x0 + num/x0)/2

print(round(x1, 2))