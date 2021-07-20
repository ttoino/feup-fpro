# 4. Moving ball

A ball is thrown with a certain [cardinal direction](https://en.wikipedia.org/wiki/Cardinal_direction). When it hits an obstacle it turns in the angle of the obstacle. You must return the path of the ball from the beginning until it reaches the goal, represented here by the green tile:


      image/svg+xml                                          


The board is defined as a list of strings such as



```
board = [
    "E \\",
    "/ /",
    "   ",
    "\\ X"
]

```

* `' '` is empty space
* `'\\'` and `'/'` are corners that change the direction of the ball by 90º
* `'E'`, `'N'`, `'W'` and `'S'` is the initial position of the ball and respective cardinal direction of the ball
* 'X' is the ending position.


Write a Python function `move_ball(board)` that, given the board as `board`, returns a list with the positions where the ball has travelled through. In the previous example, the return value should be `[(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]`.



## Private Tests [100%]

## Public Tests [100%]
