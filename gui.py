from tkinter import *
from tkinter import ttk

class SudokuGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Sudoku Solver")
        
        self.main_frame = ttk.Frame(root, padding="3 3 12 12")
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # self.button_frame = ttk.Frame(main_frame, padding)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
