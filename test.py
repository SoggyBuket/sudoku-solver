from tkinter import *
from tkinter import ttk

root = Tk()

# canvas = tkinter.Canvas(root, width=1000, height=1000)
# canvas.grid(row = 0, column = 0)
# photo = tkinter.PhotoImage(file = 'board.png')
# canvas.create_image(0, 0, image=photo)

image = PhotoImage(file='board.png')
label = ttk.Label(root, image=image)
# label["image"] = PhotoImage(file='board.png')
label.grid(row=0, column=0)

root.mainloop()
