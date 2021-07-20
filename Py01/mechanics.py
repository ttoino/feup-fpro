import math
angle = int(input())*math.pi/180  # convert to radians

v = 18
g = 10

d = v**2 * math.sin(2*angle) / g

print(round(d))