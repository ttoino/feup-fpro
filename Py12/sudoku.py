def solve_sudoku(board):
    for i, l in enumerate(board):
        for j, n in enumerate(l):
            if n == 0:
                c = [board[i][j] for j in range(9)]
                s = [board[i//3*3+x][j//3*3+y] for x in range(3) for y in range(3)]
                for k in range(1, 10):
                    if k not in l and k not in c and k not in s:
                        board[i][j] = k

    return board