# 4. Overlap segments

Write a Python function `overlaps(segments)` that receives a list of `segments`, where each segment is represented by a tuple `(start, end)`, containing the start and end points of the segment, and returns a **set of tuples** with the indices of the overlapping segments.


For example, in this illustration,



```

0:  +---+---+---+
1:          +---+---+
2:                      +---+
3:                                  +
4:                                  +---+
    0---1---2---3---4---5---6---7---8---9

```

`overlaps([(0, 3), (2, 4), (5, 6), (8, 8), (8, 9)])`, the function should return `{(0, 1), (3, 4)}`.



## Private Tests [100%]

## Public Tests [100%]
