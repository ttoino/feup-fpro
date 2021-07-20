def soup(matrix, word, pos=None):
    if not pos:
        for i, l in enumerate(matrix):
            for j, v in enumerate(l):
                if word[0] == v:
                    p = soup(matrix, word[1:], (i, j))
                    if p:
                        return f"{chr(i + 65)}{j + 1}"

    else:
        if not word:
            return True

        for i in range(-1, 2):
            for j in range(-1, 2):
                x = pos[0] + i
                y = pos[1] + j
                if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) and word[0] == matrix[x][y]:
                    p = soup(matrix, word[1:], (x, y))
                    if p:
                        return p