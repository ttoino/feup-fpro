# 2. Tic-tac-toe

[Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe), also known as "jogo do galo" in Portugal or "jogo da velha" in Brazil, is a two-player game where each player has a different symbol, which can be either **x** or **o**. The game is played alternately and the goal of each player is to make a line across the board using its symbol.


Write a function `tic_tac_toe(board, player)` that, given a matrix representing the game in the string `board`, returns where the next move should be played so that the player in the string `player` wins. Assume there is always one and only one possible winning move.


For example, if the following `board` is given:




|  | 1 | 2 | 3 |
| --- | --- | --- | --- |
| **A** |  | **x** | **x** |
| **B** |  | **o** |  |
| **C** | **o** | **x** | **o** |


The `board` is represented as the string `" xx\n o \noxo"`.


Then, for both `player='x'` and `player='o'` the winning move is `"A1"`.



## Private Tests [100%]

## Public Tests [100%]
