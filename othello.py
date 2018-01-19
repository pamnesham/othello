import turtle
import random


#This function sets up the playing area
def startingBoard():
    # Create board size (llx, lly, urx, ury)
    turtle.screensize(100, 100)
    turtle.setworldcoordinates(0, 100, 100, 0)
    turtle.pu()
    ###### Make Turtle draw fast ######
    turtle.speed(0)
    turtle.delay(0)
    ###### Number the rows and columns ######
    ## create ycor labels
    yct = 0
    y = 16
    while yct <= 7:
        turtle.goto(5, y)
        turtle.write(yct, font =("Arial", 12, "bold"))
        yct += 1
        y += 10
    ## create xcor labels
    xct = 0
    x = 15
    while xct <= 7:
        turtle.goto(x, 95)
        turtle.write(xct, font =("Arial", 12, "bold"))
        xct += 1
        x += 10
    ###### Stamp squares onto the board ######
    turtle.shape("square")
    turtle.turtlesize(3, 3, 3)
    turtle.color("gray", "Green")
    xcor = 85
    ycor = 85
    xcount = 0
    ycount = 0
    while ycount <= 7:
        if ycor == 85:
            while ycor > 15:
                turtle.goto(xcor, ycor)
                turtle.stamp()
                ycor -= 10
        if ycor == 15:
            while ycor < 85:
                turtle.goto(xcor, ycor)
                turtle.stamp()
                ycor += 10
            ycount += 1
        xcor -= 10
    ## starting tokens:
    #topleft:
    turtle.goto(45,45)
    tokens("w")
    #top right:
    turtle.goto(55,45)
    tokens("b")
    #bottom right:
    turtle.goto(55,55)
    tokens("w")
    #bottom left:
    turtle.goto(45,55)
    tokens("b")


#This function takes user input and converts it to turtle coordinates
def coordConvert(xinput, yinput):
    coordict = {(0,0):(15,15), (1,0):(25,15), (2,0):(35,15), (3,0):(45,15),
    (4,0):(55,15), (5,0):(65,15), (6,0):(75,15), (7,0):(85,15),

    (0,1):(15,25), (1,1):(25,25), (2,1):(35,25), (3,1):(45,25),
    (4,1):(55,25), (5,1):(65,25), (6,1):(75,25), (7,1):(85,25),

    (0,2):(15,35), (1,2):(25,35), (2,2):(35,35), (3,2):(45,35),
    (4,2):(55,35), (5,2):(65,35), (6,2):(75,35), (7,2):(85,35),

    (0,3):(15,45), (1,3):(25,45), (2,3):(35,45), (3,3):(45,45),
    (4,3):(55,45), (5,3):(65,45), (6,3):(75,45), (7,3):(85,45),

    (0,4):(15,55), (1,4):(25,55), (2,4):(35,55), (3,4):(45,55),
    (4,4):(55,55), (5,4):(65,55), (6,4):(75,55), (7,4):(85,55),

    (0,5):(15,65), (1,5):(25,65), (2,5):(35,65), (3,5):(45,65),
    (4,5):(55,65), (5,5):(65,65), (6,5):(75,65), (7,5):(85,65),

    (0,6):(15,75), (1,6):(25,75), (2,6):(35,75), (3,6):(45,75),
    (4,6):(55,75), (5,6):(65,75), (6,6):(75,75), (7,6):(85,75),

    (0,7):(15,85), (1,7):(25,85), (2,7):(35,85), (3,7):(45,85),
    (4,7):(55,85), (5,7):(65,85), (6,7):(75,85), (7,7):(85,85)}

    turtle.goto(coordict[(xinput, yinput)])


##This function creates white or black tokens
def tokens(color):
    if color == "w":
        turtle.color("black", "ivory")
        turtle.shape("circle")
        turtle.turtlesize(1.7, 1.7, 1)
        turtle.stamp()
    else:
        turtle.color("ivory", "black")
        turtle.shape("circle")
        turtle.turtlesize(1.7, 1.7, 1)
        turtle.stamp()


##This function makes turtle appear the right color w/o stamping
##Fixes bug that made turtle the wrong color briefly
def appearColor(color):
    turtle.turtlesize(1.7, 1.7, 1)
    if color == "w":
        turtle.color("black", "ivory")
        turtle.shape("circle")
        turtle.turtlesize(1.7, 1.7, 1)
    else:
        turtle.color("ivory", "black")
        turtle.shape("circle")


#This function identifies possible neighboring spaces
def directions(ycor, xcor):
    d = [[0,1], [1, 1], [1,0], [1,-1], [0, -1], [-1, -1,], [-1, 0], [-1, 1]]
    return d


#This function determines if a space is unoccupied
def isUnOccupied(board, x, y):
    if board[y][x] == "u":
        return True
    else:
         return False


#This function determines if a space is on the board or out of range
def inGrid(x, y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        return True
    else:
        return False


#This function determines if a move is valid
def isValidMove(board, row, col, color):
    if inGrid(row, col) == True:
        if isUnOccupied(board, row, col) == True:
            if willFlip(board, row, col, color) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


#This function determines if there are chips of the opposite color that would
#   flip between the potential new chip and another chip of the same color
def willFlip(board, x, y, color):
    good = 0
    directs = directions(x, y)
    spaceState = board[y][x]
    for yd, xd in directs:
        if inGrid((x + xd), (y+yd)) == True:
            newy = y + yd
            newx = x + xd
            spaceState = board[newy][newx]
            while spaceState != color and spaceState != "u" and inGrid(newx +xd, newy +yd)==True:
                newy += yd
                newx += xd
                spaceState = board[newy][newx]
                if spaceState == color:
                    good += 1
                    newy = y
                    newx = x
            if spaceState == "u" or inGrid(x, y) == False:
                good += 0
                newy = y
                newx = x
    if good >= 1:
        return True
    else:
        return False


#This function creates a list of all valid moves for a turn
def getValidMoves(board,color):
    moves = []
    row = 0
    col = 0
    for r in range(0,8):
        for c in range(0, 8):
            if isValidMove(board, r, c, color) == True:
                moves += [(r,c)]
    return moves


#This nonpure function displays the chips in the turtle graphics
def putChipsDown(board, x, y, color):
    flipChips = []
    maybeChips = []
    directs = directions(x, y)
    spaceState = board[y][x]
    for yd, xd in directs:
        if inGrid((x + xd), (y+yd)) == True:
            newy = y + yd
            newx = x + xd
            spaceState = board[newy][newx]
            while spaceState != color and spaceState != "u" and inGrid(newx + xd, newy +yd)==True:
                #add chips to a temp list whether they flip or not
                maybeChips.append([newy,newx])
                newy += yd
                newx += xd
                spaceState = board[newy][newx]
                if spaceState == color:
                    ### chips were found that should flip, move them to the flip list
                    for maybey, maybex in maybeChips:
                        flipChips.append([maybey,maybex])
            maybeChips = []
            newy = y
            newx = x
    appearColor(color)
    if len(flipChips) > 0:
        if color == "w":
            turtle.delay(70)
        board[y][x] = color
        coordConvert(x, y)
        tokens(color)
        turtle.delay(0)
        for flipy, flipx in flipChips:
            board[flipy][flipx] = color
            coordConvert(flipx, flipy)
            tokens(color)
    return board


#This function determines where the computer will play
def selectNextPlay(board):
    pcMoves = getValidMoves(board, "w")
    betterMove = []
    #check for corners
    for each in pcMoves:
        if each == (0,0) or each == (0,7) or each == (7,0) or each == (7,7):
            betterMove += [each]
            random.shuffle(betterMove)
            return betterMove[0]
    #check for sides
    for i in range(0,8):
        if (i, 7) in pcMoves:
            betterMove += [(i,7)]
        if (7, i) in pcMoves:
            betterMove += [(7, i)]
        if (0, i) in pcMoves:
            betterMove += [(0, i)]
        if (i, 0) in pcMoves:
            betterMove += [(i, 0)]
    if len(betterMove) > 0:
        random.shuffle(betterMove)
        return betterMove[0]
    #else random move
    else:
        random.shuffle(pcMoves)
        return pcMoves[0]


#This function alternates the turns
def turns(board):
    color = "b"
    ### If at least one side has a valid move
    while len(getValidMoves(board, "b")) > 0 or len(getValidMoves(board, "w")) > 0:
        ### If the user has valid moves, user's turn:
        if len(getValidMoves(board, "b")) > 0:
            color = "b"
            play = turtle.textinput("Enter: x,y", "Enter the coordinates of your play: ")
            if play == "" or play == None:
                turtle.hideturtle()
                turtle.pencolor("DarkOrange")
                turtle.goto(50,30)
                turtle.write("Game forfeited.", align = "center", font = ("Arial", 30, "bold"))
                tally(board)
                break
            while len(play) != 3 or play[1] != "," or play[0] not in \
             ("1","2","3","4","5","6","7","0") or play[2] not in ("1","2","3","4","5","6","7","0"):
                play = turtle.textinput("Enter: x,y", "Enter the coordinates of your play in the format: x,y ")
                if play == "" or play == None:
                    turtle.pencolor("DarkOrange")
                    turtle.goto(50,30)
                    turtle.hideturtle()
                    turtle.write("Game forfeited.", align = "center", font = ("Arial", 30, "bold"))
                    tally(board)
                    break
            xplay = int(play[0])
            yplay = int(play[2])
            tmove = (xplay,yplay)
            while tmove not in getValidMoves(board, color):
                play = turtle.textinput("Invalid move.", "Enter the correct x,y coordinates of your play: ")
                if play == "" or play == None:
                    turtle.hideturtle()
                    turtle.pencolor("DarkOrange")
                    turtle.goto(50,30)
                    turtle.write("Game forfeited.", align = "center", font = ("Arial", 30, "bold"))
                    tally(board)
                    break
                while len(play) != 3 or play[1] != "," or play[0] not in \
                 ("1","2","3","4","5","6","7","0") or play[2] not in ("1","2","3","4","5","6","7","0"):
                    play = turtle.textinput("Enter: x,y", "Enter the coordinates of your play in the format: x,y ")
                    if play == "" or play == None:
                        turtle.hideturtle()
                        turtle.pencolor("DarkOrange")
                        turtle.goto(50,50)
                        turtle.write("Game forfeited.\n Click anywhere to exit.", align = "center", font = ("Arial", 30, "bold"))
                        tally(board)
                        turtle.exitonclick()
                        break
                xplay = int(play[0])
                yplay = int(play[2])
                tmove = (xplay,yplay)
            newBoard = putChipsDown(board, xplay, yplay, "b")
        else:
            if len(getValidMoves(board, "b")) <= 0 and len(getValidMoves(board, "w")) > 0:
                turtle.textinput("Black has no moves.", "You cannot move. Click ok to continue.")
        ### If the pc has valid moves, pc's turn:
        if len(getValidMoves(board, "w")) > 0:
            color = "w"
            pc = selectNextPlay(newBoard)
            xpc = pc[0]
            ypc = pc[1]
            newBoard = putChipsDown(newBoard, xpc, ypc, "w")
        else:
            if len(getValidMoves(board, "w")) <= 0 and len(getValidMoves(board, "b")) > 0:
                turtle.textinput("White has no moves.", "White cannot move. Click ok to continue.")
    #if no possible turns left:
    if len(getValidMoves(board, "w")) <= 0 and len(getValidMoves(board, "b")) <= 0:
        tally(board)



#Shows winner/loser and counts the chips
def tally(board):
    bCount = 0
    wCount = 0
    for r in board:
        for c in r:
            if c == 'b':
                bCount += 1
            elif c == 'w':
                wCount += 1
    turtle.goto(50, 70)
    turtle.write("White: " + str(wCount) + " Black: " + str(bCount), align = "center", font = ("Arial", 30, "normal"))
    turtle.goto(50, 50)
    turtle.pencolor("DarkOrange")
    if bCount > wCount:
        turtle.write("You win!", align = "center", font = ("Arial", 34, "bold"))
    elif wCount > bCount:
        turtle.write("You lose!", align = "center", font = ("Arial", 34, "bold"))
    else:
        turtle.write("It's a Tie!", align = "center", font = ("Arial", 34, "bold"))
    turtle.exitonclick()


#Main function solicits user input and calls functions
def main():
    turtle.hideturtle()
    startingBoard()
    #matrix of unoccupied(u), black(b), or white(w) spaces
    boardState = [["u", "u", "u", "u", "u", "u", "u", "u"],
                ["u", "u", "u", "u", "u", "u", "u", "u"],
                ["u", "u", "u", "u", "u", "u", "u", "u"],
                ["u", "u", "u", "w", "b", "u", "u", "u"],
                ["u", "u", "u", "b", "w", "u", "u", "u"],
                ["u", "u", "u", "u", "u", "u", "u", "u"],
                ["u", "u", "u", "u", "u", "u", "u", "u"],
                ["u", "u", "u", "u", "u", "u", "u", "u"]]
    # play the game:
    turns(boardState)


if __name__ == '__main__':
    main()
