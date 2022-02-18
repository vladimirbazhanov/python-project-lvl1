import prompt
from brain_games.shared import welcome_user, greet_user, get_username
from brain_games.settings import ROUNDS_COUNT


def run_game(game_engine):
    welcome_user()
    username = get_username()
    greet_user(username)

    print(game_engine.GAME_RULES)

    current_round = 1

    while current_round <= ROUNDS_COUNT:
        question, correct_answer = game_engine.build_question_with_answer()

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
