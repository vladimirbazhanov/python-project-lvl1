import prompt
from random import randint
from brain_games.cli import welcome_user, greet_user, get_username
from brain_games.settings import MIN_ASKED_NUMBER,\
    MAX_ASKED_NUMBER, ROUNDS_COUNT


def start_game():
    welcome_user()
    username = get_username()
    greet_user(username)

    print_game_rules()

    current_round = 1

    while current_round <= ROUNDS_COUNT:
        question, correct_answer = build_questions_and_correct_answer()

        print(f'Question: {question}')
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


def print_game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def build_questions_and_correct_answer():
    question = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer
