def direction_v(direction):
    return {"E": (0, 1), "N": (-1, 0), "W": (0, -1), "S": (1, 0)}[direction]


def rotate(direction, tile):
    if tile not in ("/", "\\"):
        return direction
    elif tile == "/":
        return {"S": "W", "W": "S", "N": "E", "E": "N"}[direction]
    elif tile == "\\":
        return {"N": "W", "W": "N", "S": "E", "E": "S"}[direction]


def move_ball(board):
    board = {(i, j): c for i, s in enumerate(board) for j, c in enumerate(s)}
    pos = None
    direction = None
    end = None
    for k, v in board.items():
        if v == "X":
            end = k
        elif v.isalpha():
            pos = k
            direction = v

    positions = [pos]
    while pos != end:
        d = direction_v(direction)
        pos = pos[0] + d[0], pos[1] + d[1]
        positions.append(pos)
        direction = rotate(direction, board[pos])

    return positions