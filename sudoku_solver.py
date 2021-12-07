import gui as g
import logic as l
import pickle

def main():
    """Setup all the things and return the root window"""
    
    root = g.rootInit()
    frames = g.createFrames(root)
    styles = g.createStyles()
    wid = g.createWidgets(root, frames, styles)
    # g.setDefaultBoard(wid) # -- this is for debug
    g.gridAll(frames, wid)

    # -- init all the button functions
    wid["but"]["start"].config(command=lambda: start(wid))
    wid["but"]["reset"].config(command=lambda: reset(wid))
    wid["but"]["clear"].config(command=lambda: clear(wid))
    wid["but"]["add"].config(command=lambda: storeBoard(wid))

    # -- a wrapper for the setBoard function so that the line below it works
    def setBoardWrap(a):
        g.setBoard(wid, readSBoards(), wid["ot"]["select"][0].get())

    wid["ot"]["select"][0].bind("<<ComboboxSelected>>", setBoardWrap)

    # -- set the values in the combo box
    g.setBoardCombo(wid, readSBoards())

    return root

def reset(wid):
    """Reset the labels and allow input"""
    g.resetLabels(wid)
    g.allowInput(wid)

def clear(wid):
    """Reset and clear the input"""
    reset(wid)
    g.clearEntries(wid)
    g.resetAdded(wid)

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

        g.resetAdded(wid)

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

def storeBoard(wid):
    """Add board state to file"""
    addBoard(g.getEns(wid))
    g.showAdded(wid)
    g.setBoardCombo(wid, readSBoards())

def makeId(flat_boxes):
    """Make ID for a board"""
    board_id = ""

    for i in range(len(flat_boxes)):
        board_id += str(flat_boxes[i])

    return board_id

def addBoard(flat_boxes):
    """Write a board to the file with extra steps"""
    e_boxes = readSBoards()
    boxes_id = makeId(flat_boxes)
    if boxes_id not in e_boxes.keys() and flat_boxes.count(0) <= (81 - 17):
        e_boxes[boxes_id] = flat_boxes
        writeSBoards(e_boxes)

def writeSBoards(e_boxes):
    """Write board to a file"""
    with open("./boards.pickle", "wb") as f:
        pickle.dump(e_boxes, f)

def readSBoards():
    """Read boards from file"""
    s_boards = {}
    with open("./boards.pickle", "rb") as f:
        s_boards = pickle.load(f)

    return s_boards


if __name__ == "__main__":
    root = main()
    root.mainloop()
