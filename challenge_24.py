# There are no comments, so I don't know what you are trying to do.

def drawline(p, x):
    for i in range(0, p):
        print(" ", end=" "),
    for i in range(0, x):
        print(".", end=" "),
    print()
    return


def drawpicture():
    drawline(1, 3)
    drawline(1, 5)
    drawline(1, 6)
    drawline(1, 3)
    drawline(1, 8)
    drawline(1, 2)
    drawline(1, 9)
    drawline(1, 7)
    return


drawpicture()
