from tkinter import *
from tkinter import ttk

root = Tk()

# canvas = tkinter.Canvas(root, width=1000, height=1000)
# canvas.grid(row = 0, column = 0)
# photo = tkinter.PhotoImage(file = 'board.png')
# canvas.create_image(0, 0, image=photo)

image = PhotoImage(file='img/board.png')
lbw = {}

main_frame = ttk.Frame(root)
entry_frame = ttk.Frame(main_frame)

def create():
    global lbw

    lbw["label"] = ttk.Label(main_frame)
    lbw["label"]["image"] = image

def grid():
    main_frame.grid(row=0, column=0)
    entry_frame.grid(row=0, column=0)
    
    lbw["label"].grid(row=0, column=0, sticky=(N, S, E, W))

create()
grid()

var = StringVar()
e = ttk.Entry(main_frame, textvariable=var)
e.grid(row=0, column=0)

var2 = StringVar()
f = ttk.Entry(main_frame, textvariable=var2)
f.grid(row=0, column=0, sticky=N)

root.mainloop()
