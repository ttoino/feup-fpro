import random

def cows_bulls(seed):
    random.seed(seed)
    correct = list(str(random.randrange(0, 10000)))

    def closure(guess):
        guess = list(str(guess))
        cows = 0
        bulls = 0
        for c, g in list(zip(correct, guess)):
            if c == g:
                cows += 1
                correct.remove(c)
                guess.remove(g)

        for g in guess:
            if g in correct:
                bulls += 1
                correct.remove(g)

        return cows, bulls

    return closure