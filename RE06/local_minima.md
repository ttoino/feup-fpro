# 3. Find local minima

Given a list of integers `alist`, write a Python function `local_minima(alist, n)` that finds all the local minima on it, within a specified odd neighborhood `n`. The function should return a list with all (local minimum, index) pairs found in `alist`.


An element `alist[x]` is a local minimum if it is less than or equal to its neighbors. The number of neighbors of an element `alist[x]` depends on the neighborhood `n`. For example, if the neighborhood is 3, the element `alist[x]` has two neighbors: `alist[x-1]` and `alist[x+1]`. If `n=5`, `alist[x]` has four neighbors: `alist[x-2]`, `alist[x-1]`, `alist[x+1]` and `alist[x+2]`.


Note that for corner elements, you have to consider only the neighbours that lie within the list range (in one side only). Furthermore, if there are *adjacent* local minima (i.e., with the same value within the neighborhood range), you have to return just the local minima with the lowest index.



## Private Tests [50%]

## Public Tests [100%]
