from bs4 import BeautifulSoup
import requests as req

# Function to test the score service
def test_scores_service():
    # Send a request to the local website and get the response
    Web = req.get('http://127.0.0.1:5000')
    
    # Initialize the return value as False
    to_return = False
    
    # Parse the website content using BeautifulSoup and specify the HTML parser
    S = BeautifulSoup(Web.content, "html.parser")
    
    # Find the div with the id "score" and get its text content
    div_text = S.find("div", {"id": "score"}).get_text()
    
    # Check if the score is between 0 and 1000
    if 0 < int(div_text) < 1000:
        to_return = True  # Set return value to True if the score is valid
    
    # Return the result of the check
    return to_return

# Main function to call the test and print the result
def main_function():
    # Initialize the return value as -1 (indicating an error by default)
    to_return = -1
    
    # If the score service test passes (returns True)
    if test_scores_service():
        print("ok")  # Print "ok"
        to_return = 0  # Set return value to 0 (indicating success)
    
    # Return the final result
    return to_return

# Call the main function
main_function()
