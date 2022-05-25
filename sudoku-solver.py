board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(board):
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#returns the row and column containing value of 0 in the board (2d array)
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    
    #when there are no more empty squares, return nothing
    return None

def validate(board, n, pos):

    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == n and (i,j) != pos:
                return False

    return True

#uses recursion, when the board is full it is solved.
#utilizes the backtrack algorithm
def solve(board):

    find = findEmpty(board)

    #board not full (base case)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validate(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

print("~~~~~~~~~~~~~~~~~~~~~~~")
print("BEFORE:")
print("~~~~~~~~~~~~~~~~~~~~~~~")
printBoard(board)
solve(board)
print("~~~~~~~~~~~~~~~~~~~~~~~")
print("SOLUTION")
print("~~~~~~~~~~~~~~~~~~~~~~~")

printBoard(board)