from utils import BAD_RETURN_CODE

SCORES_FILE_NAME = "Scores.txt"


def calculate_points(difficulty):
    return (difficulty * 3) + 5


def add_score(difficulty):
    try:
        difficulty = int(difficulty)
    except ValueError:
        print("Invalid difficulty level. Must be an integer.")
        return

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + calculate_points(difficulty)

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))

    print(f"New score: {new_score}")
