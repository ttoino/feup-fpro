# 5. No more conjunctions

Logical conjunctions (i.e., `and` / `or`) have been declared illegal!


Please rewrite the following code without using them:



```
a = int(input())
b = int(input())
count = 0
for i in range(a, b):
    if (((i % 3 == 0 and i % 5 == 0) or i % 11 == 0) and i % 7 == 0) or (i+a > b and i % 2 != 1):
        count += 1
    else:
        count -= 1
print(count)

```


## Private Tests [100%]

## Public Tests [100%]
