from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sudoku Solver")
# root.geometry("600x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# -- the image for the board. Also it has to be global for some reason
board_img = PhotoImage(file="board.png")

# -- TODO: Distinguish the input board from the output board in a good way

def createStyles():
    styles = {
        "s": ttk.Style(),
        "m": ttk.Style(),
    }

    styles["s"].configure(
        "something.TFrame", 
        background="red", 
        relief="raised",
    )

    styles["s"].configure(
        "main.TFrame", 
        background="blue", 
        relief="groove", 
        borderwidth=5, 
    )

    return styles

def createFrames():
    main_frame = ttk.Frame(root)
    frames = {
        "main": main_frame,
        "button": ttk.Frame(main_frame, padding="10"),
        "l_board": ttk.Labelframe(main_frame, text="Input:"),
        "r_board": ttk.Frame(main_frame),
    }

    return frames

def createWidgets(frames):
    wid = {
        "lb": {
            "input_text": ttk.Label(frames["l_board"], text="hello", padding=""),
            "board": ttk.Label(frames["l_board"], image=board_img)
        },
        "rb": {
            "board": ttk.Label(frames["r_board"], image=board_img)
        },
        "but": {
            "start": ttk.Button(frames["button"], text="Start")
        },
    }

    return wid

def gridAll(frames, wid):
    # -- gridding the frames
    frames["main"].grid(column=0, row=0, sticky=(N, W, E, S))
    frames["l_board"].grid(column=1, row=1, sticky=W)
    frames["button"].grid(column=2, row=1, sticky=S)
    frames["r_board"].grid(column=3, row=1, sticky=E)

    # -- gridding the widgets
    wid["lb"]["board"].grid(column=0, row=1, sticky=(N, S, E, W))
    # wid["lb"]["input_text"].grid(column=0, row=0, sticky=(N, W))

    wid["rb"]["board"].grid(column=0, row=0, sticky=(N, S, E, W))

    wid["but"]["start"].grid(column=0, row=5, sticky=(S, E))

def setupThings():
    # -- houses all the frames
    frames = createFrames()
    # -- houses all the widgets
    wid = createWidgets(frames)
    # -- houses all the styles
    styles = createStyles()

    # # -- the image for the board
    # board_img = PhotoImage(file="board.png")

    # wid["lb"]["board"]["image"] = board_img

    # wid["lb"]["board"] = ttk.Label(frames["l_board"], image=board_img)

    # frames["l_board"].configure(style="main.TFrame")

    gridAll(frames, wid)

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
