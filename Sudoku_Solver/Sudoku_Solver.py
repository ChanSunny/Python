import time

def loadPuzzleFile():
    board = []
    textfile_sudoku = open ("SudokuPuzzle.txt", "r")
    puzzle = fileHandle.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
            board.append(list(map(int,puzzle[line].split(","))))
        else:
            board.append(list(map(int,puzzle[line].split(","))))
    textfile_sudoku.close()
    return board

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def valid(board, num, pos):
    row = pos[0]
    column = pos[1]

    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    for i in range (len(board)):
        if board[i][column] == num and row != i:
            return False
    rowBox = row // 3
    columnBox = column // 3
    for i in range(rowBox*3, (rowBox*3) + 3):
        for j in range((columnBox*3), (columnBox*3) + 3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

def printBoard(board):
    if not findEmpty(board):
        print("Finished puzzle")
    else:
        print("Unsolved puzzle")
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------")
        for j in range(len(board[0])):
            if j%3 == 0:
                print("\b|", end ="")
            print(str(board[i][j])+" ", end="")
        print("\b|")
        time.sleep(.1)
    print("-------------------")

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range (1,10):
        if valid(board, i , find):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

board = [
     [7, 8, 0, 4, 0, 0, 1, 2, 0],
     [6, 0, 0, 0, 7, 5, 0, 0, 9],
     [0, 0, 0, 6, 0, 1, 0, 7, 8],
     [0, 0, 7, 0, 4, 0, 2, 6, 0],
     [0, 0, 1, 0, 5, 0, 9, 3, 0],
     [9, 0, 4, 0, 6, 0, 0, 0, 5],
     [0, 7, 0, 3, 0, 0, 0, 1, 2],
     [1, 2, 0, 0, 0, 7, 4, 0, 0],
     [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
printBoard(board)   
solve(board)    
time.sleep(.5)
printBoard(board)
