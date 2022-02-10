from random import randint
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def print_game_rules():
    print(GAME_RULES)


def build_questions_and_correct_answer():
    question = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer
