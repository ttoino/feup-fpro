# 1. Sparse dot product

A *sparse vector* is a vector whose entries are almost all zero, e.g., [0, 1, 0, 0, 0, 0, 0, 0, 2, 0]. For memory efficiency, sparse vectors can be represented as dictionaries with keys representing the indices of non-zero values, and then the value of a key corresponds to the value of the vector at that index. For example, the vector [0, 1, 0, 0, 2] can be stored as the dictionary {1: 1, 4: 2}.


Write a Python function `sparse_dot_product(dict1, dict2)` that computes the inner product of two sparse vectors, `dict1` and `dict2`, represented as dictionaries.



## Private Tests [100%]

## Public Tests [100%]
