import random
from time import sleep
from clear import clearScr
from copy import deepcopy

def generate():
    lrg = [25, 50, 75, 100]
    vals = []
    sVals = []
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
                if inp == 'l':
                    vals.append(lrg[rand.randint(0,3)])
                    print(f"Added {vals[i]}")
                else:
                    vals.append(rand.randint(1,10))
                    print(f"Added {vals[i]}")
        sleep(1)
    #target calculation
    print()
    display(vals, "Unknown")
    sVals = deepcopy(vals)
    random.shuffle(sVals)
    print("Calculating target...")
    target = 0
    while target < sum(vals):
        ops = []
        mUsed = False
        dUsed = False
        target = sVals[0]
        for i in range(5):
            rand = random.Random()
            posOps = ["+"]
            if target > sVals[i+1]:
                posOps.append("-")
            if sVals[i+1] <= 10 and not mUsed:
                posOps.append("*")
            if target % sVals[i+1] == 0 and not dUsed:
                posOps.append("/")
                posOps.append("/")
            op = posOps[rand.randint(0, len(posOps)-1)]

            ops.append(op)
            if op == "*":
                mUsed = True
            elif op == "/":
                dUsed = True
            
            target = eval(f"{target} {op} {sVals[i+1]}")
            sleep(0.1)

    target = int(target)
    sol = f"(((({sVals[0]} {ops[0]} {sVals[1]}) {ops[1]} {sVals[2]}) {ops[2]} {sVals[3]}) {ops[3]} {sVals[4]}) {ops[4]} {sVals[5]}"

    return vals, target, sol

def display(vals: list, target):
    clearScr()
    print("Numbers: ", end="")
    for i in range(6):
        print(f"{vals[i]}  ", end="")
    print("\n")
    print(f"Target: {target}")
    print()

def countdown(sol: str):
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
    for i in range(5, 0, -1):
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
