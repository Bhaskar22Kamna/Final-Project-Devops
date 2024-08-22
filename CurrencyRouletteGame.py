# 1. get_money_interval - Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for a given difficulty d, and total value of money t, the interval will be: (t - (5 - d), t + (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of value 
# for a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user lost or won.

import random
import requests, json
from GuessGame import generate_number, get_guess_from_user

# Function to get the current exchange rate from USD to ILS
def getCurrencyRate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    # Send a GET request to the exchange rate API
    response = requests.get(url, verify=False)
    print(f'response is {response}')
    # Return the exchange rate from USD to ILS
    return response.json()['rates']['ILS']

# Function to calculate the interval for the correct guess
def get_money_interval(total_value_of_money, difficulty):
    t = total_value_of_money
    d = 6 - difficulty  # Adjust interval based on difficulty
    # Calculate the upper and lower bounds of the interval
    toRet0 = t + d
    toRet1 = t - d
    return toRet0, toRet1

# Main function to play the Currency Roulette game
def play_currency(difficulty):
    # Currency codes for conversion
    from_currency = "USD"
    to_currency = "ILS"
    # API key for the currency conversion service
    api_key = "3JKXC3A97NMG380H"
    status = False  # Initialize game status as False (not won)
    
    # Get the current currency exchange rate from USD to ILS
    currentCurrencyExchangeRate = getCurrencyRate()
    
    # Prompt the user for an amount in USD
    number_message = "amount in USD:"
    generate_number_amount_in_USD = generate_number(number_message, 101)
    
    # Convert the amount from USD to ILS
    amount_in_ILS = currentCurrencyExchangeRate * generate_number_amount_in_USD
    
    # Prompt the user to guess the total value in ILS
    guess_amount_of_money = get_guess_from_user("Please choose total value of money in ILS: ")
    
    # Calculate the correct interval for the guess based on difficulty
    get_money_interval_amount0, get_money_interval_amount1 = get_money_interval(amount_in_ILS, difficulty)
    
    # Print the calculated interval for debugging purposes
    print(get_money_interval_amount0)
    print(get_money_interval_amount1)
    
    # Check if the user's guess is within the interval
    if get_money_interval_amount1 <= guess_amount_of_money <= get_money_interval_amount0:
        print("you win")
        status = True  # Set status to True if the guess is correct
    else:
        print("you lost")
    
    # Return the game status (True if won, False if lost)
    return status

# Function to get real-time currency exchange rate using an API (alternative method)
def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key):
    # Base URL for the currency exchange API
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    # Complete URL for the API request
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
  
    # Send a GET request to the API
    req_ob = requests.get(main_url) 
  
    # Parse the JSON response into a Python dictionary
    result = req_ob.json()
  
    # Extract the exchange rate from the response
    currencyExchangeRate = result["Realtime Currency Exchange Rate"]['5. Exchange Rate']
    
    # Return the exchange rate
    return currencyExchangeRate
