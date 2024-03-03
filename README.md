# PokemonTCGLCodeImport
Python script to help import bulks of tcgl codes into the game

This script simplifies the process of importing codes into TCGL (Trading Card Game Live) by automating the copying of codes from a text file to the clipboard.

* Setup: Place your codes in a text file of your choice. (Each code should be on a separate line)

* Running the Script:
    Run the script by executing the Python file.
    You'll be prompted to enter the path to the text file containing your codes.

* Copying Codes:
    When pressing CTRL+V to paste a code, the script will automatically replace the clipboard content with the next code.

* Limitation:
    TCGL allows importing a maximum of 10 codes at a time.
    After importing 10 codes, pressing CTRL+V will not paste a new code.

* Restart:
    The script will prompt you to restart if you want to import more than 10 codes.
# Example
Enter the path to the text file: codes.txt

When CTRL+V is pressed, copying next line.

Line copied: ABC123

When CTRL+V is pressed, copying next line.

Line copied: DEF456

When CTRL+V is pressed, copying next line.

Line copied: GHI789

...

10 codes copied, restart program? (Y/N): Y

# Requirements

Python 3.x
pyperclip library: Install using pip install pyperclip
keyboard library: Install using pip install keyboard
