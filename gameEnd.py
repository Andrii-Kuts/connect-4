import display

def victory(board, player, resign=False, sx=-1, sy=-1, d=0):
    display.display_winning_board(board, resign=resign, sx=sx, sy=sy, d=d)
    display.player_won(player)

def draw(board):
    display.display_board(board)
    display.draw()