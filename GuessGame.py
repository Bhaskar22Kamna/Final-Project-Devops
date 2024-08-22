import random

# Function to generate a random number based on difficulty
def generate_number(message, difficulty):
    # Generate a random number between 1 and the given difficulty
    number = random.randint(1, difficulty)
    # Print the message along with the generated number
    print(f"{message} {number}")
    # Return the generated number
    return number

# Function to get a number guess from the user
def get_guess_from_user(message):
    # Ask the user to input a number based on the given message
    number = int(input(message))
    # Return the user's input as an integer
    return number

# Function to compare the user's guess with the generated number
def compare_results(difficulty):
    # Create a message to prompt the user for their guess
    message = f"Please choose a number between 1 and {difficulty}: "
    # Get the user's guess
    guess_number_from_user = get_guess_from_user(message)
    
    # Message for displaying the secret number
    secret_number_message = "Secret number:"
    # Generate a secret number based on the difficulty
    generate_number_ret = generate_number(secret_number_message, difficulty)
    
    # Compare the generated number with the user's guess
    if generate_number_ret == guess_number_from_user:
        return True  # Return True if the guess is correct
    else:
        return False  # Return False if the guess is incorrect

# Main function to play the guessing game
def play_guess(difficulty):
    # Check if the user's guess matches the generated number
    compare_results_status = compare_results(difficulty)
    
    # Initialize the game status as False (not won)
    status = False
    
    # If the guess is correct, print "you win" and set status to True
    if compare_results_status:
        print("you win")
        status = True
    else:
        # If the guess is incorrect, print "you lost"
        print("you lost")
    
    # Return the final game status (True if won, False if lost)
    return status
