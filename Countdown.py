import random
from time import sleep
from clear import clearScr
from copy import deepcopy

def generate():
    lrg = [25, 50, 75, 100] #large values
    vals = [] #selected values
    sVals = [] #shuffled Values
    #number input
    for i in range(6):
        inp = ""
        while inp == "":
            inp = input(f"{i+1}. Enter L (Large number) or S (Small number): ").lower()
            rand = random.Random()
            if inp != 'l' and inp != 's':
                print("ERROR: Invalid Input, try again")
                inp = ""
            else:
                if inp == 'l': #large values
                    vals.append(lrg[rand.randint(0,3)])
                    print(f"Added {vals[i]}")
                else:
                    vals.append(rand.randint(1,10)) #small values
                    print(f"Added {vals[i]}")
        sleep(1) #allows for better random number calculation
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
            if sVals[i+1] <= 10 and not mUsed: #if second value small and multiply not used before, multiply possible
                posOps.append("*")
            if target % sVals[i+1] == 0 and not dUsed: #if divide produces integer and divide not used before, divide possible
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
    print(f"Target: {target}")
    print()

def countdown(sol: str):
    #countdown
    sleep(1)
    print("Countdown started!")
    print()
    sleep(10)
    print("20 seconds left...")
    print()
    sleep(10)
    print("10 seconds left...")
    print()
    sleep(5)
    for i in range(5, 0, -1): #5,4,3,2,1
        print(f"{i}...")
        print()
        sleep(1)
    print("\n\n\n")
    print("TIMES UP!")
    print("\n")
    print(f"Solution:")
    print(sol)

def main():
    print()
    vals, target, sol = generate()
    display(vals, target)
    countdown(sol)
