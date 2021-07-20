# Juggler Sequence

Write a recursive Python function `juggler(n, p)` that, given two integers `n` and `p`, calculates the `p`-th term in the juggler sequence for `n`. The juggler sequence for a non-negative integer `n` is defined as follows:


* juggler(n, 0) = n
* juggler(n, p) = ⌊juggler(n, p-1)1/2⌋, if juggler(n, p-1) is even
* juggler(n, p) = ⌊juggler(n, p-1)3/2⌋, if juggler(n, p-1) is odd



## Private Tests [100%]

## Public Tests [100%]
