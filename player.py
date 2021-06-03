class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn


# each of these functions will move the player in the 
# chosen direction by adding or subtracting the players row or column position 
# each function will also print an exit message

    def moveUp(self):
        print("Enter e to exit")
        self.rowPosition -= 1

    # TODO
    def moveDown(self):
        print("Enter e to exit")
        self.rowPosition += 1
    # TODO
    def moveLeft(self):
        print("Enter e to exit")
        self.columnPosition += 1

    # TODO
    def moveRight(self):
        print("Enter e to exit")
        self.columnPosition -= 1


