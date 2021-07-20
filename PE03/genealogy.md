# 5. Calculator with fractions

Write a function `calculator(expr)` that given an expression `expr` computes its value. The expression `expr` may be a fraction tuple as `(numerator, denominator)` or it may be a tuple composed of `(expr, operator, expr)`. The valid operators are only multiplication (`'*'`) and division (`'/'`) and all values are non-negative. Simplify the result to the smallest integer dividend.


For example, `calculator(((1, 3), '*', (2, 5)))` calculates the expression $$\frac{1}{3}\times\frac{2}{5}$$ and evaluates to the fraction $$\frac{2}{15}$$, represented by `(2, 15)`.



## Private Tests [100%]

## Public Tests [100%]
