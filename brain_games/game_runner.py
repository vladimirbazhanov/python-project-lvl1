import prompt

ROUNDS_COUNT = 3
MIN_ASKED_NUMBER = 1
MAX_ASKED_NUMBER = 25


def run_game(game_engine):
    welcome_user()
    username = get_username()
    greet_user(username)

    print(game_engine.GAME_RULES)

    current_round = 1

    while current_round <= ROUNDS_COUNT:
        question, correct_answer = game_engine.build_question_with_answer(
            MIN_ASKED_NUMBER,
            MAX_ASKED_NUMBER
        )

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. ",
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {username}!')

            return

        current_round += 1

    print(f'Congratulations, {username}!')


def welcome_user():
    print('Welcome to the Brain Games!')


def greet_user(username):
    print(f'Hello, {username}!')


def get_username():
    return prompt.string('May I have your name? ')
