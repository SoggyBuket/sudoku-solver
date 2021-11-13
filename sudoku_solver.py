import gui as g
import logic as l

def main():
    root = g.rootInit()
    frames = g.createFrames(root)
    styles = g.createStyles()
    wid = g.createWidgets(root, frames, styles)
    g.gridAll(frames, wid)

    wid["but"]["start"].config(command=lambda: g.run(wid))

    return root


if __name__ == "__main__":
    root = main()
    root.mainloop()
