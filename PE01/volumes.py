from math import pi

kind = input()
r = float(input())

area = 0

if kind == "sphere":
    area = 4 * pi * r**3 / 3
elif kind == "cylinder":
    h = float(input())
    
    area = pi * r**2 * h
elif kind == "cone":
    h = float(input())
    
    area = pi * r**2 * h / 3
    
print(round(area, 1))