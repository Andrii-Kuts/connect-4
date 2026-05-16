import board
import display
import gameEnd

current_player = 1
activeGame = False

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
    elif result == board.MoveResult.GAME_ENDED:
        stop()

def resign():
    gameEnd.victory(board.get_board(), 3-current_player, resign=True)
    stop()

def stop():
    global activeGame
    activeGame = False

def start():
    global current_player
    global activeGame
    current_player = 1
    board.clear_board()
    setup_move()
    activeGame = True