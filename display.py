def print_cell(output, x, y, cell, highlight=False):
    for i in range(11):
        output[x*6][y*10 + i] = output[x*6 + 6][y*10 + i] = "."
    for i in range(7):
        output[x*6 + i][y*10] = output[x*6 + i][y*10 + 10] = "."
    if(cell == 0):
        return
    elif cell == 1:
        color = ""
        if(highlight):
            color = "\033[32m"
        else:
            color = "\033[31m"
        val = color + "#\033[0m"
        for dx in range(-1, 2, 2):
            for dy in range(-1, 2, 2):
                output[x*6 + 3][y*10 + 5] = val
                output[x*6 + 3 + dx][y*10 + 5 + dy] = val
                output[x*6 + 3 + dx][y*10 + 5 + dy*2] = val
                output[x*6 + 3 + dx*2][y*10 + 5 + dy*3] = val
                output[x*6 + 3 + dx*2][y*10 + 5 + dy*4] = val
        return
    elif cell == 2:
        color = ""
        if(highlight):
            color = "\033[32m"
        else:
            color = "\033[33m"
        for i in range(2, 5):
            output[x*6 + i][y*10 + 1] = output[x*6 + i][y*10 + 9] = color + "#\033[0m"
        for i in range(2, 9):
            output[x*6 + 1][y*10 + i] = output[x*6 + 5][y*10 + i] = color + "#\033[0m"
        return

def display_current_player(current_player):
    if current_player == 1:
        print("\033[31m⏱️ Red to move ⏱️\033[0m")
    elif current_player == 2:
        print("\033[33m⏱️ Yellow to move ⏱️\033[0m")

def column_filled():
    print("❌ This column is filled! ❌")

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def display_board(board, showVictory=False, sx=-1, sy=-1, d=0):
    print("\n" * 10)
    highlighted = set()
    if showVictory:
        for i in range(4):
            x = sx + i * dx[d]
            y = sy + i * dy[d]
            highlighted.add((x, y))

    output = []
    for _ in range(len(board)*6 + 2):
        row = []
        for _ in range(len(board[0])*10 + 1):
            row.append(" ")
        output.append(row)

    for row in range(len(board)):
        for col in range(len(board[row])):
            isHighlighted = (row, col) in highlighted
            print_cell(output, row, col, board[row][col], highlight=isHighlighted)
    for col in range(len(board[0])):
        output[len(board) * 6 + 1][col * 10 + 5] = str(col+1)

    for row in output:
        for cell in row:
            print(cell, end="")
        print()

def player_won(player):
    if player == 1:
        print("\033[31m🎉 Red won! 🎉\033[0m")
    elif player == 2:
        print("\033[33m🎉 Yellow won! 🎉\033[0m")

def draw():
    print("⚖️ Draw! ⚖️")