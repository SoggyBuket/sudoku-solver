import gui as g
import logic as l
import pickle

def main():
    """Setup all the things and return the root window"""
    root = g.rootInit()
    frames = g.createFrames(root)
    styles = g.createStyles()
    wid = g.createWidgets(root, frames, styles)
    g.setDefaultBoard(wid)
    g.gridAll(frames, wid)

    wid["but"]["start"].config(command=lambda: start(wid))
    wid["but"]["reset"].config(command=lambda: reset(wid))
    wid["but"]["clear"].config(command=lambda: clear(wid))

    return root

def reset(wid):
    """Reset the labels and allow input"""
    g.resetLabels(wid)
    g.allowInput(wid)

def clear(wid):
    """Reset and clear the input"""
    reset(wid)
    g.clearEntries(wid)

def start(wid):
    """Start solving the board"""
    count = 0
    for i in range(len(wid["en"][0])):
        if wid["en"][0][i].get():
            count += 1
    # -- check if board has at least 17 numbers
    if count >= 17:
        # -- solve the sudoku
        answer = solveBoard(wid)
        if answer == False:
            print("Answer can not be found")
        else:
            print("Done")
        # print(board)

def solveBoard(wid):
    """Solve the sudoku while (not really) updating the GUI"""

    # -- get initial board in row form, as well as boxes
    board, boxes = g.createRowBoard(wid)

    # -- see if the board is solvable off the bat
    if l.checkIfBad(board, boxes):
        print("Bad puzzle :(")
        return False

    # -- get initial possible nums and update boxes
    board, boxes, change = l.getAllPossibleNums(board)
    gts = []

    # -- main loop for solving
    while True:
        # -- set all of the singles on the board. 
        # -- returns number of changes and -1 if found an empty list
        board, count = l.setSingles(board, boxes)

        if count == 0:
            print("No more singles")
            # -- set invisible singles if no more singles
            board, deduced = l.deduce(board, boxes)

            if deduced == True:
                print("Deduced")
            else:
                print("No more deduce")
                board, gts = l.guess(board, boxes, gts, False)
        elif count < 1:
            print("Empty found")
            board, gts = l.guess(board, boxes, gts, True)

        print("Before possibilities")
        l.pBoard(board)
        # -- get possible nums after all the changes and update boxes
        board, boxes, change = l.getAllPossibleNums(board)

        g.setLabels(boxes, wid)

        print("After")
        l.pBoard(board)

        if not change:
            break

    return True



if __name__ == "__main__":
    root = main()
    root.mainloop()
