def fib_helper(i):
    if i <= 2:
        return 1
    return fib_helper(i-1) + fib_helper(i - 2)

def fib(start, end):
    for i in range(start, end+1):
        yield fib_helper(i)