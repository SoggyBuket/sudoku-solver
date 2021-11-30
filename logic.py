# --- Logic for sudoku_solver.py --- #

def getBoxes(board):
    """Get all boxes for the Sudoku board"""
    boxes = []
    for box in range(9):
        boxes.append([])

    for row in range(len(board)):
        for col in range(9):
            boxes[col//3 + (3 * (row//3))].append(board[row][col])

    return boxes

def checkIfBad(board, boxes):
    """Check if the board starts bad"""
    def repeats(iterable):
        for j in range(1, len(iterable)+1):
            if iterable.count(j) > 1:
                return True
        
        return False

    for i in range(9):
        if repeats(getCol(board, i)) or repeats(board[i]) or repeats(boxes[i]):
            return True

    return False

def getCol(board, y):
    """Return a specified column from board"""
    def getColumn(i):
        return i[y]

    col = list(map(getColumn, board))

    return col

def checkPossibleNums(board, boxes, x, y):
    """Check and see what a cell could be"""
    # -- x and y are the absolute x and y positions on the whole board

    row = board[x]
    col = getCol(board, y)
    box = boxes[y//3 + (3 * (x//3))]

    pos = board[x][y]

    # print(f"x, y: {x}, {y}")
    # print(f"Row: {row}")
    # print(f"Column: {col}")
    # print(f"Box: {box}")
    # print(f"Num/pos: {pos}")

    possible_nums = []

    for num in range(1, 10):
        if not num in row and not num in col and not num in box:
            possible_nums.append(num)

    return possible_nums

def getAllPossibleNums(board):
    """
    Find the possible numbers each square on the board could be and
    add a list of them where the number is
    """
    boxes = getBoxes(board)
    for row in range(len(board)):
        for col in range(9):
            if board[row][col] == 0 or isinstance(board[row][col], list):
                possible_nums = checkPossibleNums(board, boxes, row, col)

                board[row][col] = possible_nums
    boxes = getBoxes(board)

    return board, boxes

def setSingles(board, boxes):
    """Make the arrays with only one number be just that number"""
    changes = 0

    for row in range(len(board)):
        for col in range(9):
            if isinstance(board[row][col], list):
                if len(board[row][col]) == 1:
                    board[row][col] = board[row][col][0]
                    changes += 1
                elif len(board[row][col]) < 1 or checkIfBad(board, boxes): # -- safe guard
                    return board, -1

    return board, changes

def deduce(board, boxes):
    """
    Check and see if a cell has a value that is the only one with that 
    value in it's row, column or box
    """

    for row in range(len(board)):
        for col in range(9):
            if isinstance(board[row][col], list):
                # -- get the flattened row, col and box possibilities minus the ones from
                # -- this cell
                pos_row, pos_col, pos_box = findPosLines(board, boxes, row, col)
                # print(f"row, col: {row}, {col}")
                # pBoard(board)
                # print(pos_row)
                # print(pos_col)
                # print(pos_box)
                # print("")
                
                for i in range(len(board[row][col])):
                    num = board[row][col][i]

                    if num not in pos_row or num not in pos_col or num not in pos_box:
                        board[row][col] = num
                        # print(f"row, col: {row}, {col}  num: {num}")
                        # deleteSame(board, num, row, col)

                        return board, True

    return board, False

def guess(board, boxes, gts, error):
    # -- guessing means putting a number in a square from it's possibilities. We
    # -- have to make a gts each time we guess so we can store the board state
    # -- and revert back if we need to

    # -- gts needs: board, row, col, possibilities, index in possibilities
    # manageGTS(board, gts)

    pGTS(gts)

    if error:
        buffer = (False, False)
        while not buffer[0]:
            buffer = manageGTS(board, boxes, gts)
        board, gts = buffer
    else:
        gts.append(createGTS(board, gts, False))

    # print(gts)
    pBoard(board)
    # -- set the guess in gts
    # print(gts)
    # print(gts[-1])
    # print(gts[-1][1])
    # print(gts[-1][2])
    # print(gts[-1][3])
    # print(gts[-1][4])
    # print(gts[-1][3][gts[-1][4]])
    board[gts[-1][1]][gts[-1][2]] = gts[-1][3][gts[-1][4]]

    return board, gts

def pGTS(gts):
    for i in range(len(gts)):
        print(gts[i])
        print(f"Board: {i}")
        pBoard(gts[i][0])
    print("Done print")

def manageGTS(board, boxes, gts):

    # -- goal is to store states and place a number in 
    # -- a cell as a guess. if the guess doesn't work then try a different guess.
    # -- if all don't work then go back a store and try another guess. if there
    # -- are no stores because there are no guesses you can make then the board
    # -- is unsolvable
    
    if len(gts) >= 1:
        board = copy2DList(gts[-1][0])

        pBoard(board, "manageGTS")     

        if gts[-1][4]+1 == len(gts[-1][3]) or checkIfBad(board, boxes):
            print("Bad")
            deleteGTS(gts)
            return False, False
        else:
            print("increment")
            gts[-1][4] += 1
    else:
        gts.append(createGTS(board, gts, False))

    return board, gts

def createGTS(board, gts, pop, x=0, y=0):
    """Find a new array for a gts"""
    for i in range(81 - (y + (9*x))):
        row = i//9
        col = i%9

        if isinstance(board[row][col], list):
            print(f"Guess at row, col: {row}, {col}")
            if pop:
                deleteGTS(gts)

            # gts.append([[], row, col, board[row][col], 0])

            # gts[-1][0] = copy2DList(board)

            return [copy2DList(board), row, col, board[row][col], 0]

    # return False

def deleteGTS(gts):
    return gts.pop()

def copy2DList(a):
    b = []
    for i in range(len(a)):
        b.append([])
        for j in range(len(a[i])):
            b[i].append(a[i][j])

    return b

# def deleteSame(board, num, x, y):
#     for i in range(9):
#         if isinstance(board[x][i], list) and num in board[x][i]:
#             print(f"row delete {num}  row, col: {x}, {i}")
#             board[x][i].remove(num)

#         if isinstance(board[i][y], list) and num in board[i][y]:
#             print(f"col delete {num}  row, col: {i}, {y}")
#             board[i][y].remove(num)

#     for row in range(3):
#         for col in range(3):
#             box_num = board[(3 * (x//3)) + row][(3 * (y//3)) + col]
#             if isinstance(box_num, list) and num in box_num:
#                 print(f"box delete {num}  row, col: {(3 * (x//3)) + row}, {(3 * (y//3)) + col}")
#                 board[(3 * (x//3)) + row][(3 * (y//3)) + col].remove(num)

def findPosLines(board, boxes, x, y):
    """
    Return the flattened possibilities of the row, col
    and box of a cell, minus it's possibilities
    """
    row = board[x]
    col = getCol(board, y)
    box = boxes[y//3 + (3 * (x//3))]

    pos_row = []
    pos_col = []
    pos_box = []

    for i in range(9):
        # -- flatten row possibilities
        if isinstance(row[i], list) and i != y:
            for j in range(len(row[i])):
                pos_row.append(row[i][j])
        
        # -- flatten col possibilities
        if isinstance(col[i], list) and i != x:
            for j in range(len(col[i])):
                pos_col.append(col[i][j])

        # -- flatten box possibilities
        if isinstance(box[i], list) and (i != (y + 3 * (x - (3 * (x//3)))) - (3 * (y//3))):
            for j in range(len(box[i])):
                pos_box.append(box[i][j])

    return pos_row, pos_col, pos_box
                
# -- copy from gui.py
def pBoard(board, message=None):
    if message:
        print(message)

    print("-------------------")
    for i in range(len(board)):
        for j in range(9):
            print(f" {board[i][j]}", end="")

        print("")
    print("-------------------")
