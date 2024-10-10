import random
import time


def generate_sequence(difficulty):
    """
    Generates a list of random numbers between 1 and 101, with a length equal
    to the specified difficulty.
    """
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    """
    Prompts the user to input a list of numbers matching the length of the
    generated sequence.
    """
    print(f"Please enter {difficulty} numbers separated by spaces:")
    while True:
        try:
            user_input = input("Your guess: ")
            # Convert input to a list of integers
            user_list = list(map(int, user_input.split()))

            # Check if the user entered the correct number of items
            if len(user_list) == difficulty:
                return user_list
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Make sure to enter numbers separated by spaces.")


def is_list_equal(sequence, user_list):
    """
    Compares the generated sequence with the user's input and returns True if
    they are identical, False otherwise.
    """
    return sequence == user_list


def play(difficulty):
    """
    Executes the game by generating a sequence of random numbers, displaying
    them for a brief time, and then asking the user to recall the numbers.
    Returns True if the user's input matches the sequence, otherwise False.
    """
    sequence = generate_sequence(difficulty)
    print(f"Remember this sequence: {sequence}")
    time.sleep(0.7)  # Wait for 0.7 seconds before clearing the screen
    print("\033c", end="")  # Clears the screen (works in Unix-based terminals like Linux and macOS)

    user_list = get_list_from_user(difficulty)
    is_correct = is_list_equal(sequence, user_list)

    if is_correct:
        print("Congratulations! You remembered the sequence correctly.")
        return True
    else:
        print("Sorry, that was not the correct sequence.")
        print(f"The correct sequence was: {sequence}")
        return False
