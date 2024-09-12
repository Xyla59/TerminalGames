from clear import clearScr
import random
import time
from copy import deepcopy

grid = []#stores game grid
score = 0 #stores score
end = 0 #end var, 0 = playing, 1 = win, 2 = loss

def setup(): #setup grid
    global grid, score, end
    grid = []
    score = end = 0
    temp1 = ["", "", "", ""]
    for i in range(4):
        grid.append(deepcopy(temp1))
    for i in range(2):
        placeNew(True)
    
def placeNew(start: bool): #place new number randomly on grid
    global grid
    r = random.Random(x=time.time())
    empty = []
    for y in range(4): #Calculating random placement
        for x in range(4):
            if grid[x][y] == "":
                empty.append([x,y])
    rand = r.randint(0,len(empty)-1)
    toPlace = empty.pop(rand)
    val = r.randint(0, 4) #calculating value to be placed (1/5 = 4, else = 2)
    if start:
        val = 0
    if val < 4:
        grid[toPlace[0]][toPlace[1]] = 2
    else:
        grid[toPlace[0]][toPlace[1]] = 4

def drawgrid(): #draws grid to screen
    global score, grid
    clearScr()
    print(f"Score: {score}")
    print()
    for x in range(4):
        for y in range(4):
            if grid[x][y] == "":
                print("[    ] ", end="")
            elif grid[x][y] < 10:
                print(f"[  {grid[x][y]} ] ", end="")
            elif grid[x][y] < 100:
                print(f"[ {grid[x][y]} ] ", end="")
            elif grid[x][y] < 1000:
                print(f"[ {grid[x][y]}] ", end="")
            else:
                print(f"[{grid[x][y]}] ", end="")
        print()
    print()

def checkEndCon(): #checks end conditions, 0 = continue, 1 = win, 2 = loss, 3 = full but possible move
    global grid, end
    end = 2 #assume loss
    for y in range(4):
        for x in range(4):
            if grid[x][y] == 2048: #win cond
                end = 1
                return end
            elif grid[x][y] == "": #cont cond
                end = 0
                return end
    if checkSurround(): #other cont cond
        end = 3
    return end
            
def checkSurround(): #check surrounding values if possible move can be made
    global grid
    for x in range(0, 4):
        for y in range(0, 4):
            checkY = False #to remove corners and centre
            for surY in range(y-1, y+2):
                checkX = False # To remove corners and centre
                for surX in range(x-1, x+2):
                    if surX >= 0 and surY >= 0 and surX < 4 and surY < 4 and grid[surX][surY] == grid[x][y] and (checkY ^ checkX):
                        return True #move can be made even if grid full
                    checkX = not checkX
                checkY = not checkY
    return False #no move can be made

def countEmpty(item: int, line: int, change: int, yAxis: bool): #count how far to move val and if to merge
    global grid
    maxMove = 0
    count = 0
    merge = False
    if change == 1: #up or left
        maxMove = item + 1
    elif change == -1: #down or right
        maxMove = 4 - item
    if maxMove != 1: #edge number, can't move
        for i in range(1, maxMove):
            if yAxis:
                if grid[item-(change*i)][line] == "":
                    count += 1 #move into empty space
                elif grid[item-(change*i)][line] == grid[item][line]: #move into filled space but add numbers
                    count += 1
                    merge = True
                    break
                else: #cant move
                    break
            else:
                if grid[line][item-(change*i)] == "": #see above
                    count += 1
                elif grid[line][item-(change*i)] == grid[line][item]:
                    count += 1
                    merge = True
                    break
                else:
                    break
    return count, merge #returns number to move and if to merge

def move(): #looping statement for which moves to make
    global grid, score, end
    moves = ['w','a','s','d'] #valid moves
    loop = True
    while loop:
        direct = input("Enter direction to move (W/A/S/D): ").lower() 
        print()
        if direct in moves:
            loop = False #input valid
        else:
            print("ERROR: Invalid input")

    yAxis = False #which axis to move in
    start = 0 #starting index in line
    stop = 4 #final index + 1 in line
    change = 0 #direction to shift vals
    if direct == 'w':
        change = 1
        yAxis = True
    elif direct == 'a':
        change = 1
    elif direct == 's':
        change = -1
        yAxis = True
    else: #d
        change = -1
    if change == -1:
        start = 3
        stop = -1

    for line in range(4): #deals with movement of vals in grid
        for item in range(start, stop, change):
            if yAxis:
                if grid[item][line] != "":
                    try:
                        count, merge = countEmpty(item, line, change, yAxis)
                        if count > 0 and not merge:
                            grid[item-(change*count)][line] = deepcopy(grid[item][line])
                            grid[item][line] = ""
                        elif count > 0 and merge:
                            grid[item-(change*count)][line] = deepcopy(grid[item-(change*count)][line]*2)
                            grid[item][line] = ""
                            score += grid[item-change][line]
                    except:
                        pass
            else:
                if grid[line][item] != "":
                    try:
                        count, merge = countEmpty(item, line, change, yAxis)
                        if count > 0 and not merge:
                            grid[line][item-(change*count)] = deepcopy(grid[line][item])
                            grid[line][item] = ""
                        elif count > 0 and merge:
                            grid[line][item-(change*count)] = deepcopy(grid[line][item-(change*count)]*2)
                            grid[line][item] = ""
                            score += grid[line][item-(change*count)]
                    except:
                        pass
    if end == 0:
        placeNew(False)

def main(): #main function, handles loop and checking end conds
    setup()
    while checkEndCon() == 0 or checkEndCon() == 3:
        drawgrid()
        move()
    drawgrid()
    if checkEndCon() == 1:
        print("Congratulations, you got 2048!")
    else:
        print("No more space, you lose!")

#main()