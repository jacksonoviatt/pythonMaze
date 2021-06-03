from gameboard import GameBoard
from player import Player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO

# I created a new Player called played starting at position 3,2
played = Player(3, 2)
# I created a new GameBoard called board
board = GameBoard()
while True:


    # this while loop will run until the user exits the game with e key,
    # or the user wins. 
    board.printBoard(played.rowPosition, played.columnPosition)
    
    selection = input("Make a move: ")
    winCheck = board.checkWin(played.rowPosition, played.columnPosition)
    # this conditional block will run the move functions based on the users choice
    # we will check the row or column position by calling the check move function from gameboard.py
    # assuming that check passes and the user is not hitting the walls
    # if they choose e the loop will break and ezit the game
    # if they are on the winning square, the loop 
    
    if (winCheck == True):
        print("You win!")
        break
    elif(selection == "w"):
        check = board.checkMove(played.rowPosition - 1, played.columnPosition)
        
        if(check == True):
            played.moveUp()
            
    elif(selection == "s"):
        check = board.checkMove(played.rowPosition + 1, played.columnPosition)
        if(check == True):
            played.moveDown()
           
    elif(selection == "a"):
        check = board.checkMove(played.rowPosition, played.columnPosition - 1)
        if(check == True):
            played.moveRight()
           
    elif(selection == "d"):
        check = board.checkMove(played.rowPosition, played.columnPosition + 1)
        if(check == True):
            played.moveLeft()
    elif(selection == "e"):
        break
    
    else:
        check = board.checkMove(played.rowPosition, played.columnPosition)
        print("please enter a valid key")
    
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
