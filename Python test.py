def drawline(p,x):
    for i in range (0,p):
        print(" ", end=""),
    for i in range (0,x):
        print ("*", end=""),
    print()
    return

def drawpicture ():
    drawline(1,10)
    drawline(1,12)
    drawline(1,3)
    drawline(1,5)
    drawline(1,16)
    drawline(1,18)
    drawline(1,23)
    drawline(1,100)
    return
drawpicture()