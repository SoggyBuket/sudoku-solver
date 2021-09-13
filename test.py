from tkinter import *
from tkinter import ttk

root = Tk()

# canvas = tkinter.Canvas(root, width=1000, height=1000)
# canvas.grid(row = 0, column = 0)
# photo = tkinter.PhotoImage(file = 'board.png')
# canvas.create_image(0, 0, image=photo)

image = PhotoImage(file='board.png')
lbw = {}

main_frame = ttk.Frame(root)

def create():
    global lbw

    lbw["label"] = ttk.Label(main_frame)
    lbw["label"]["image"] = image

def grid():
    main_frame.grid(row=0, column=0)
    
    lbw["label"].grid(row=0, column=0)

create()
grid()

root.mainloop()
