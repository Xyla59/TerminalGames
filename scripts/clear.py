from os import system, name

def clearScr():
    if name == "nt":
        system("cls")
    else:
        system("clear")