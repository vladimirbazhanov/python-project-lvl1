import prompt
from random import randint, choice
from brain_games.cli import welcome_user, greet_user, get_username
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER, ROUNDS_COUNT


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
    print('What is the result of the expression?')


def build_questions_and_correct_answer():
    operations = ['+', '-', '*']
    value1 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    value2 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)

    question = ' '.join([str(value1), choice(operations), str(value2)])
    correct_answer = str(eval(question))

    return question, correct_answer
