def print_cell(cell, highlight=False):
    if cell == 0:
        print(".", end="")
    elif cell == 1:
        if(highlight):
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("X\033[0m", end="")
    elif cell == 2:
        if(highlight):
            print("\033[32m", end="")
        else:
            print("\033[33m", end="")
        print("O\033[0m", end="")
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

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def display_winning_board(board, resign=False, sx=-1, sy=-1, d=0):
    highlighted = set()
    if not resign:
        for i in range(4):
            x = sx + i * dx[d]
            y = sy + i * dy[d]
            highlighted.add((x, y))

    for row in range(len(board)):
        for col in range(len(board[row])):
            isHighlighted = (row, col) in highlighted
            print_cell(board[row][col], highlight=isHighlighted)
        print()

def player_won(player):
    if player == 1:
        print("\033[31mRed won!\033[0m")
    elif player == 2:
        print("\033[33mYellow won!\033[0m")

def draw():
    print("Draw!")