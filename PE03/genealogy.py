def calculator(expr):
    if len(expr) == 2:
        return expr
    
    f1, op, f2 = expr
    n1, d1 = calculator(f1)
    n2, d2 = calculator(f2)
    if op == "/":
        n2, d2 = d2, n2
        
    n, d = n1*n2, d1*d2
    
    if n > 1 and d > 1:
        for i in range(2, n+1):
            while d % i == 0 and n % i == 0:
                n, d = n//i, d//i
                
    return (n, d)