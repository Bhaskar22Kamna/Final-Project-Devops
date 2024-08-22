# Import functions from other modules
from Live import welcome, load_game
from GuessGame import play_guess
from MemoryGame import play_memo
from CurrencyRouletteGame import play_currency
from Score import add_score
from Utils import screen_cleaner

# Messages for game selection and difficulty selection
choseGameMessage = ("0.Exit and Shutdown.\n"
                    "1.Memory Game – a sequence of numbers will appear for one second and you have to guess it back.\n"
                    "2.Guess Game – guess a number and see if you chose the same as the computer.\n"
                    "3.Currency Roulette – try to guess the value of a random amount of USD in ILS.\n")

choseDifficultyMessage = ("0. back to main menu.\n"
                          "1. low difficulty.\n"
                          "2. medium low difficulty.\n"
                          "3. medium difficulty.\n"
                          "4. medium high difficulty.\n"
                          "5. high difficulty.\n")

# Get player's name and display a welcome message
name = input("Enter your name : ")
print(welcome(name))

# Load the initial game choice from the user
gameNumber = load_game(choseGameMessage, 0, 3, "game")

# Main loop to run the selected game
while gameNumber:
    if gameNumber == 1:
        # Load difficulty level for the Memory Game
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        # Play the Memory Game while difficulty level is valid
        while gameDifficulty:
            # Play the Memory Game and add score if the game is won
            if play_memo(gameDifficulty):
                add_score(gameDifficulty)
            # Load the difficulty level again
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    
    elif gameNumber == 2:
        # Load difficulty level for the Guess Game
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        # Play the Guess Game while difficulty level is valid
        while gameDifficulty:
            # Play the Guess Game and add score if the game is won
            if play_guess(gameDifficulty):
                add_score(gameDifficulty)
            # Load the difficulty level again
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    
    elif gameNumber == 3:
        # Load difficulty level for the Currency Roulette Game
        gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
        # Play the Currency Roulette Game while difficulty level is valid
        while gameDifficulty:
            # Play the Currency Roulette Game and add score if the game is won
            if play_currency(gameDifficulty):
                add_score(gameDifficulty)
            # Load the difficulty level again
            gameDifficulty = load_game(choseDifficultyMessage, 0, 5, "difficulty")
    
    # Load the next game choice from the user
    gameNumber = load_game(choseGameMessage, 0, 3, "game")
