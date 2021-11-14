# things to do
#  - gui for inputting the sudoku
#  - sudoku solving logic
#  - maybe some other things?

# board = [
#     [0,0,9,0,8,0,0,2,7],
#     [2,0,5,4,0,0,3,0,0],
#     [0,0,0,1,2,0,0,9,0],
#     [0,9,0,3,0,0,6,8,0],
#     [0,3,2,0,0,0,0,5,0],
#     [0,0,8,9,0,2,0,0,1],
#     [0,0,0,6,5,0,0,1,3],
#     [0,8,6,2,1,0,5,0,9],
#     [0,2,1,0,0,0,8,4,0],
# ]

# boxes = []

# -- 0 is nothing is there. 1-9 is the number there. <10 is not allowed
# -- maybe <10 are numbers given by the user initally

# Goal: fill the board with 1-9 without repeating numbers in rows, columns or boxes

# Plan: go through each square and see all the numbers each could be
#  - could go through box by box

#  - go through box by box to see what each square can be
#  - go back and look at if any square can only be one thing or the total number of one
#  number is 1, an put that in the right spot
#    - each time, recheck all the numbers and update the total values

def getBoxes(board):
    """Get all boxes for the Sudoku board"""
    x_offset = 0
    y_offset = 0
    boxes = [
        [], [], [], 
        [], [], [], 
        [], [], [],
    ]

    for i in range(3):
        current_row = []
        for j in range(3):
            current_box = []

            for k in range(3):
                current_box.append(board[k+y_offset][x_offset:3+x_offset])
            
            current_row.append(current_box)
            x_offset += 3
        boxes.append(current_row)
        y_offset += 3
        x_offset = 0

    # for i in range(9):


    return boxes

# def checkIfBad(board, boxes):

def checkPossibleNums(board, boxes, x, y):
    """Check and see what a square could be"""
    # x and y are the absolute x and y positions on the whole board

    def getColumn(i):
        return i[y]

    row = board[x]
    col = list(map(getColumn, board))
    box = boxes[y//3 + (3 * (x//3))]

    pos = board[x][y]

    print(f"x, y: {x}, {y}")
    print(f"Row: {row}")
    print(f"Column: {col}")
    print(f"Box: {box}")
    print(f"Num/pos: {pos}")

    possible_nums = []

    for num in range(1, 10):
        if not num in row and not num in col and not num in box:
            possible_nums.append(num)

    return possible_nums

def getAllPossibleNums(board, boxes):
    """
    Find the possible numbers each square on the board could be and
    add a list of them where the number is
    """
    # boxes = getBoxes(board)

    for row in range(len(board)):
        for col in range(9):
            if board[row][col] == 0:
                possible_nums = checkPossibleNums(board, boxes, row, col)
            
                if len(possible_nums) < 1:
                    print("Puzzle unsolvable :(")
                    print(f"row: {row}  col: {col}")
                    print(possible_nums)
                    return False
                else:
                    board[row][col] = possible_nums

    return board
