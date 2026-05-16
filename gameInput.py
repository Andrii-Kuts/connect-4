import game

def startGame():
    if game.activeGame:
        print('❌ The game is already active! Use "stop" to stop it')
        return
    game.start()

def check_active_game():
    if not game.activeGame:
        print('❌ Game is not running! Use "start" to start a game')
        return False
    return True

def stop():
    game.stop()
    print("✌️ See you soon!")
    exit(0)

def restart():
    game.stop()
    game.start()

def resign():
    if not check_active_game():
        return
    game.resign()

def move(column):
    if not check_active_game():
        return
    if not column.isdigit():
        print("❌ This move is not a number! Type column number from 1 to 7")
        return
    column_number = int(column)
    if column_number < 1 or column_number > 7:
        print("❌ Column number should be between 1 and 7!")
        return
    game.move(column_number-1)

def help():
    print("Commands:")
    print("▪️ start: starts a new game")
    print("▪️ move <column>: makes a move")
    print("▪️ resign: forfeits the game")
    print("▪️ restart: restarts a game")
    print("▪️ stop: exits the programm")
    print("▪️ help: shows this tutorial")

def start():
    print('👋 Welcome to Connect 4!')
    print('type "start" to start a game')
    while(True):
        input_line = input("\033[34m")
        print("\033[0m",end="")
        args = input_line.split()
        if len(args) == 0:
            continue
        command = args[0]
        if command == "start":
            startGame()
        elif command == "stop":
            stop()
        elif command == "restart":
            restart()
        elif command == "resign":
            resign()
        elif command == "move":
            if len(args) < 2:
                print("❌ Provide column number")
            else:
                move(args[1])
        elif command == "help":
            help()
        else:
            print('❌ Unknown command! Use "help"')