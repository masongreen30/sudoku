from audioop import add
#from pickle import FALSE
import pygame, sys

WIDTH = 576
HEIGHT = 576
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SQUARE_COLOR = (226, 235, 243)
SEL_SQUARE_COLOR = (187, 222, 251)
BORDER_COLOR = (190, 198, 212)
TEXT_COLOR = (52, 72, 97)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(WHITE)

class Board:

    layout1 = [
        [0, 0, 0, 0, 2, 0, 5, 6, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 9, 1, 0, 3, 4, 2],
        [4, 7, 0, 1, 3, 0, 0, 0, 0],
        [0, 6, 2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 7, 6, 0, 2, 1, 0],
        [0, 0, 5, 8, 0, 0, 0, 2, 6],
        [7, 0, 0, 3, 0, 9, 8, 5, 0],
        [8, 9, 1, 2, 5, 0, 0, 0, 3]
    ]

    layout = [
        [(0, True), (0, True), (0, True), (0, True), (2, False), (0, True), (5, False), (6, False), (8, False)],
        [(0, True), (0, True), (0, True), (0, True), (0, True), (0, True), (0, True), (0, True), (0, True)],
        [(0, True), (8, False), (7, False), (9, False), (1, False), (0, True), (3, False), (4, False), (2, False)],
        [(4, False), (7, False), (0, True), (1, False), (3, False), (0, True), (0, True), (0, True), (0, True)],
        [(0, True), (6, False), (2, False), (0, True), (9, False), (0, True), (0, True), (0, True), (0, True)],
        [(0, True), (3, False), (0, True), (7, False), (6, False), (0, True), (2, False), (1, False), (0, True)],
        [(0, True), (0, True), (5, False), (8, False), (0, True), (0, True), (0, True), (2, False), (6, False)],
        [(7, False), (0, True), (0, True), (3, False), (0, True), (9, False), (8, False), (5, False), (0, True)],
        [(8, False), (9, False), (1, False), (2, False), (5, False), (0, True), (0, True), (0, True), (3, False)]
    ]


    def __init__(self):
        self.cubeList = []

    def drawBoard(self, mouseX, mouseY):
        # draw cubes on board
        for i in range(9):
            col = []
            for j in range(9):
                cube = Cube(self.layout1[j][i], i*64, j*64)
                if (mouseX == j and mouseY == i and self.layout[j][i][1]):
                    cube.setColor(SEL_SQUARE_COLOR)
                col.append(cube)
            self.cubeList.append(col)

        # draw lines on board
        for i in range(4):
            pygame.draw.line(screen, BLACK, (0,64*3*i), (576,64*3*i), 4)
            pygame.draw.line(screen, BLACK, (64*3*i,0), (64*3*i,576), 4)

class Cube:
    width = 64
    height = 64

    def __init__(self, num, xPos, yPos):
        self.num = num
        self.rectObj = pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(xPos, yPos, self.width, self.height))
        self.xPos = xPos
        self.yPos = yPos
        pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(xPos+2, yPos+2, self.width-4, self.height-4))
        if (num != 0):
            font = pygame.font.SysFont('Arial', 48)
            text = font.render(str(num), True, TEXT_COLOR)
            textRect = text.get_rect()
            textRect.center = self.rectObj.center
            screen.blit(text, textRect)

    def insertNum(self, n):
        self.num = n
        font = pygame.font.SysFont('Arial', 48)
        text = font.render(str(n), True, TEXT_COLOR)
        textRect = text.get_rect()
        textRect.center = self.rectObj.center
        screen.blit(text, textRect)

    def getNum(self):
        return self.num
    
    def setColor(self, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.xPos+2, self.yPos+2, self.width-4, self.height-4))
        pass
        
    

gameBoard = Board()

# main loop
row = -1
col = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousX = event.pos[0]
            mousY = event.pos[1]

            row = int(mousY // 64)
            col = int(mousX // 64)

        if event.type == pygame.KEYDOWN and (row in range(0, 10)) and (col in range(0, 10)):
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                #user_text = user_text[:-1]
                pass
  
            # Unicode standard is used for string
            # formation
            #else:
                #user_text += event.unicode

            elif event.key == pygame.K_0:
                gameBoard.layout1[row][col] = 0

            elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, 
                               pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                if (gameBoard.layout[row][col][1]): # gameBoard.cubeList[col][row].canChange
                    gameBoard.layout1[row][col] = event.unicode

    gameBoard.drawBoard(row, col)

    pygame.display.update()

