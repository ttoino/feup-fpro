# Square Root

The square root of any non-negative number can be calculated using the following algorithm:


1. Calculate the midpoint of the interval **[a, b]** of possible values for the square root of the number;
2. If the midpoint is the solution or the limits of the interval agree at least on 5 decimal places, exit the iteration and return the solution obtained;
3. If the midpoint is greater than the solution, then define it as the new upper limit of the interval, otherwise define it as the new lower limit of the interval;
4. Iterate this process until the condition to exit is met.


Write a Python program that receives a float `n`, provided by the user, and calculates the square root by implementing the algorithm described.



## Private Tests [100%]

## Public Tests [100%]
