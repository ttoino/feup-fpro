# 4. Moving Average

Write a Python function `moving_average(alist, n)` that, given a list `alist` of integers and an odd integer `n` (representing the neighborhood span) returns a list with the averages of the neighborhood for each number, rounded to two decimal places. Note that each neighborhood span has exactly `n` elements.


If `alist` has length < 3 or if `n` < 3, then the result is the empty list.


For example:


* `a_list = [1, 2, 3, 4, 5]`, `n = 3` ⇒ `[(1+3)/2, (2+4)/2, (3+5)/2]` ⇒ `[2.0, 3.0, 4.0]`



## Private Tests [100%]

## Public Tests [100%]
