# 4. Nested filter/map/reduce

Write a Python function `nested_fmr(f, m, r, lst)` that, given 3 functions `f`, `m` and `r`, recursively applies the filter `f`, followed by the map `m`, followed by the reduce `r` on every sublist of the nested list last.


For example with `f = lambda x: x < 10`,   `m = lambda x: abs(x)`   and   `r = lambda x, y: x + y` and the nested list `[[4, -20],[15, -1], -4, 3]`, the function should return `8`, with the intermediary step `[24, 1, -4, 3]`, after applying filter/map/reduce to the nested list.



## Private Tests [100%]

## Public Tests [100%]
