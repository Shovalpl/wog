from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette_game


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

    # Call the appropriate game function based on the user's choice
    if game_choice == '1':
        play_memory_game(difficulty)
    elif game_choice == '2':
        play_guess_game(difficulty)
    elif game_choice == '3':
        play_currency_roulette_game(difficulty)

