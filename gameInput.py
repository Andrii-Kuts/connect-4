import game

def stop():
    ...

def restart():
    ...

def resign():
    ...

def move(column):
    if not column.isdigit():
        print("This move is not a number! Type column number from 1 to 7")
        return
    column_number = int(column)
    if column_number < 1 or column_number > 7:
        print("Column number should be between 1 and 7!")
        return
    game.move(column_number-1)

def help():
    ...

def start():
    while(True):
        input_line = input()
        args = input_line.split()
        command = args[0]
        if command == "stop":
            stop()
        elif command == "restart":
            restart()
        elif command == "resign":
            resign()
        elif command == "move":
            move(args[1])
        elif command == "help":
            help()
        else:
            print('Unknown command! Use "help"')