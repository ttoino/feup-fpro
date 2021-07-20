def change(money):
    r = dict()
    for i in [2, 1, .5, .2, .1, .05, .02, .01]:
        (x, money) = divmod(money, i)
        money = round(money, 2)
        r[i] = x
    return r
