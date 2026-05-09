from enum import Enum

board = []
for row in range(6):
    board_row = []
    for column in range(7):
        board_row.append(0)
    board.append(board_row)

def check_for_win():
    ...

def check_for_draw():
    ...

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
    if check_for_win():
        # Do something
        return MoveResult.GAME_ENDED
    if check_for_draw():
        # Do something
        return MoveResult.GAME_ENDED
    return MoveResult.SUCCESSFUL

def clear_board():
    ...
    # TODO

def get_board():
    return board

