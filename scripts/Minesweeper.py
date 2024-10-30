from clear import clearScr #for clearing screen
import random as r #for random placement of mines
import time #for random function's seed
from copy import deepcopy #to copy by value to lists, not reference

#Globals
xSize = 0
ySize = 0
mineCount = 0
minesFound = 0
flagsPlaced = 0
exploded = False
win = False
firstGuess = True
grid = []

def setup(): #setup of size of minefield and number of mines
    global xSize, ySize, mineCount
    valid = False
    x = y = mines = None
    while not valid:
        try: 
            x = int(input("Enter number of cells across (1-30): "))
            y = int(input("Enter number of cells down (1-15): "))
        except Exception:
            print("ERROR: Invalid Input")
        if x != None or y != None:
            if x > 0 and x < 31 and y > 0 and y < 16:
                valid = True
            else:
                print("ERROR: Invalid Input")
    valid = False
    while not valid:
        try:
            mines = int(input(f"Enter number of mines (1-{(x-1) * (y-1)}): "))
        except Exception:
            print("ERROR: Invalid Input")
        if mines != None:
            if mines > 0 and mines <= (x-1) * (y-1):
                valid = True
            else:
                print("ERROR: Invalid Input")
    xSize = x
    ySize = y
    mineCount = mines

def populate():
    global xSize, ySize, mineCount, grid
    rand = r.Random(x=time.time())
    print("Creating minefield, this may take a minute...")
    
    #grid is a 3d array, 2d array for grid, then first layer contains locations and numbers, second is user interaction
    print("\tSmoothing ground...") #Creates Grid Size
    temp = [None, " "] 
    temp2 = []
    for y in range(ySize):
        temp2.append(deepcopy(temp))
    for x in range(xSize):
        grid.append(deepcopy(temp2))
    
    print("\tSetting mines...")
    for i in range(mineCount): #adds mines randomly
        placed = False
        while not placed:
            randX = rand.randint(0, xSize-1)
            randY = rand.randint(0, ySize-1)
            if grid[randX][randY][0] == None:
               grid[randX][randY][0] = "X"
               placed = True
            
    print("\tRecording surroundings...") #Adds values for surrounding cells
    record()

    print("Creation complete!")

def record():
    for y in range(ySize):
        for x in range(xSize):
            if grid[x][y][0] == None:
                surCount = 0
                for surY in range(y-1, y+2):
                    for surX in range(x-1, x+2):
                        if surX >= 0 and surY >= 0 and surX < xSize and surY < ySize:
                            if grid[surX][surY][0] == "X":
                                surCount += 1
                grid[x][y][0] = deepcopy(surCount)

def displayGrid(): #Displays formatted grid
    global win, exploded, grid
    clearScr()
    print("Minefield:")
    print()
    if win or exploded:
        level = 0
    else:
        level = 1
    print("  ", end="")
    for i in range(xSize):
        if i < 10:
            print(f"  {i} ", end="")
        else:
            print(f" {i} ", end="")
    print()
    for y in range(ySize):
        if y < 10:
            print(f"{y}  ", end="")
        else:
            print(f"{y} ", end="")
        for x in range(xSize):
            val = grid[x][y][level]
            if val == 'X' and win == True:
                val = 'F'
            print(f"[{val}] ", end="")
        print()
    print()

def makeGuess():
    global xSize, ySize, mineCount, minesFound, win, exploded, flagsPlaced, grid, firstGuess
    gx = gy = gType = None
    valid = False
    remainingFlags = mineCount - flagsPlaced
    while not valid: #input sanitisation for cell guesses
        try: 
            print()
            print(f"Flags remaining: {remainingFlags}")
            print()
            gx = int(input("Enter x coord: "))
            gy = int(input("Enter y coord: "))
            gType = input("Enter 'F' for Flag or 'C' to Clear: ").upper()
        except Exception:
            print("ERROR: Invalid Input, coords must be numbers and type must be 'F' or 'C'")
        if gx != None or gy != None or gType != None:
            if gx >= 0 and gx < xSize and gy >= 0 and gy < ySize:
                if gType == "F" or gType == "C":
                    valid = True
                else:
                    print("ERROR: Invalid Input, enter 'F' or 'C'")
            else:
                print("ERROR: Invalid Input, coord(s) out of range")
        else:
            print("ERROR: Invalid Input, please enter an option for all statements")
    
    #checks grid and applies guess
    skip = False
    if gType == 'F': #flag click
        if grid[gx][gy][1] == ' ' and remainingFlags > 0:
            grid[gx][gy][1] = deepcopy('F')
            flagsPlaced += 1
        elif grid[gx][gy][1] == 'F':
            grid[gx][gy][1] = deepcopy(' ')
            flagsPlaced -= 1
        else:
            print("ERROR: Invalid option")
            skip = True
        if not skip:
            if grid[gx][gy][0] == 'X' and grid[gx][gy][1] == 'F':
                minesFound += 1
            elif grid[gx][gy][0] == 'X' and grid[gx][gy][1] == ' ':
                minesFound -= 1
            if checkFullGuess():
                win = True
    else: #clearing click
        if firstGuess and grid[gx][gy][0] == "X":
            grid[gx][gy][0] = deepcopy(None)
            placed = False
            for y in range(ySize):
                for x in range(xSize):
                    if grid[x][y][0] != "X" and gx != x and gy != y:
                        grid[x][y][0] = deepcopy("X")
                        placed = True
                    if placed:
                        break
                if placed:
                    break
            record()
        firstGuess = False
        if grid[gx][gy][1] == " ":
            grid[gx][gy][1] = deepcopy(grid[gx][gy][0])
            if grid[gx][gy][1] == 'X':
                exploded = True
            elif grid[gx][gy][1] == 0:
                clearSurround(gx, gy)
        else:
            print("ERROR: Invalid option")

def checkFullGuess():
    for y in range(ySize):
        for x in range(xSize):
            if grid[x][y][1] == ' ':
                return False
    return True

def clearSurround(x: int, y: int): #if a 0 is cleared, clears all surrounding cells until a greater number is found
    global grid
    for surY in range(y-1, y+2):
        for surX in range(x-1, x+2):
            if surX >= 0 and surY >= 0 and surX < xSize and surY < ySize and grid[surX][surY][1] == " ":
                grid[surX][surY][1] = deepcopy(grid[surX][surY][0])
                if grid[surX][surY][1] == 0:
                    clearSurround(surX, surY)

def checkEndCond(): #checks end conditions to check win or loss
    global win, exploded
    if win == True:
        print()
        displayGrid()
        print()
        print("Congratulations, all mines cleared! You win!")
        return False
    elif exploded == True:
        print()
        displayGrid()
        print()
        print("You hit a mine! You lose!")
        return False
    return True
    

def main(): #main function to control main loop
    loop = True
    setup()
    populate()
    while loop:
        displayGrid()
        makeGuess()
        loop = checkEndCond()