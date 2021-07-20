def mastermind(g0, g1, g2, k0, k1, k2):
    guesses = [g0, g1, g2]
    keys = [k0, k1, k2]

    points = 0

    for i in range(3):
        guess = guesses[i]
        if (guess == keys[i]):
            points += 3
            keys[i] = ""

    for i in range(3):
        guess = guesses[i]
        if (guess in keys):
            points += 1
            keys[keys.index(guess)] = ""

    return points