def welcome(name):
    # A welcome message that includes the player's name
    message = (f"Hello {name} and welcome to the world of games (WoG).\n"
               "Here you can find many cool games to play.")
    # Return the welcome message
    return message


def load_game(message, lowOption, highOption, option):
    # Display the game or difficulty selection message to the player
    print(message)
    # Prompt the player to choose an option within the specified range
    number = int(input(f"Enter your choice {lowOption}-{highOption}: "))

    # Validate that the entered number is within the specified range
    while lowOption < number > highOption:
        # Inform the player of their choice
        print(f'You chose {option} : {number}')
        # Prompt the player to enter a valid choice
        number = int(input(f"Enter your choice {lowOption}-{highOption}: "))
        # Display the message again for the new input
        print(message)

    # Return the valid number chosen by the player
    return number

def welcome(name):
    # A welcome message that includes the player's name
    message = (f"Hello {name} and welcome to the world of games (WoG).\n"
               "Here you can find many cool games to play.")
    # Return the welcome message
    return message


def load_game(message, lowOption, highOption, option):
    # Display the game or difficulty selection message to the player
    print(message)
    # Prompt the player to choose an option within the specified range
    number = int(input(f"Enter your choice {lowOption}-{highOption}: "))

    # Validate that the entered number is within the specified range
    while lowOption < number > highOption:
        # Inform the player of their choice
        print(f'You chose {option} : {number}')
        # Prompt the player to enter a valid choice
        number = int(input(f"Enter your choice {lowOption}-{highOption}: "))
        # Display the message again for the new input
        print(message)

    # Return the valid number chosen by the player
    return number

