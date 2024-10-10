import random
import requests


def get_money_interval(difficulty):
    """
    Retrieves the current USD to ILS exchange rate and calculates an interval
    for the correct answer based on the game's difficulty level.
    """
    # Get the current USD to ILS exchange rate using a free currency API
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        exchange_rate = response.json().get('rates', {}).get('ILS', None)

        if exchange_rate is None:
            print("Error fetching exchange rate.")
            return None, None

        # Generate a random amount in USD between 1 and 100
        random_usd = random.randint(1, 100)
        converted_ils = random_usd * exchange_rate

        # Calculate the acceptable interval range based on difficulty
        allowed_difference = 10 - difficulty
        min_acceptable = converted_ils - allowed_difference
        max_acceptable = converted_ils + allowed_difference

        return min_acceptable, max_acceptable, random_usd

    except requests.RequestException as e:
        print(f"Error connecting to currency API: {e}")
        return None, None, None


def get_guess_from_user(random_usd):
    """
    Prompts the user to input a guess for the converted value of a specified
    amount in USD to ILS.
    """
    while True:
        try:
            guess = float(input(f"Guess the ILS value of {random_usd} USD: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def compare_results(guess, min_acceptable, max_acceptable):
    """
    Compares the user's guess to the acceptable interval and returns True if
    the guess is within the range, False otherwise.
    """
    return min_acceptable <= guess <= max_acceptable


def play(difficulty):
    """
    Executes the game by invoking the functions above and returns True if
    the user wins, and False if the user loses.
    """
    min_acceptable, max_acceptable, random_usd = get_money_interval(difficulty)

    # Check if the interval could be generated (to ensure API success)
    if min_acceptable is None or max_acceptable is None:
        print("Unable to start the game due to API issues.")
        return False

    user_guess = get_guess_from_user(random_usd)
    is_within_range = compare_results(user_guess, min_acceptable, max_acceptable)

    if is_within_range:
        print(f"Congratulations! Your guess of {user_guess} ILS was correct.")
        return True
    else:
        print(f"Sorry, your guess of {user_guess} ILS was incorrect.")
        print(f"The correct range was between {min_acceptable:.2f} ILS and {max_acceptable:.2f} ILS.")
        return False
