import pygame
import os


# Initializes a new Game class instance  with a board and screensize parameters.
# The size of each piece is calculated using integer division; the screensize dimensions
# divided by the board size dimensions.
class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

# Main event loop. Creates a screen, and initializes pygame.
# Handles the mouse click events, rightClick will either be true or false
# and will be sent to the handleClick function along with the position of the
# click. It then draws the board with the updated move.
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if (self.board.getWon()):
                running = False
        pygame.quit()
# Loops through every piece on the board, retrieves their updated
# value along with the corresponding image, and blits the images starting
# with the lop left space, cycling through each column before blitting the next row.
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

# Uses os to load image files from the images folder into a dictionary,
# uses pygame.transform to scale down images to the size of a piece.
    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load("images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

# returns the correct image from the image folder, depending on the properties of the
# piece that is passed in.
    def getImage(self, piece):
        string = "bomb" if piece.getHasBomb() else str(piece.getNumAround())
        if (piece.getClicked()):
            string = "bomb-at-clicked" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flagged" if piece.getFlagged() else "facingDown"
        return self.images[string]

# Generates the index of the piece clicked using integer division.
# Handles the click functionality.
    def handleClick(self, position, rightClick):
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)