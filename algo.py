BLOCKSIZE = 40


def valid(grid, x,y, val):
    # y = pos[0] // BLOCKSIZE
    # x = (pos[1] - 40) // BLOCKSIZE
    # print(x,y)
    for i in range(9):
        if grid[x][i] == val:
            # print("error 1")
            return False

    #     check if the value is already present in the same column
    for i in range(9):
        if grid[i][y] == val:
            # print("error2")
            return False

    #     check if the value is already present in the same column
    col = y // 3
    row = x // 3
    c1 = col * 3
    r1 = row * 3
    # print(x, y, row, col, grid[row][col], r1, c1)
    for i in range(r1, r1 + 3):
        for j in range(c1, c1 + 3):
            if grid[i][j] == val:
                # print("error cell")
                return False
    return True


def isSolved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True


# backtracking algorithm for solving the sudoku grid
def findpos(grid):
    # find an empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


# def solve(grid):
#
#     pos = findpos(grid)
#     print(pos)
#     position = (pos[0] * BLOCKSIZE, pos[1] * BLOCKSIZE + 40)
#     if pos:
#         for i in range(1, 10):
#             if valid(grid, position, i):
#                 grid[pos[0]][pos[1]] = i
#                 grid=solve(grid)
#                 grid[pos[0]][pos[1]] = 0
#     return grid

def solve(grid):
    pos = findpos(grid)
    if pos == None:
        return True
    else:
        for i in range(1, 10):
            if valid(grid, pos[0], pos[1], i):
                grid[pos[0]][pos[1]] = i
                if solve(grid):
                    return True
                grid[pos[0]][pos[1]] = 0
    return False
