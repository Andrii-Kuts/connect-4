import board
import display

current_player = 1

def get_current_player():
    return current_player

def setup_move():
    display.display_board(board.get_board())
    display.display_current_player(current_player)

def move(column):
    global current_player
    result = board.place_piece(column, current_player)
    if result == board.MoveResult.SUCCESSFUL:
        current_player = 3 - current_player
        setup_move()
    elif result == board.MoveResult.COLUMN_FILLED:
        display.column_filled()

def start():
    global current_player
    current_player = 1
    board.clear_board()
    setup_move()