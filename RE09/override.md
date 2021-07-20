# 4. Override operation

Write a function `override(l1, l2)` that, given two lists of tuples, performs the operation `l1 ++ l2` known as *override*. The *override* operation, given two lists of tuples, produces a new list with every member of `l2` and every member of `l1` that is not overridden by an element from `l2` (i.e., does not begin with the same atomic element). For example,



```
[(a,b), (c,d), (c, e)] ++ [(a,c), (b,d)] = [(a,c), (b,d), (c,d), (c,e)]

```

Note that `(a,b)` from the first list was overridden by `(a,c)` from the second list and all other elements were maintained.


The resulting list should be ordered by the first element of each tuple.



## Private Tests [100%]

## Public Tests [100%]
