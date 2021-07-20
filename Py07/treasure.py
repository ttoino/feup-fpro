def treasure(clues):
    clue = (0, 0)
    while clue in clues:
        clue = clues.pop(clue)
    return clue
