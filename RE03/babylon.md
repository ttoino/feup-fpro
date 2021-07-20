# 5. Babylonian square-root

Write a Python program that uses the *Babylonian method* for printing square roots.


For a number `num` given by user input, to find its square root, do the following:


1. Make an initial guess: any positive number $$x\_0<num$$
2. Improve the guess: apply the formula $$x\_1=(x\_0+num/x\_0)/2$$; the number $$x\_1$$ is a better approximation to `sqrt(num)`
3. Iterate until convergence: apply the formula $$x\_{n+1}=(x\_n+num/x\_n)/2$$ until the process converges; convergence is achieved when the digits of $$x\_{n+1}$$ and $$x\_n$$ agree on 2 decimal places.


Please use `round` with two decimal places.


The use of the `math` module is forbidden.


For example:


* for `num=20` the output is `4.47`
* for `num=25` the output is `5.0`



## Private Tests [100%]

## Public Tests [100%]
