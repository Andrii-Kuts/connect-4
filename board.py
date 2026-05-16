from enum import Enum
import gameEnd

board = []

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def check_line(sx, sy, d):
    if board[sx][sy] == 0:
        return 0
    for i in range(0, 4):
        x = sx + i * dx[d]
        y = sy + i * dy[d]
        if x < 0 or x >= 6 or y < 0 or y >= 7:
            return 0
        if board[x][y] != board[sx][sy]:
            return 0
    return board[sx][sy]

def check_for_win():
    for sx in range(0, 6):
        for sy in range(0, 7):
            for d in range(0, 4):
                res = check_line(sx, sy, d)
                if res != 0:
                    return (res, sx, sy, d)
    return False

def check_for_draw():
    for x in range(0, 6):
        for y in range(0, 7):
            if board[x][y] == 0:
                return False
    return True

class MoveResult(Enum):
    SUCCESSFUL = 1
    COLUMN_FILLED = 2
    GAME_ENDED = 3

def place_piece(column, color):
    row = 5
    while board[row][column] != 0 and row >= 0:
        row -= 1
    if row < 0:
        return MoveResult.COLUMN_FILLED
    board[row][column] = color
    win = check_for_win()
    if win != False:
        gameEnd.victory(board, win[0], sx=win[1], sy=win[2], d=win[3])
        return MoveResult.GAME_ENDED
    if check_for_draw():
        gameEnd.draw(board)
        return MoveResult.GAME_ENDED
    return MoveResult.SUCCESSFUL

def clear_board():
    global board
    board = []
    for _ in range(6):
        board_row = []
        for _ in range(7):
            board_row.append(0)
        board.append(board_row)

def get_board():
    return board

