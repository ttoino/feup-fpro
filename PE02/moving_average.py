def moving_average(l, n):
    if len(l) < 3 or n < 3:
        return []
    
    return [round(sum(l[i - n//2:i] + l[i + 1:i + n//2 + 1])/(n - 1), 2) for i in range(n//2, len(l) - n//2)]