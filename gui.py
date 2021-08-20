from tkinter import *
from tkinter import ttk

root = root
root.title("Sudoku Solver")

# -- houses all of the frames
frames = {
    "main": ttk.Frame(root),
    "button": ttk.Frame(main_frame, padding="5"),
    "l_board": ttk.Frame(main_frame, padding="3"),
    "r_board": ttk.Frame(main_frame, padding="3"),
}

# -- houses all of the things in the button frame
button_widgets = {}

# -- houses all of the things in the left board frame
l_board_widgets = {}

# -- houses all of the things in the right board frame
r_board_widgets = {}

def gridFrames():
    frames["main"].grid(column=0, row=0, sticky=(N, W, E, S))
    frames["button"].grid(column=1, row=0, sticky=N)
    frames["l_board"].grid(column=0, row=0, sticky=W)
    frames["r_board"].grid(column=2, row=0, sticky=E)

# main_frame = ttk.Frame(root)
# main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

# -- the padding is very interesting:
# -- 1 number means that amount of pixels on all sides
# -- 2 numbers means the first number on the left and right, and the second top
#    and bottom
# -- 4 numbers means left, top, right, bottom
# button_frame = ttk.Frame(main_frame, padding="5")
# button_frame.grid(column=1, row=0, sticky=N)

# lboard_frame = ttk.Frame(main_frame, padding="3")
# lboard_frame.grid(column=0, row=0, sticky=W)

# rboard_frame = ttk.Frame(main_frame, padding="3")
# rboard_frame.grid(column=2, row=0, sticky=E)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# NOTES:
# -- to have borders, you need the 'borderwidth' option set to 2, then you can use 
#    'relief' to set the border style you want
# -- if something isn't working properly, like you can't change a color on something,
#    see if you can use a style to make it work
# -- minimum amount of numbers allowed is 17
# -- can use 'trace_*' on a linked variable for an entry to see if anything has changed
#    in it. Not very "Pythonic" but it should work if need be
# -- will need to use validate for the numbers on the sudoku to make sure they are 1-9
#    or space as an empty square


# IDEAS:
# -- maybe have 2 boards; one on the left for inputting data and one on the right for
#    what the computer outputs so you can compare the original to the solved puzzle
