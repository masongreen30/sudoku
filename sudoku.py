import math

def solve(board):
    """
    Solves an AxA sudoku board using backtracking
     Arguments:
        board: incomplete sudoku board
     Returns:
        bool: true when board is solved
    """

    [row, col] = emptyLocation(board)

    if (row == -1 or col == -1):
        return True

    for i in range(1, len(board)+1):
        if (validLocation(board, row, col, i)):
            board[row][col] = i
            
            if (solve(board)):
                return True

            board[row][col] = 0
    return False

def emptyLocation(board):
    """
    Finds an empty spot on the board
     Arguments:
        board: incomplete sudoku board
     Returns:
        list: location of empty spot
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return [i, j]
    return [-1, -1]

def validLocation(board, row, col, num):
    """
    Checks if the number is at a valid location
     Arguments:
        board: incomplete sudoku board
        row:   
        col:   
        num:   number to be inserted
     Returns:
        bool
    """
    # check rows/columns
    for i in range(len(board)):
        if (num == board[row][i] and [row, i] != [row, col]):
            return False
        if (num == board[i][col] and [i, col] != [row, col]):
            return False
    
    # check grid "pieces"
    sq = (int)(math.sqrt(len(board)))
    [r, c] = [row//sq, col//sq]

    for i in range(sq):
        for j in range(sq):
            if (board[sq*r+i][sq*c+j] == num and [sq*r+i, sq*c+j] != [row, col]):
                return False

    return True

def printBoard(board):
    """
    Prints an AxA board
     Arguments:
        board
     Returns:
        None
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], " ", end='')
        print()
    print()

board1 = [
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

board2 = [
        [1, 0, 3, 0],
        [0, 0, 2, 1],
        [0, 1, 0, 2],
        [2, 4, 0, 0]
    ]    


print("9x9 board:")
printBoard(board1)
print("9x9 board solved:")
solve(board1)
printBoard(board1)

print("4x4 board:")
printBoard(board2)
print("4x4 board solved:")
solve(board2)
printBoard(board2)