import os

SCORES_FILE_NAME = './Scores.txt'  # Path to the file where scores are saved
BAD_RETURN_CODE = -1  # Error code used to indicate a failure

def screen_cleaner():
    # I use this function to clear the terminal screen
    # os.system('cls')  
    os.system('clear')  
