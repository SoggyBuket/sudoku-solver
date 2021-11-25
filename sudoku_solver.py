import gui as g
import logic as l
import time

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
        # -- get initial board in row form, as well as boxes
        # -- NOTE: should I move this into solveBoard?
        board, boxes = g.createRowBoard(wid)

        # -- solve the sudoku
        answer = solveBoard(board, boxes, wid)
        if answer == False:
            print("Answer can not be found")
        else:
            print("Done")
        # print(board)

def solveBoard(board, boxes, wid):
    """Solve the sudoku while updating the GUI"""
    # -- see if the board is solvable off the bat
    if l.checkIfBad(board, boxes):
        print("Bad puzzle :(")
        return False

    # -- get initial possible nums and update boxes
    l.getAllPossibleNums(board, boxes)
    boxes = l.getBoxes(board)

    # -- main loop for solving
    while True:
        # -- set all of the singles on the board. 
        # -- returns number of changes and -1 if found an empty list
        count = l.setSingles(board)

        if count == 0:
            print("No more singles")
            # -- set invisible singles if no more singles
            deduced = l.deduce(board, boxes)

            if deduced == True:
                print("Deduced")
            else:
                print("No more deduce")
                break
        elif count < 1:
            print("Empty found")
            break

        # -- get possible nums after all the changes and update boxes
        l.getAllPossibleNums(board, boxes)
        boxes = l.getBoxes(board)

        g.setLabels(boxes, wid)

        l.pBoard(board)

    return True



if __name__ == "__main__":
    root = main()
    root.mainloop()
