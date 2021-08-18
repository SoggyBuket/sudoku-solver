# things to do
#  - gui for inputting the sudoku
#  - sudoku solving logic
#  - maybe some other things?

import tkinter as tk # -- gonna use this later for gui interface

board = [
    [0,0,9,0,8,0,0,2,7],
    [2,0,5,4,0,0,3,0,0],
    [0,0,0,1,2,0,0,9,0],
    [0,9,0,3,0,0,6,8,0],
    [0,3,2,0,0,0,0,5,0],
    [0,0,8,9,0,2,0,0,1],
    [0,0,0,6,5,0,0,1,3],
    [0,8,6,2,1,0,5,0,9],
    [0,2,1,0,0,0,8,4,0],
]

boxes = []

# -- 0 is nothing is there. 1-9 is the number there. <10 is not allowed
# -- maybe <10 are numbers given by the user initally

# Goal: fill the board with 1-9 without repeating numbers in rows, columns or boxes

# Plan: go through each square and see all the numbers each could be
#  - could go through box by box

#  - go through box by box to see what each square can be
#  - go back and look at if any square can only be one thing or the total number of one
#  number is 1, an put that in the right spot
#    - each time, recheck all the numbers and update the total values

def getBoxes():
    """Get all boxes for the Sudoku board"""
    x_offset = 0
    y_offset = 0

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

def checkPossibleNums(x, y):
    """Check and see what a square could be"""
    # x and y are the absolute x and y positions on the whole board

    def getColumn(row):
        return row[y]

    row = board[x];
    column = list(map(getColumn, board))
    box = boxes[x//3][y//3]
    flat_box = box[0]+box[1]+box[2]
    # pos = board[x][y]

    possible_nums = []

    # print(f"x, y: {x}, {y}")
    # print(f"Row: {row}")
    # print(f"Column: {column}")
    # print(f"Box: {box}")
    # print(f"Num/pos: {pos}")

    for num in range(1, 10):
        if not num in row and not num in column and not num in flat_box:
            possible_nums.append(num)

    return possible_nums

def getAllPossibleNums():
    """
    Find the possible numbers each square on the board could be and
    add a list of them where the number is
    """
    getBoxes()

    for i in range(81):
        # this works because of how division with 9 works
        hor = i//9
        ver = i%9

        possible_nums = []

        if board[hor][ver] == 0:
            possible_nums = checkPossibleNums(hor, ver)
        
        if len(possible_nums) < 1:
            print("Puzzle unsolvable :(")
            return False
        else:
            board[hor][ver] = possible_nums

        

getAllPossibleNums()
