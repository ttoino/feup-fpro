# 5. Crazy letter soup

Write a function `soup(matrix, word)` that, given a `matrix` of letters, returns the first location of the `word` in the matrix.


For example, let's say we have the following matrix and are trying to find the word `"PORTO"`.




|  | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| **A** | X | A | B | N | T | O |
| **B** | Y | T | N | R | I | T |
| **C** | U | P | O | M | D | S |
| **D** | I | O | H | U | O | O |
| **E** | R | T | E | L | Q | X |
| **F** | I | W | J | K | P | Z |


Then the function returns `"C2"` because the word starts in line=**C**, column=**2**.


Notice that the words can be in any direction: northwest, north, northeast, east, southeast, south, southwest or west.


All letters are given in upper-case and the function returns the first occurrence of the word using lexicographical order (i.e. if the word can be found in `"A4"` and `"B2"`, then it returns `"A4"`).



## Private Tests [50%]

## Public Tests [100%]
