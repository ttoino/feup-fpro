# Generator from an interval list

An interval list is a list of tuples that represent intervals. Each tuple represents an interval in the form (min, max). Tuples appear in increasing order in the list and the intervals are disjoint.


For example, the list of intervals `intlist=[(1,1), (3,5), (10,15)]` represents the full sequence `1, 3, 4, 5, 10, 11, 12, 13, 14, 15`.


Write a generator function `generator(intlist)` that iteratively yields the next term in the full sequence, encoded in the list `intlist`.



## Private Tests [100%]

## Public Tests [100%]
