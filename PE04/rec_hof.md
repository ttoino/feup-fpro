# 5. Process  commands

Write a Python function `rec_hof(hofs, lst)` that recursively applies a list of higher-order functions `hofs` to a nested list `lst`. Each element of `hofs` is a tuple with a "function operation" (for example, `map`) and a "function argument" (for example, a lambda function).


For example, the list `hofs=[(map, sum), (filter, lambda x: x>0)]` applied to `lst=[[-1, 2],[2, 3]]` should return `[2, 5]`, by applying the `filter` with the lambda to the sub-lists (resulting in `[[2],[2, 3]]`) and then the `map` of function `sum` to the top-list.


Inputs are assumed to be always valid.



## Private Tests [75%]

## Public Tests [100%]
