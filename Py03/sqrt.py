n = int(input())

minimum = 0
maximum = n
midpoint = (maximum - minimum)/2 + minimum

while (maximum - minimum >= 0.00001):
    if (midpoint*midpoint > n):
        maximum = midpoint
    else:
        minimum = midpoint
    
    midpoint = (maximum - minimum)/2 + minimum

print(round(midpoint, 5))