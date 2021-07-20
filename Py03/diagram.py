l = int(input())
s = int(input())
r = l

if (r <= s):
    l = r
    r = s
    s = l

while (True):
    if (s <= r):
        r -= s
        continue

    if (r == 0):
        print(s)
        break

    l = r
    r = s
    s = l