# 2. Flowchart

Implement the following flowchart as a Python script:


xml version="1.0" encoding="UTF-8" standalone="no"?





flowchart



input

i = int(input())



c1

i % 2 ≠ 1



input->c1





c2

i % 7 = 0



c1->c2


no



print1

print(i²)



c1->print1


yes



c3

i % 11 = 0



c2->c3


yes



print2

print(i-2)



c2->print2


no



c4

i % 3 = 0



c3->c4


no



print3

print(3i+2)



c3->print3


yes



c5

i % 5 = 0



c4->c5


yes



print4

print(0)



c4->print4


no



print5

print(-i)



c5->print5


yes



print6

print(5-i)



c5->print6


no




## Private Tests [100%]

## Public Tests [100%]
