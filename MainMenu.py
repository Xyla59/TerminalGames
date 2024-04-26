import passwordGuess as pg
import Minesweeper as ms
import tfe
import Countdown as cd
from clear import clearScr
from time import sleep

while True:
    clearScr()
    print("Welcome to the game menu!")
    print()
    print("1. 2048")
    print("2. Countdown")
    print("3. Minesweeper")
    print("4. Password Guesser")
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
        print("You have selected: Countdown")
        cd.main()
    elif game == 3:
        print("You have selected: Minesweeper")
        ms.main()
    elif game == 4:
        print("You have selected: Password Guesser")
        pg.main()
    elif game == 0:
        print("Thanks for playing!")
        sleep(1)
        break
    else:
        print("ERROR: Invalid input")
    
    print()
    input("Press Enter to return to the game menu")