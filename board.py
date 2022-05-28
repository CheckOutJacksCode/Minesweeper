from piece import Piece
from random import random


# Create a Minesweeper board instance
# Initialize board properties and call 'setBoard', which sets
# in motion placing bombs and setting the rest of the
# spaces on the board
class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()

# Double nested loop goes through creating each piece, starting
# with the top row and going through every column before
# moving on to the next row, setting a boolean property 'hasBomb'
# randomly according to a set probability
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()

# This function has the same double loop, starting with the first row
# and looping through every piece. It gets the piece using the row and col,
# and then calls getListOfNeighbors which returns a list of all neighboring piece instances.
# It then calls setNeighbors to apply values to the pieces.
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

# Checks the surrounding pieces for a given index, continues on if
# the index in is checking is either out of bounds or the index itself,
# and then appends it to the neighbors list.
    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors



    def getSize(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

# function that handles the outcome of clicking on a piece.
# If the piece is a bomb, it toggles self.lost to 'true'.
# for anything other than a 0, the function returns and clicks the piece.
# If it is a zero, the function recursively clicks its neighbors.
    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if (flag):
            piece.toggleFlag()
            return
        piece.click()
        if (piece.getHasBomb()):
            self.lost = True
            return
        self.numClicked += 1
        if (piece.getNumAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()):
                self.handleClick(neighbor, False)

    def getLost(self):
        return self.lost

# When all spaces that are not a bomb are clicked, then you have won.
    def getWon(self):
        return self.numNonBombs == self.numClicked