# 4. Mastermind

Write a function `mastermind(g1, g2, g3, c1, c2, c3)` to evaluate a *single line* of a [mastermind game](https://en.wikipedia.org/wiki/Mastermind_(board_game)).


The function receives 6 single character strings. Each string can be `"b"` for blue, `"w"` for white and `"y"` for yellow. The first 3 arguments are the *user guess*. The last 3 arguments are the *correct key*. Argument 1 is the user guess for the value at argument 4 and so on.


You should give 3 points for each user guess that is completely correct, that is, the same color at the same position in the key and 1 point if the user guessed the color right but at the wrong position (that is, the color exists in the key but at another wrong position).


Note that one right guess (position or color) counts only once.


For example:


* `mastermind("b", "w", "y", "w", "y", "w")` returns the integer `2`
* `mastermind("b", "w", "y", "b", "w", "y")` returns the integer `9`
* `mastermind("b", "b", "y", "b", "w", "b")` returns the integer `4`



## Private Tests [75%]

## Public Tests [100%]
