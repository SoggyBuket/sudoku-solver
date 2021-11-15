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

        answer = l.solveBoard(board, boxes)
        if answer == False:
            print("Answer can not be found")
        # print(board)


if __name__ == "__main__":
    root = main()
    root.mainloop()
