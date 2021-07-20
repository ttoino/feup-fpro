# 5. Cows and bulls

Write a Python function `cows_bulls(seed)` that, given an integer `seed`, calls `random.seed(seed)` to initialise the random generator. Then, the function creates a random number in the interval [0000, 9999] (`correct`) and a closure function to be returned. That closure function, when called with a number `guess`, calculates the score of the ["cows and bulls" game](https://en.wikipedia.org/wiki/Bulls_and_Cows) of the `correct` versus `guess` numbers, and returns it as a tuple of the form `(cows, bulls)`.


The number of `cows` are the number of digits guessed in the correct place. The number of `bulls` are the number of digits guessed correctly but in the wrong place. It is a "cows and bulls" version of the game.


For example: 


* if the given seed is `12345`, then the generated random number is `6825`; if the closure function is called with `guess=2275`, then the result of the closure should be `(1, 1)`.


Note: a [seed](https://docs.python.org/3/library/random.html#random.seed) is a number used to create a pseudo-random generator. The seed guarantees that the generated numbers will be consistent in different computers.



## Private Tests [100%]

## Public Tests [100%]
