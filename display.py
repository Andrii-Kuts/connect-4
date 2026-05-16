CELL_HEIGHT = 6
CELL_WIDTH = 12

# 0 - up
# 1 - right
# 2 - down
# 3 - left
# 0-15 - mask of adjacent corners
cornerSymbols = {
    3: "┗",
    6: "┏",
    7: "┣",
    9: "┛",
    11: "┻",
    12: "┓",
    13: "┫",
    14: "┳",
    15: "╋"
}

def generate_grid(n, m, output):
    color = "\033[34m"
    reset = "\033[0m"
    for i in range(0, n+1):
        for j in range(0, m*CELL_WIDTH+1):
            output[i*CELL_HEIGHT][j] = color + "━" + reset
    for i in range(0, n*CELL_HEIGHT+1):
        for j in range(0, m+1):
            output[i][j*CELL_WIDTH] = color + "┃" + reset
    for i in range(0, n+1):
        for j in range(0, m+1):
            mask = 0
            if i > 0: mask += 1
            if j < m: mask += 2
            if i < n: mask += 4
            if j > 0: mask += 8
            output[i*CELL_HEIGHT][j*CELL_WIDTH] = color + cornerSymbols[mask] + reset

def print_cell(output, x, y, cell, highlight=False):
    if(cell == 0):
        return
    
    color = ""
    green = "\x1b[38;2;0;200;20m"
    reset = "\033[0m"

    if highlight:
        color = green
    elif cell == 1:
        color = "\033[31m"
    elif cell == 2:
        color = "\033[33m"

    if highlight:
        for i in range(1, CELL_WIDTH):
            output[x * CELL_HEIGHT][y * CELL_WIDTH + i] = green + "━" + reset
            output[(x+1) * CELL_HEIGHT][y * CELL_WIDTH + i] = green + "━" + reset
        for i in range(1, CELL_HEIGHT):
            output[x * CELL_HEIGHT + i][y * CELL_WIDTH] = green + "┃" + reset
            output[x * CELL_HEIGHT + i][(y+1) * CELL_WIDTH] = green + "┃" + reset
        for dx in range(0, 2):
            for dy in range(0, 2):
                output[(x + dx) * CELL_HEIGHT][(y + dy) * CELL_WIDTH] = green + "█" + reset

    # rows = [
    #     " ▟█████▙ ",
    #     "▟███████▙",
    #     "█████████",
    #     "▜███████▛",
    #     " ▜█████▛ ",
    # ]

    rows = [
        " __dbb_, ",
        ")ddXXXbbc",
        "ddXXXXXbL",
        ")qYXXXYpc",
        " 'YYYYY` ",
    ]

    rows = [
        " ░▒▒███▒▒░ ",
        "░▒▓█████▓▒░",
        "▒▓███████▓▒",
        "░▒▓█████▓▒░",
        " ░▒▒███▒▒░ ",
    ]

    for i in range(1, CELL_HEIGHT):
        for j in range(1, CELL_WIDTH):
            output[x*CELL_HEIGHT + i][y*CELL_WIDTH + j] = color + rows[i-1][j-1] + "\033[0m"

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
    for _ in range(len(board)*CELL_HEIGHT + 2):
        row = []
        for _ in range(len(board[0])*CELL_WIDTH + 1):
            row.append(" ")
        output.append(row)

    generate_grid(len(board), len(board[0]), output)

    for row in range(len(board)):
        for col in range(len(board[row])):
            isHighlighted = (row, col) in highlighted
            print_cell(output, row, col, board[row][col], highlight=isHighlighted)
    for col in range(len(board[0])):
        output[len(board) * CELL_HEIGHT + 1][col * CELL_WIDTH + 6] = str(col+1)

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