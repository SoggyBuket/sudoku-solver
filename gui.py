# --- GUI for sudoku_solver.py --- #

from tkinter import *
from tkinter import ttk

# -- regex
import re

def rootInit():
    """Create the root window and return it"""
    root = Tk()
    root.title("Sudoku Solver")
    # root.geometry("600x600")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    return root

def createStyles():
    """Create all the styles used in one array"""
    styles = {
        "s": ttk.Style(),
        "m": ttk.Style(),
        "e": ttk.Style(),
        "b": ttk.Style(),
    }

    # -- debug boarders
    # styles["s"].configure(
    #     "TLabel", background="black", relief="solid",
    #     borderwidth=1,
    # )
    # styles["m"].configure(
    #     "but.TFrame", background="blue", relief="groove", 
    #     borderwidth=1, 
    # )

    styles["e"].configure(
        "box.TFrame", background="black", relief="solid",
        borderwidth=2,
    )

    styles["b"].configure(
        "board.TFrame", background="black", relief="solid", 
        borderwidth=3,
    )

    return styles

def createFrames(root):
    """Create all of the frames used in one array"""
    main_frame = ttk.Frame(root)

    # -- the padding is very interesting:
    # -- 1 number means that amount of pixels on all sides
    # -- 2 numbers means the first number on the left and right, and the second top
    #    and bottom
    # -- 4 numbers means left, top, right, bottom
    frames = {
        "main": main_frame,
        "button": ttk.Frame(main_frame, padding="10", style="but.TFrame"),
        "b_center": ttk.Frame(main_frame, padding="10", style="but.TFrame"),
        "t_center": ttk.Frame(main_frame, padding="10", style="but.TFrame"),
        "l_board": ttk.Frame(main_frame, padding="3", style="board.TFrame"),
        "r_board": ttk.Frame(main_frame, padding="3", style="board.TFrame"),
        "e_boxes": [],
        "l_boxes": [],
        "input_text": ttk.Frame(main_frame, padding="1", style="but.TFrame"),
        "output_text": ttk.Frame(main_frame, padding="1 4", style="but.TFrame"),
    }

    for i in range(9):
        frames["e_boxes"].append(ttk.Frame(frames["l_board"], padding="1", style="box.TFrame"))
        frames["l_boxes"].append(ttk.Frame(frames["r_board"], padding="1", style="box.TFrame"))

    return frames

def createWidgets(root, frames, styles):
    """Create all of the widgets used in one array"""

    # -- To make a new widget add it to the wid array and grid it
    wid = {
        "en": [[]],
        "la": [[]],
        "txt": {
            "input_text": ttk.Label(frames["input_text"], text="Input:", padding="20 1"),
            "output_text": ttk.Label(frames["output_text"], text="Output:", padding="20 1"),
        },
        "but": {
            "start": ttk.Button(frames["b_center"], text="Start", padding="10 7"),
            "reset": ttk.Button(frames["b_center"], text="Reset"),
            "clear": ttk.Button(frames["b_center"], text="Clear"),
            "add": ttk.Button(frames["t_center"], text="Add Board"),
        },
        "ot": {
            "select": [ttk.Combobox(frames["input_text"]), StringVar()]
        }
    }

    # -- check if the entry is a number
    def check(new):
        return re.match('^[1-9]*$', new) is not None and len(new) <= 1

    # -- a wrapper for the check function
    check_wrap = (root.register(check), "%P")

    # -- make all entries
    for box in range(len(frames["e_boxes"])):
        for i in range(9):
            # -- this might be hard to debug later
            wid["en"][0].append(StringVar())
            wid["en"].append(ttk.Entry(
                frames["e_boxes"][box], textvariable=wid["en"][0][i+(9*box)], validate="key",
                validatecommand=check_wrap, width=1, font=("TkDefaultFont 42"), takefocus=1,
                justify=CENTER, style="TEntry"
            ))

    # -- make all the labels for the output board
    for box in range(len(frames["l_boxes"])):
        for i in range(9):
            wid["la"][0].append(StringVar())
            wid["la"][0][i+(9*box)].set("0")
            wid["la"].append(ttk.Label(
                frames["l_boxes"][box], textvariable=wid["la"][0][i+(9*box)], font=("TkDefaultFont 40"),
                width=1, justify=RIGHT
            ))

    wid["ot"]["select"][0].config(textvariable=wid["ot"]["select"][1], state="readonly")

    return wid

def gridAll(frames, wid):
    """Grid all of the widgets and frames used"""

    # -- gridding the frames
    frames["main"].grid(column=0, row=0, sticky=(N, W, E, S))
    frames["l_board"].grid(column=1, row=1, rowspan=2, sticky=W)
    # frames["button"].grid(column=2, row=1, sticky=(S, N))
    frames["b_center"].grid(column=2, row=2, sticky=S)
    frames["t_center"].grid(column=2, row=1, sticky=N)
    frames["r_board"].grid(column=3, row=1, rowspan=2, sticky=E)
    frames["input_text"].grid(column=1, row=0, sticky=(N, W))
    frames["output_text"].grid(column=3, row=0, sticky=(N, W))

    # -- grid the boxes for the entries and labels
    for i in range(len(frames["e_boxes"])):
        frames["e_boxes"][i].grid(column=i%3, row=i//3)
        frames["l_boxes"][i].grid(column=i%3, row=i//3)

    # -- gridding the widgets
    wid["but"]["start"].grid(column=0, row=5, sticky=S)
    wid["but"]["reset"].grid(column=0, row=4, sticky=S)
    wid["but"]["clear"].grid(column=0, row=3, sticky=S)
    wid["but"]["add"].grid(column=0, row=1, sticky=N)

    wid["ot"]["select"][0].grid(column=1, row=0, sticky=S)

    wid["txt"]["input_text"].grid(column=0, row=0)
    wid["txt"]["output_text"].grid(column=0, row=0)

    count = 1
    # -- grid all entry and labels in the boxes
    for box in range(len(frames["e_boxes"])):
        for i in range(9): # -- size of each box
            wid["en"][count].grid(
                column=i%3, row=i//3, ipadx=9,
                padx=3, pady=3
                )

            wid["la"][count].grid(
                column=i%3, row=i//3,
                padx=17, pady=8
            )

            count += 1

def setDefaultBoard(wid):
    """Set the default board in the entries for debug purposes"""
    d_boards = [
        [
            0, 0, 9, 2, 0, 5, 0, 0, 0, 
            0, 8, 0, 4, 0, 0, 1, 2, 0, 
            0, 2, 7, 3, 0, 0, 0, 9, 0, 
            0, 9, 0, 0, 3, 2, 0, 0, 8, 
            3, 0, 0, 0, 0, 0, 9, 0, 2, 
            6, 8, 0, 0, 5, 0, 0, 0, 1, 
            0, 0, 0, 0, 8, 6, 0, 2, 1, 
            6, 5, 0, 2, 1, 0, 0, 0, 0, 
            0, 1, 3, 5, 0, 9, 8, 4, 0,
        ],
        [
            9, 2, 0, 0, 8, 3, 0, 4, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 7, 0, 2, 0, 0, 0, 0, 0,
            0, 0, 4, 0, 0, 0, 5, 0, 1,
            0, 5, 0, 0, 9, 0, 0, 6, 0,
            3, 0, 2, 0, 0, 0, 4, 0, 0,
            0, 0, 0, 0, 0, 9, 0, 5, 0,
            0, 0, 4, 0, 0, 0, 0, 0, 0,
            0, 3, 0, 7, 1, 0, 0, 2, 8,
        ]
    ]

    c = 0
    setBoard(wid, d_boards, c)

def setBoard(wid, s_boards, c):
    """Put given board in input board"""

    for i in range(len(s_boards[c])):
        val = ""

        if s_boards[c][i] != 0:
            val = s_boards[c][i]

        wid["en"][0][i].set(val)

def setupThings():
    """For running the file by itself (untested)"""

    root = rootInit()
    # -- houses all the frames
    frames = createFrames(root)
    # -- all the styles are global already I think so I don't know why I do this
    styles = createStyles()
    # -- houses all the widgets
    wid = createWidgets(root, frames, styles)
    # -- grid all of the widgets
    gridAll(frames, wid)

    # -- run 'createRowBoard' when button is pressed
    wid["but"]["start"].config(command=lambda: createRowBoard(wid))
    # wid["but"]["reset"].config(command=lambda: reset(wid))
    # root.bind("<Return>", lambda e: wid["but"]["start"].invoke())
    # root.bind("<KP_Enter>", lambda e: wid["but"]["start"].invoke())

    return root

def resetLabels(wid):
    """Reset all output labels to 0"""
    for i in range(len(wid["la"][0])):
        wid["la"][0][i].set(0)

def allowInput(wid):
    """Allow inputting to the input board"""
    for i in range(len(wid["en"]) - 1):
        wid["en"][i+1].configure(state="normal")

def clearEntries(wid):
    """Clear all input entry widgets"""
    for i in range(len(wid["en"][0])):
        wid["en"][0][i].set("")

def showAdded(wid):
    """Show that board was added"""
    wid["but"]["add"].config(state="disabled", text="Added")

def resetAdded(wid):
    """Reset added status"""
    wid["but"]["add"].config(state="normal", text="Add Board")

def setBoardCombo(wid, s_boards):
    """Show stored boards in combo box"""
    wid["ot"]["select"][0].config(values=list(s_boards.keys()))

def createRowBoard(wid):
    """Create board array in row layout from entries"""
    board = []
    boxes = []

    # -- fill board with 0s
    for row in range(9):
        board.append([])
        for col in range(9):
            board[row].append(0)

    # -- create board and boxes from the entries and it's layout
    for box in range(9):
        boxes.append([])
        for cell in range(9):
            count = cell + (9 * box)
            num = 0

            en = wid["en"][0][count].get()
            la_set = en

            wid["en"][count+1].configure(state="disabled")

            if en.isdigit():
                num = int(en)

            if en == "0":
                la_set = ''

            wid["la"][0][count].set(la_set)

            board[cell//3 + (3 * (box//3))][(cell + 3 * (box - (3 * (box//3)))) - (3 * (cell//3))] = num
            boxes[box].append(num)

    # -- print board and boxes to the terminal
    print("Whole board:")
    pBoard(board)
    print("Boxes:")
    pBoard(boxes)
    print(boxes)

    return [board, boxes]

def getEns(wid):
    """Get the entry's values in flat box form"""
    flat_boxes = []

    for i in range(81):
        num = 0
        en = wid["en"][0][i].get()

        if en.isdigit():
            num = int(en)

        flat_boxes.append(num)

    return flat_boxes

def setLabels(boxes, wid):
    """Set the labels to the board values from boxes"""
    for box in range(len(boxes)):
        for cell in range(9):
            count = cell + (9 * box)
            if isinstance(boxes[box][cell], int):
                wid["la"][0][count].set(boxes[box][cell])


def pBoard(board):
    """Print board to the terminal *prettily*"""
    print("-------------------")
    for i in range(len(board)):
        for j in range(9):
            print(f" {board[i][j]}", end="")

        print("")
    print("-------------------")


if __name__ == "__main__":
    root = setupThings()
    root.mainloop()

# NOTES:
# -- to have borders, you need the 'borderwidth' option set to 2, then you can use 
#    'relief' to set the border style you want
# -- if something isn't working properly, like you can't change a color on something,
#    see if you can use a style to make it work
