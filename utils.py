import os
import platform

# Variables
SCORES_FILE_NAME = "Scores.txt"  # A string representing a file name. By default “Scores.txt”
BAD_RETURN_CODE = -1  # A number representing a bad return code for a function.


# Functions
def screen_cleaner():
    """
    Clears the terminal screen. Works on Windows, macOS, and Linux.
    Useful for clearing the screen before a new game starts or during games like Memory Game.
    """
    # Determine the operating system and execute the appropriate clear command.
    if platform.system() == "Windows":
        os.system('cls')  # Command to clear screen in Windows
    else:
        os.system('clear')  # Command to clear screen in Unix-based systems like Linux and macOS
