import random


def generate_number(difficulty):
    """
    Generates a random number between 0 and the specified difficulty.
    """
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    """
    Prompts the user to input a number within the range of 0 to the difficulty.
    Returns the entered number as an integer.
    """
    while True:
        try:
            user_guess = int(input(f"Guess a number between 0 and {difficulty}: "))
            if 0 <= user_guess <= difficulty:
                return user_guess
            else:
                print(f"Please enter a number between 0 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(secret_number, user_guess):
    """
    Compares the secret number with the user's guess.
    Returns True if they match, False otherwise.
    """
    return secret_number == user_guess


def play(difficulty):
    """
    Initiates the game by generating a number, getting the user's guess,
    comparing the results, and returning True if the user wins, or False if they lose.
    """
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    is_correct = compare_results(secret_number, user_guess)

    if is_correct:
        print("Congratulations! You've guessed the correct number!")
        return True
    else:
        print(f"Sorry, you guessed wrong. The correct number was {secret_number}.")
        return False
