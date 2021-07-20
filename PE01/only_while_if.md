# 5. Only while and if

The upcoming Python XP is a new cleaned-up version and many flow control statements have been removed.


Modify the following code so that only `while` and `if` are used as flow control (i.e., you cannot use `for`, `elif`, `else`, `continue` or `break`).



```
a = int(input())
b = int(input())

for i in range(a, b, 3):
    n = i
    if i**2 > (b/2)**2:
        break
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 2 == 0:
        for _ in range(3):
            n //= 2
    else:
        n += 1
    print(n)

```


## Private Tests [100%]

## Public Tests [100%]
