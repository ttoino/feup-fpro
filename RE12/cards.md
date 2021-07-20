# 3. Card game

We are going to develop and test a card game based on the module cards available [here at GitHub](https://github.com/fpro-feup/public/blob/master/recitas/12/cards.py). Study it as you will import it as a module and use the code in `cards.play()` as a starting point for your own code.


First, write an auxiliary Python function `card_value(card)` that, given a `card`, returns its value. The values of the cards correspond to their numerical value from 2-10, all face cards (Jack, Queen, King) count 10 and the Ace counts 11. If the suits are black (clubs and spades) the value of the card doubles. 🂡 🃑


Then re-write a new Python function `play(seed)` that returns a string with the winners of the game (for example, `"P1 P4"`). The winners of each turn, the ones with the most valuable cards, earn one point, and the final winners are the ones with the maximum number of points. The `seed` must be used to initialize the pseudo-random number generator using [`random.seed(seed)`](https://docs.python.org/3/library/random.html#random.seed).


As in the `play()` example given in the module `cards`, the game goes as follows:


1. We deal a hand of 13 cards to each player *(already done in the imported module)*
2. Then a start player is chosen and the players take turns playing their cards *(done)*
3. The players will play random cards at each turn until their hands are empty *(done)*
4. The turn winner, or winners in case there's a draw, are computed using the value of their cards
5. The winner, or winners in case there's a draw, are computed in the end.



## Private Tests [100%]

## Public Tests [100%]
