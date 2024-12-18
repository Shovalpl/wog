from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette_game
from score import add_score

user = input('Enter your name: ')


def welcome():
    return f'Hi {user}'


print(welcome())


def start_play():
    print('Please choose a game to play:')
    print('1. Memory Game, 2. Guess Game, 3. Currency Roulette')
    game_choice = input('Enter the number of the game you want to play: ')

    while True:
        # Check if the choice is one of the valid options
        if game_choice in ['1', '2', '3']:
            break
        else:
            print('Error! That is not the correct number. Please try again.')
            game_choice = input('Enter the number of the game you want to play: ')

    print('Please choose a difficulty:')
    print('1, 2, 3, 4, 5')
    difficulty_choice = input('Enter the number of the difficulty you want to play: ')

    while True:
        # Check if the choice is one of the valid difficulty levels
        if difficulty_choice in ['1', '2', '3', '4', '5']:
            difficulty = int(difficulty_choice)
            break
        else:
            print('Error! That is not the correct number. Please try again.')
            difficulty_choice = input('Enter the number of the difficulty you want to play: ')

    # Dictionary to map game choices to their respective play functions
    game_functions = {
        '1': play_memory_game,
        '2': play_guess_game,
        '3': play_currency_roulette_game
    }

    # Fetch and execute the appropriate game function
    selected_game = game_functions[game_choice]
    game_result = selected_game(difficulty)

    # If the user won, add the score
    if game_result:
        add_score(difficulty)
        print("Congratulations! You've won the game!")
    else:
        print("Sorry, you lost the game. Better luck next time!")

    play_again()


# Ask if the user wants to play another game
def play_again():
    while True:
        choice = input("Would you like to play another game? (yes/no): ").lower()
        if choice in ['yes']:
            start_play()
        if choice != ['yes']:
            print("Thank you for playing! Goodbye!")
            break  # Exit the loop if the user doesn't want to play again

