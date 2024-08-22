import random
import time
from Utils import screen_cleaner

# Function to generate a sequence of random numbers
def generate_sequence(difficulty):
    list_of_number = []  # Initialize an empty list to hold the numbers
    i = 0  # Initialize counter
    # Generate a list of random numbers
    while i < difficulty:
        list_of_number.append(random.randint(1, 100))  # Add a random number between 1 and 100 to the list
        i = i + 1  # Increment the counter
    return list_of_number  # Return the generated list

# Function to get a list of numbers from the user
def get_list_from_user(difficulty):
    list_of_number = []  # Initialize an empty list to hold the user's numbers
    i = 0  # Initialize counter
    # Collect a list of numbers from the user
    while i < difficulty:
        # Prompt the user to enter a number between 1 and 100 and add it to the list
        list_of_number.append(int(input("Please choose a number between 1 to 100: ")))
        i = i + 1  # Increment the counter
    return list_of_number  # Return the list of numbers entered by the user

# Function to compare the generated list with the user's list
def is_list_equal(difficulty):
    # Generate a sequence of random numbers
    generate_list = generate_sequence(difficulty)
    print(f"List of numbers: {generate_list}")  # Display the generated list
    time.sleep(2)  # Pause for 2 seconds to allow the user to memorize the numbers
    screen_cleaner()  # Clear the screen
    # Get the list of numbers entered by the user
    guess_list_from_user = get_list_from_user(difficulty)
    # Check if the generated list matches the user's list
    if generate_list == guess_list_from_user:
        return True  # Return True if the lists are equal
    else:
        return False  # Return False if the lists are not equal

# Function to play the Memory Game
def play_memo(difficulty):
    # Compare the generated list with the user's list
    compare_results_status = is_list_equal(difficulty)
    status = False  # Initialize the game status as False (lost)
    # Check the result and print the appropriate message
    if compare_results_status:
        print("You win")  # Print message if the user won
        status = True  # Set status to True
    else:
        print("You lost")  # Print message if the user lost
    return status  # Return the game status
