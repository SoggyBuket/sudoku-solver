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

def createBoxes():
    """Create all boxes for the Sudoku board"""
    x_offset = 0
    y_offset = 0

    for i in range(3):
        for j in range(3):
            current_box = []

            for k in range(3):
                current_box.append(board[k+y_offset][x_offset:3+x_offset])
            
            boxes.append(current_box)
            x_offset += 3
        y_offset += 3
        x_offset = 0


createBoxes()

# print(f"Board: {board}")
# print(f"Boxes: {boxes}")
