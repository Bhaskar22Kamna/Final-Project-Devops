# This file’s sole purpose is to serve the user’s score from the scores.txt file over HTTP with 
# HTML using Python’s Flask library.

# Import necessary functions and modules
from Score import read_score
from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define the route for the root URL ('/')
@app.route('/')
# The function associated with the root URL
def worldOfGame():
    # Read the score from the scores file
    score = read_score()
    print(score)  # Print the score to the console for debugging

    # Check if the score is valid
    if score:
        # Create an HTML response displaying the score
        message = "<html> <head> <title>Scores Game</title> </head> <body> <h1>The score is : <div id='score'>" + score + "</div></h1> </body></html>"
    else:
        # Create an HTML response indicating an error with the score
        errorMessage = "<html> <head> <title>Scores Game</title> </head> <body> <h1><div id='score' style='color:red'>" + score + "</div></h1> </body></html>"
        # Return the error message if the score is not valid
        return errorMessage

    # Return the message displaying the score
    return message

# Main driver function
if __name__ == '__main__':
    # Run the Flask application on the local development server
    app.run(host='0.0.0.0')
