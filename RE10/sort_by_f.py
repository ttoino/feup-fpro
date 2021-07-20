def square_odds(s):
    return ",".join(str(int(x)**2) for x in s.split(",") if int(x) % 2 == 1)