import gui as g
import logic as l

def main():
    root = g.rootInit()
    frames = g.createFrames(root)
    styles = g.createStyles()
    wid = g.createWidgets(root, frames, styles)
    g.setDefaultBoard(wid)
    g.gridAll(frames, wid)

    wid["but"]["start"].config(command=lambda: start(wid))

    return root

def start(wid):
    count = 0
    for i in range(len(wid["en"][0])):
        if wid["en"][0][i].get():
            count += 1

    if count >= 17:
        board, boxes = g.run(wid)

        answer = solveBoard(board, boxes, wid)
        if answer == False:
            print("Answer can not be found")
        else:
            print("Done")
        # print(board)

def solveBoard(board, boxes, wid):
    if l.checkIfBad(board, boxes):
        print("Bad puzzle :(")
        return False

    l.getAllPossibleNums(board, boxes)

    while True:
        count = l.setSingles(board)
        deduced = []

        if count >= 1:
            l.getAllPossibleNums(board, boxes)
        elif count == 0:
            print("No more singles")
            deduced = l.deduce(board, boxes)

            if deduced[0] != None:
                print(f"row, col: {deduced[0]}, {deduced[1]}  num: {board[deduced[0]][deduced[1]]}")
            else:
                print("No deduce")
                break
        else:
            print("Empty found")
            break

        boxes = l.getBoxes(board)
        g.setLabels(boxes, wid)

        print(count)
        l.pBoard(board)

    return True



if __name__ == "__main__":
    root = main()
    root.mainloop()
