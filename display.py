def print_cell(cell):
    if cell == 0:
        print(".", end="")
    elif cell == 1:
        print("\033[31mX\033[0m", end="")
    elif cell == 2:
        print("\033[33mO\033[0m", end="")
    else:
        print(" ", end="")

def display_current_player(current_player):
    if current_player == 1:
        print("\033[31mRed to move\033[0m")
    elif current_player == 2:
        print("\033[33mYellow to move\033[0m")

def column_filled():
    print("This column is filled!")

def display_board(board):
    for row in board:
        for cell in row:
            print_cell(cell)
        print()