import prompt
from brain_games.cli import welcome_user, get_username
from random import randint

MIN_ASKED_NUMBER = 1
MAX_ASKED_NUMBER = 25
ROUNDS_COUNT = 3


def start_game():
    welcome_user()
    username = get_username()

    print_info()

    current_round = 1

    while current_round <= ROUNDS_COUNT:
        asked_number = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
        correct_answer = 'yes' if asked_number % 2 == 0 else 'no'

        print(f'Question: {asked_number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'."
            )
            print(f'Let\'s try again, {username}!')

            return

        current_round += 1

    print(f'Congratulations, {username}!')


def print_info():
    print('Answer "yes" if the number is even, otherwise answer "no".')
