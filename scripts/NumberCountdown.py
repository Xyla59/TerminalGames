import random
from time import sleep
from clear import clearScr
from copy import deepcopy

def generate():
    lrg = [25, 50, 75, 100] #large values
    sml = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #small values
    vals = ["x", "x", "x", "x", "x", "x"] #selected values
    sVals = [] #shuffled Values
    #number input
    for i in range(6):
        display(vals, "Unknown")
        inp = ""
        while inp == "":
            inp = input(f"{i+1}. Enter L (Large number) or S (Small number): ").lower()
            print()
            rand = random.Random()
            if inp != 'l' and inp != 's':
                print("ERROR: Invalid Input, try again")
                inp = ""
            else:
                if inp == 'l': #large values
                    if len(lrg) == 0: #resets lrg list if >4 lrg numbers chosen
                        lrg = [25, 50, 75, 100]
                    toAdd = lrg.pop(rand.randint(0,len(lrg)-1)) #Ensures unique numbers
                    vals[i] = toAdd
                else: #small values
                    toAdd = sml.pop(rand.randint(0,len(sml)-1)) #Ensures unique numbers
                    vals[i] = toAdd
    #target calculation
    print()
    display(vals, "Unknown")
    sVals = deepcopy(vals)
    random.shuffle(sVals)
    print("Calculating target...")
    target = 0
    while target < sum(vals): #target value must be greater than the sum of all the numbers
        ops = []
        mUsed = False #1 multiply
        dUsed = False #1 divide
        target = sVals[0] #target starts with first value
        for i in range(5):
            rand = random.Random()
            posOps = ["+"] #possibe operators
            if target > sVals[i+1]: #if first value is greater, subtract is possible
                posOps.append("-")
            if sVals[i+1] <= 10 and sVals[i+1] > 1 and not mUsed: 
                #if second value small but not 1 and multiply not used before, multiply possible
                posOps.append("*")
                posOps.append("*")
            if target % sVals[i+1] == 0 and sVals[i+1] > 1 and not dUsed: 
                #if divide produces integer and divisor > 1 and divide not used before, divide possible
                posOps.append("/")
                posOps.append("/")
                posOps.append("/") #increases chances of divide actually being used
            op = posOps[rand.randint(0, len(posOps)-1)] #random selection of possible operators

            #appends to operators list and marks if multiply or divide used
            ops.append(op)
            if op == "*":
                mUsed = True
            elif op == "/":
                dUsed = True
            
            target = eval(f"{target} {op} {sVals[i+1]}") #calculates intermediate target using new operator and next value
            sleep(0.1) #allows for better random number generation

    target = int(target)
    #solution
    sol = f"(((({sVals[0]} {ops[0]} {sVals[1]}) {ops[1]} {sVals[2]}) {ops[2]} {sVals[3]}) {ops[3]} {sVals[4]}) {ops[4]} {sVals[5]}"

    return vals, target, sol

def display(vals: list, target):
    #displays values and target
    clearScr()
    print("Numbers: ", end="")
    for i in range(6):
        print(f"{vals[i]}  ", end="")
    print("\n")
    print(f"Target: {target}\n")

def countdown(vals: list, target: int, sol: str):
    #countdown
    for timer in range(30, -1, -1):
        sleep(1)
        display(vals, target)
        print(f"{timer}")
    print("\n")
    print("TIMES UP!")
    print("\n")
    print(f"Solution:")
    print(sol)

def main():
    print()
    vals, target, sol = generate()
    display(vals, target)
    countdown(vals, target, sol)

#main() #For testing purposes