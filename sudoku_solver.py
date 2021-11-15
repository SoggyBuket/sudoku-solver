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

        answer = solveBoard(board, boxes)
        if answer == False:
            print("Answer can not be found")
        else:
            print("Done")
        # print(board)

def solveBoard(board, boxes):
    if l.checkIfBad(board, boxes):
        print("Bad puzzle :(")
        return False

    l.getAllPossibleNums(board, boxes)

    while True:
        count = l.setSingles(board)
        if count >= 1:
            l.getAllPossibleNums(board, boxes)
        elif count == 0:
            print("No more singles")
            break
        else:
            print("Empty found")
            break

        print(count)
        l.pBoard(board)

    return True



if __name__ == "__main__":
    root = main()
    root.mainloop()
