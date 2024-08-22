from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    # Calculate the points based on the difficulty level
    points_of_winning = difficulty * 3 + 5
    
    # Open the scores file to read the current score
    fr = open(SCORES_FILE_NAME, 'r')
    file_score = fr.read()  # Read the score from the file
    fr.close()  # Close the file after reading
    
    # If the file is empty, set the score to 0
    if not file_score:
        file_score = 0
    
    # Calculate the new score by adding the points from the win
    new_score = int(file_score) + points_of_winning
    new_score_w = str(new_score)  # Convert the new score to a string
    
    # Open the scores file to write the new score
    fw = open(SCORES_FILE_NAME, 'w')
    fw.write(new_score_w)  # Write the new score to the file
    fw.close()  # Close the file after writing

def read_score():
    try:
        # Open the scores file to read the current score
        fr = open(SCORES_FILE_NAME, 'r')
        file_score = fr.read()  # Read the score from the file
        fr.close()  # Close the file after reading
    except:
        # If there is an error (e.g., file not found), return an error message
        file_score = "file not found"
    
    # Return the score or error message
    return file_score
