from tkinter import *
from tkinter import ttk

import re

root = Tk()
root.title("Sudoku Solver")
# root.geometry("600x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# -- the image for the board. Also it has to be global for some reason
board_img = PhotoImage(file="img/board.png")

def createStyles():
    styles = {
        "s": ttk.Style(),
        "m": ttk.Style(),
        "e": ttk.Style()
    }

    styles["s"].configure(
        "something.TFrame", 
        background="red", 
        relief="raised",
    )

    styles["m"].configure(
        "main.TFrame", 
        background="blue", 
        relief="groove", 
        borderwidth=5, 
    )

    styles["e"].configure(
        "TEntry",
        font=25
    )

    return styles

def createFrames():
    main_frame = ttk.Frame(root)
    frames = {
        "main": main_frame,
        "button": ttk.Frame(main_frame, padding="10"),
        "l_board": ttk.Frame(main_frame),
        "text": ttk.Frame(main_frame, style="main.TFrame"),
        "r_board": ttk.Frame(main_frame),
    }

    return frames

def createWidgets(frames, styles):
    wid = {
        "lb": {
            "board": ttk.Label(frames["l_board"], image=board_img)
        },
        "rb": {
            "board": ttk.Label(frames["r_board"], image=board_img)
        },
        "en": [[]],
        "txt": {
            "input_text": ttk.Label(frames["text"], text="Input:", padding="20 1"),
            "output_text": ttk.Label(frames["text"], text="Output:", padding="20 1"),
        },
        "but": {
            "start": ttk.Button(frames["button"], text="Start")
        },
    }

    # -- check if the entry is a number
    def check(new):
        return re.match('^[1-9]*$', new) is not None and len(new) <= 1

    # -- a wrapper for the check function
    check_wrap = (root.register(check), "%P")

    # -- make all entries
    for i in range(81):
        # -- this might be hard to debug later
        wid["en"][0].append(StringVar())
        wid["en"].append(ttk.Entry(
            frames["l_board"], textvariable=wid["en"][0][i], validate="key",
            validatecommand=check_wrap, style="TEntry", width=1, font=("TkDefaultFont 20")
        ))

    return wid

def gridAll(frames, wid):
    # -- gridding the frames
    frames["main"].grid(column=0, row=0, sticky=(N, W, E, S))
    frames["l_board"].grid(column=1, row=1, sticky=W)
    frames["button"].grid(column=2, row=1, sticky=S)
    frames["r_board"].grid(column=3, row=1, sticky=E)
    frames["text"].grid(column=1, row=0, columnspan=3, sticky=N)

    # -- gridding the widgets
    wid["lb"]["board"].grid(column=0, row=0, columnspan=17, rowspan=21)

    wid["rb"]["board"].grid(column=0, row=1, columnspan=9, rowspan=9, sticky=(N, S, E, W))

    wid["but"]["start"].grid(column=0, row=5, sticky=(S, E))

    wid["txt"]["input_text"].grid(column=0, row=0, sticky=(N, W))
    wid["txt"]["output_text"].grid(column=2, row=0, sticky=(N, W))

    # -- TODO: make the entries display right
    # -- put them in the right spot and up the size of the font

    count = 1
    # -- grid all entry boxes
    for row in range(9):
        for col in range(9):
            wid["en"][count].grid(
                column=col+4, row=row+6, ipady=5, ipadx=7,
                padx=1, pady=1
                )
            count += 1

# -- I don't think I want this function when I start to interface with the main file
def setupThings():
    # -- houses all the frames
    frames = createFrames()
    # -- houses all the styles
    styles = createStyles()
    # -- houses all the widgets
    wid = createWidgets(frames, styles)

    # frames["l_board"].configure(style="main.TFrame")

    gridAll(frames, wid)

if __name__ == "__main__":
    setupThings()

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



root.mainloop()

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
