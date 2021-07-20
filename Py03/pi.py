from math import factorial, sqrt

s = 0
K = 50

for k in range(0, K + 1):
    s += (factorial(4*k) * (1103 + 26390 * k)) / (factorial(k)**4 * 396**(4*k))

inverse_pi = 2 * sqrt(2) * s / 9801

print(round(1/inverse_pi, 8))