import random
from time import sleep
from clear import clearScr
from copy import deepcopy

def getAvailable():
    try:
        f = open("wordList.txt", "r")
        f.close()
        return True
    except:
        return False

def importWL():
    wordList = []
    with open("wordList.txt", "r") as f:
        for line in f:
            wordList.append(line[:-1])
    return wordList

def generate():
    letters = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    consts = ["B","B","C","C","D","D","F","F","G","H","J","K","L","L","M","M","N","N","P","P","R","R","S","S","S","T","T","Y"]
    vowels = ["A", "E", "I", "O", "U"]
    for i in range(10):
        display(letters)
        inp = ""
        rand = random.Random()
        while inp == "":
            inp = input("Constanant (C) or Vowel (V): ").lower()
            if inp != "c" and inp != "v":
                print("ERROR: Invalid Input, try again")
                inp = ""
            else:
                if inp == "v": #vowels
                    if len(vowels) == 0: #resets lrg list if >5 vowels chosen
                        vowels = ["A", "E", "I", "O", "U"]
                    toAdd = vowels.pop(rand.randint(0,len(vowels)-1)) #Ensures unique letter
                    letters[i] = toAdd.lower()
                else: #constanants
                    toAdd = consts.pop(rand.randint(0,len(consts)-1)) #Ensures unique letter
                    letters[i] = toAdd.lower()
    display(letters)
    return letters

def calcLongest(wordList: list, letters:list):
    longList = []
    availLetters = []
    print("Calculating longest word...")
    for word in wordList:
        availLetters = deepcopy(letters)
        poss = True
        for letter in word:
            if letter not in availLetters:
                poss = False
            else:
                availLetters.remove(letter)
        if poss:
            if len(longList) != 0:
                if len(word) > len(longList[0]):
                    longList = []
                    longList.append(word)
                elif len(word) == len(longList[0]):
                    longList.append(word)
            else:
                longList.append(word)
    return longList

def countdown(longList:list, letters:list):
    if len(longList) == 0:
        print("\nERROR: No words over 5 letters long, exitting...")
    else:
        for timer in range(30, -1, -1):
            sleep(1)
            display(letters)
            print(f"{timer}")
        print("\n")
        print("TIMES UP!")
        print("\n")
        print(f"Longest words:")
        count = 0
        for word in longList:
            if count > 10:
                print("    ...")
                break
            print(f"    {word}")
            count += 1
        if count > 10:
            print()
            cont = input("There are more words, display them (y/n): ").lower()
            if cont == "y":
                for i in range(count, len(longList)-1):
                    print(f"    {longList[i]}")
    print()

def display(letters:list):
    clearScr()
    for i in range(len(letters)):
        print(f"{letters[i].upper()}", end="")
        if i != len(letters) - 1:
            print(" , ", end="")
    print("\n")

def main():
    print()
    if getAvailable():
        wl = importWL()
        ls = generate()
        ll = calcLongest(wl, ls)
        countdown(ll, ls)

#main()