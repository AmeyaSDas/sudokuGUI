import time

import pygame
import algo

# initialize pygame
pygame.init()

running = True
BORDER_COLOR = (3, 7, 30)
WHITE = (237, 246, 249)
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 400

font1 = pygame.font.SysFont("Times New Roman", 20, bold=False)
font2 = pygame.font.SysFont("Segoe UI", 20, )
i = 0
BORDER = 1
BLOCKSIZE = 40

# creating the screen and setting the title and logo
SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('SUDOKU')
SCREEN.fill(WHITE)

defaultGrid = True

# Default grid/ view of the sudoku board
grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

defaultcell = []


# class for each cell
# class SudokuCell:
#     def __init__(self,value,selected,x,y):
#         self.value=value
#         self.selected=False
#         self.x=x
#         self.y=y

def find_defaultcell(grid,defaultGrid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0 and defaultGrid:
                defaultcell.append((i, j))


# CREATE THE SUDOKU BOARD
def draw_Grid():
    # Set the size of the grid block
    # for x in range(40, WINDOW_WIDTH, BLOCKSIZE):
    #     for y in range(0, WINDOW_HEIGHT + 1, BLOCKSIZE):
    #         rect = pygame.Rect(y, x, BLOCKSIZE, BLOCKSIZE)
    #         pygame.draw.rect(SCREEN, BORDER_COLOR, rect, BORDER)

    text2 = font2.render("Time:", 1, (0, 0, 0))
    # align centre
    SCREEN.blit(text2, (WINDOW_WIDTH - 150,
                        10))
    # Draws grid lines
    for i in range(0, WINDOW_HEIGHT + 1):
        if i % 3 == 0 and i != 0:
            THICK = 4
        else:
            THICK = 1
        pygame.draw.line(SCREEN, BORDER_COLOR, (0, (i * BLOCKSIZE) + 40), (WINDOW_WIDTH, ((i * BLOCKSIZE) + 40)), THICK)
        pygame.draw.line(SCREEN, BORDER_COLOR, ((i * BLOCKSIZE), 40), ((i * BLOCKSIZE), WINDOW_WIDTH), THICK)


def draw_Board(grid):
    # global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(SCREEN, (173, 181, 189),
                                 pygame.Rect((j * BLOCKSIZE), (i * BLOCKSIZE + 40), BLOCKSIZE, BLOCKSIZE))
                text2 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                # incase the center is not working , use expression
                # SCREEN.blit(text2, (j*BLOCKSIZE,i*BLOCKSIZE+40))
                # align centre
                SCREEN.blit(text2, ((j * BLOCKSIZE) + (BLOCKSIZE / 2 - text2.get_width() // 2),
                                    (i * BLOCKSIZE + 40) + (BLOCKSIZE / 2 - text2.get_height() // 2)))


# highlight the selected cell
def selectCell(pos):
    y = pos[0] // BLOCKSIZE
    x = (pos[1] - 40) // BLOCKSIZE

    # print(x, y)
    if x >= 0 and y >= 0 and (x,y) not in defaultcell:
        pygame.draw.rect(SCREEN, (173, 232, 244),
                         pygame.Rect((y * BLOCKSIZE), (x * BLOCKSIZE + 40), BLOCKSIZE, BLOCKSIZE))
        return str(y) + "_" + str(x)


def errorCell(pos, val):
    y = pos[0] // BLOCKSIZE
    x = (pos[1] - 40) // BLOCKSIZE
    # print(x, y)
    text2 = font1.render(str(val), 1, (255, 0, 0))
    # align centre
    SCREEN.blit(text2, ((y * BLOCKSIZE) + (BLOCKSIZE / 2 - text2.get_width() // 2),
                        (x * BLOCKSIZE + 40) + (BLOCKSIZE / 2 - text2.get_height() // 2)))
    return str(y) + "_" + str(x)


def success():
    text2 = font1.render("SUCCESS !!!!!", 1, (0, 127, 95))
    # align centre
    SCREEN.blit(text2, ((WINDOW_WIDTH / 2 - text2.get_width() // 2) - 50,
                        10))


def draw_result_Board(grid):
    # global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(SCREEN, (142, 148, 242),
                                 pygame.Rect((j * BLOCKSIZE), (i * BLOCKSIZE + 40), BLOCKSIZE, BLOCKSIZE))
                text2 = font1.render(str(grid[i][j]), 1, (0, 0, 0))

                # align centre
                SCREEN.blit(text2, ((j * BLOCKSIZE) + (BLOCKSIZE / 2 - text2.get_width() // 2),
                                    (i * BLOCKSIZE + 40) + (BLOCKSIZE / 2 - text2.get_height() // 2)))

start_time=time.time()
# print(start_time)
# print(str(start_time%60)," ",str((start_time%60)//60))


def setgametime(game_time):
    text2 = font2.render(str((game_time%60)//60)+":"+str(game_time%60), 1, (0, 0, 0))
    # align centre
    SCREEN.blit(text2, (WINDOW_WIDTH - 100,
                        10))

    # SCREEN.blit(None, (WINDOW_WIDTH - 50, 10))

while running:
    find_defaultcell(grid,defaultGrid)
    draw_Board(grid)
    draw_Grid()
    defaultGrid = False
    # to exit the window
    # set time
    game_time=round(time.time()-start_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected = selectCell(pos)
        if event.type == pygame.KEYDOWN and pos:
            value = None
            if event.key == pygame.K_SPACE:
                if algo.solve(grid):
                    # draw_result_Board(grid)
                    draw_Board(grid)
                    draw_Grid()
                    pygame.time.delay(60)
                    pygame.display.update()
                    setgametime(game_time)
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9
            if pos and value:
                y = pos[0] // BLOCKSIZE
                x = (pos[1] - 40) // BLOCKSIZE
                isValid = algo.valid(grid, x, y, value)
                if isValid and (x, y) not in defaultcell:
                    # print(pos, (pos[1] - 40) // BLOCKSIZE, (pos[0] - 40) // BLOCKSIZE)
                    grid[(pos[1] - 40) // BLOCKSIZE][(pos[0]) // BLOCKSIZE] = value
                else:
                    errorCell(pos, value)
            isSolved = algo.isSolved(grid)
            if isSolved:
                success()
                setgametime(game_time)

    pygame.display.update()

