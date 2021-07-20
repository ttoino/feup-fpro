# 5. Sets Logic

Logic operations such as and/or/xor have set analogues. Implement these logic operands using sets.


Write a Python function called `logic(s, operations)` that applies a series of "logic" operations between sets. The `s` parameter is the original set before any operation is applied, and the `operations` parameter is a dictionary where the *keys* are the name of the binary logic operations and the *values* are the sets to be used for the binary operation.


The following operations must be supported: **and**, **or**, **xor** and **not**. Read [the set documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) to find the respective counterpart.


For example, if `s={1,2,3,4}` and `operations={'and': {3,4,5,6}}`, then the function should return `{3,4}`.


If the operation **not** is used (which is unary), then the domain will be given as the value. For example, if `s={1,2,3,4}` and `operations={'not': {0,1,2,3,4,5,6,7,8,9}}`, then the function should return `{0,5,6,7,8,9}`.



## Private Tests [100%]

## Public Tests [100%]
