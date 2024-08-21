# Terminal Games

A variety of games to be played in command prompt or terminal.

Compatible with both Windows and Linux.

Current games:
 - 2048
 - Countdown (Maths game)
 - Minesweeper
 - Password Guesser (Wordle)
 - Countdown (Word game)


**Universal instructions**
- 

Install requirements from root dir with pip using

    pip install -r scripts/requirements.txt

Note: requirements install only needed to plkay Password Guesser, other games will work immediately

**Linux instructions**
- 

Modify permissions on the LinuxGameMenu.sh file to allow it to run as an executable using

    sudo chmod u+x LinuxGameMenu.sh

Run LinuxGameMenu.sh as a program from file explorer, or run in terminal:

    ./LinuxGameMenu.sh

If an error comes up trying to play the Password Guesser or Word Countdown games:

You may need to open the wordList.txt file in the scripts dir to format it.


**Windows Instructions**
- 

Double click WinGameMenu.bat from file explorer, or run in Command Prompt:

    WinGameMenu.bat
