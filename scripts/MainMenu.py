import passwordGuess as pg
import Minesweeper as ms
import tfe
import NumberCountdown as ncd
import WordCountdown as wcd
from clear import clearScr
from time import sleep

while True:
    clearScr()
    print("Welcome to the game menu!")
    print()
    print("1. 2048")
    print("2. Minesweeper")
    print("3. Number Countdown")
    print("4. Password Guesser", end="")
    if not pg.getAvailable():
        print(" (Unavailable)")
    else:
        print()
    print("5. Word Countdown", end="")
    if not wcd.getAvailable():
        print(" (Unavailable)")
    else:
        print()
    print()
    print("0. Quit")
    print()
    game = input("Enter the number of the game: ")
    try:
        game = int(game)
    except:
        game = 0
    print()

    if game == 1:
        print("You have selected: 2048")
        tfe.main()
    elif game == 2:
        print("You have selected: Minesweeper")
        ms.main()
    elif game == 3: 
        print("You have selected: Number Countdown")
        ncd.main()
    elif game == 4:
        if pg.getAvailable():
            print("You have selected: Password Guesser")
            pg.main()
        else:
            print("ERROR: Password Guesser is unavailable, colorama and/or len5List.txt is not installed, please choose a different game")
    elif game == 5:
        if wcd.getAvailable():
            print("You have selected: Word Countdown")
            wcd.main()
        else:
            print("ERROR: Word Countdown is unavailable, WordList.txt is not installed, please choose a different game")
    elif game == 0:
        print("Thanks for playing!")
        sleep(1)
        break
    else:
        print("ERROR: Invalid input")
    
    print()
    input("Press Enter to return to the game menu")