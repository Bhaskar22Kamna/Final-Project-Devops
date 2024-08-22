def welcome(name):
    # Returns the welcome message with the specified format
    message = f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    return message

def load_game():
    # Prints the game options as specified
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")
    
    # Prompt the user to select a game and ensure the input is valid (1-3)
    while True:
        try:
            game_choice = int(input("Enter the number of the game you want to play (1-3): "))
            if 1 <= game_choice <= 3:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Prompt the user to select a difficulty level and ensure the input is valid (1-5)
    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Return the chosen game number and difficulty level
    return game_choice, difficulty
