import tkinter as tk

class Application(tk.Frame):
    """A class for the main window"""

    def __init__(self, master=None):
        """Initialize basic variables and call methods"""
        super().__init__(master)
        self.master = master
        # pack the current frame into the master container (the window)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """Create the base widgets the window has on it"""
        self.hi_there = tk.Button(self, fg="blue", command=self.say_hi)
        # enter is mouse down?
        self.hi_there.bind("<Enter>", self.test)
        self.hi_there["text"] = "Hello world\n(click me)"
        # I don't know how to use the relief option yet :/
        self.hi_there["relief"] = "flat"
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hello :)")

    def test(self, event):
        event.widget["activeforeground"] = "red"

# initialize the window/container
root = tk.Tk()
app = Application(master=root)

# use the window manager to set the title and size of the window
app.master.title("Sudoku Solver")
app.master.maxsize(1000, 400)

# start the program/window stuff
app.mainloop()
