# Sudoku

Write a Python function `solve_sudoku(board)` that, given an incomplete Sudoku matrix in `board`, returns the complete version.


For example, if you are given this `board`:




|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 4 | 1 | 7 | 2 | 6 | 3 | 5 | 9 |
| 7 | 5 | 3 | 8 | 1 | 9 | 4 | 6 | 2 |
| 0 | 9 | 2 | 5 | 3 | 4 | 1 | 8 | 7 |
| 1 | 2 | 8 | 9 | 5 | 7 | 6 | 4 | 3 |
| 9 | 6 | 5 | 1 | 4 | 3 | 2 | 7 | 8 |
| 4 | 3 | 7 | 6 | 8 | 2 | 9 | 1 | 5 |
| 3 | 1 | 4 | 2 | 7 | 8 | 5 | 9 | 6 |
| 2 | 8 | 9 | 4 | 6 | 5 | 7 | 0 | 1 |
| 5 | 7 | 6 | 3 | 9 | 1 | 8 | 2 | 4 |


Then, you must complete all values equal to **zero**, and return the completed board. In this case, the first should be **6** and the second should be **3**.


The [rules of Sudoku](https://en.wikipedia.org/wiki/Sudoku) are:


1. Each cell must have a value between 1 and 9
2. For each line, all values should be different
3. For each column, all values should be different
4. For each of the nine 3x3 square, all values should be different.



## Private Tests [100%]

## Public Tests [100%]
