from copy import deepcopy

def tic_tac_toe(board, player):
    board = list(map(lambda x: list(x), board.splitlines()))

    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                continue
            b = deepcopy(board)
            b[i][j] = player
            cases = [all(b[k][l] == player for l in range(3)) for k in range(3)] + [all(b[l][k] == player for l in range(3)) for k in range(3)] + [all(b[k][k] == player for k in range(3)), all(b[2-k][k] == player for k in range(3))]
            if any(cases):
                return f"{chr(65+i)}{1+j}"