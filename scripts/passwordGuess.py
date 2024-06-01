#imports
import random
from clear import clearScr
try:
    from colorama import init as colInit
    from colorama import Fore
    colInit() #initialies colour library
    available = True
except:
    available = False

#globals
password = ""
maxGuess = 0

def checkguess(guess: str): #Logic for checking a guess
    correct = [0,0,0,0,0] #correct guesses and value (2 = letter + place, 1 = letter, 0 = no match)
    used = [0,0,0,0,0]

    #loops to check correct letter correct position
    for i in range(0,5):
        if guess[i] == password[i]:
            correct[i] = 2
            used[i] = 1

    #loops to check correct letter wrong position
    for g in range(0,5):
        for p in range(0,5):
            if g != p and correct[g] == 0:
                if guess[g] == password[p] and used[p] == 0:
                    correct[g] = 1
                    used[p] = 1
    
    return correct #returns array 

def guesses(): #inputs and output handling#
    global maxGuess, password
    remain = maxGuess #remaining guesseses

    grid = [] #sets up display grid and colours for display
    cols = []
    for i in range(0,maxGuess):
        temp1 = []
        temp2 = []
        for j in range(0,5):
            temp1.append("_")
            temp2.append(Fore.RESET)
        grid.append(temp1)
        cols.append(temp2)

    clearScr()
    #print empty grid
    for i in range(0,maxGuess):
        if i < 9:
            print(f"{i + 1}.  ", end="")
        else:
            print(f"{i + 1}. ", end="")
        for j in range(0,5):
            print(f"{grid[i][j]} ", end="")
        print("")
    while remain != 0:
        print()
        correct = None
        while correct == None:
            guess = input("Enter Guess: ")
            if len(guess.strip()) == 5 and guess.isalpha():
                correct = checkguess(guess) #checks guess, returs array of correctness vals
            else:
                print("ERROR: Password in incorrect format, must be 5 letters long, letters only, no spaces")
        print()
        
        clearScr()
        #selects correct colour for each letter
        for i in range(0,5):
            if correct[i] == 2:
                cols[maxGuess - remain][i] = Fore.GREEN
            elif correct[i] == 1:
                cols[maxGuess - remain][i] = Fore.YELLOW
            else:
                cols[maxGuess - remain][i] = Fore.RED
            grid[maxGuess - remain][i] = guess[i]
            #print(f"{cols[i]}{guess[i]} ", end="") #outputs coloured letter individualls
        #print(f"{Fore.RESET}") #resets display to default

        #prints grid
        for i in range(0,maxGuess):
            if i < 9:
                print(f"{i + 1}.  ", end="")
            else:
                print(f"{i + 1}. ", end="")
            for j in range(0,5):
                print(f"{cols[i][j]}{grid[i][j]} ", end="")
            print(f"{Fore.RESET}")

        if 1 in correct or 0 in correct: #not all correct
            remain -= 1
            if remain == 0: #no more guesses
                print()
                print(f'Fail - No more guesses - Word was "{password}"')
        else:
            print()
            print("Correct!")
            remain = 0

def setPassword(word: str): #setter for password if imported
    global password
    if len(word.strip()) == 5 and word.isalpha():
        password = word.lower().strip()
    else:
        print("ERROR: Password in incorrect format, must be 5 letters long, letters only, no spaces")

def randomise(): #picks a random 5 letter word as password and sets max guesses randomly between 5 and 10
    words = []
    maxInd = 0
    with open("wordList.txt", "r") as f:
        for line in f:
            if len(line[:-1]) == 5:
                words.append(line[:-1])
                maxInd += 1
    ind = random.randint(0,maxInd)
    word = words[ind]
    setPassword(word)
    randMax = random.randint(5,10)
    setMax(randMax)

def setMax(max: int):
    global maxGuess
    if max > 0:
        maxGuess = max
    else:
        print("ERROR: Max guesses can't be less than or equal to 0")

def getAvailable():
    try:
        f = open("wordList.txt", "r")
        f.close()
    except:
        return False
    return available

def main():
    if available:
        randomise()
        num = 0
        while num == 0:
            try:
                num = int(input("Enter the max number of guesses: "))
            except Exception:
                print("Error: Invalid input\n")
                num = 0
        setMax(num)
        guesses()
    else:
        print()
        print("This game is unavailable, colorama not installed")
        print()
#comment out if using as an import
#randomise()
#guesses()