import random
from time import time, sleep
from clear import clearScr

def generate():
    lrg = [25, 50, 75, 100]
    vals = []
    ops = []
    target = 0
    #number input
    for i in range(6):
        inp = ""
        while inp == "":
            inp = input(f"{i+1}. Enter L (Large number) or S (Small number): ").lower()
            rand = random.Random(time())
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
    print("Calculating target...")
    mUsed = False
    dUsed = False
    target = vals[0]
    for i in range(5):
        rand = random.Random(time())
        posOps = ["+"]
        if target > vals[i+1]:
            posOps.append("-")
        if vals[i+1] <= 10 and not mUsed:
            posOps.append("*")
        if target % vals[i+1] == 0 and not dUsed:
            posOps.append("/")
        op = posOps[rand.randint(0, len(posOps)-1)]

        ops.append(op)
        if op == "*":
            mUsed = True
        elif op == "/":
            dUsed = True
        
        target = eval(f"{target} {op} {vals[i+1]}")
        sleep(1)

    sol = f"(((({vals[0]} {ops[0]} {vals[1]}) {ops[1]} {vals[2]}) {ops[2]} {vals[3]}) {ops[3]} {vals[4]}) {ops[4]} {vals[5]}"

    return vals, target, sol

def display(vals: list, target: int):
    clearScr("cls")
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