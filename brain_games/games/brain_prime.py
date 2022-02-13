from random import randint
from math import sqrt
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def print_game_rules():
    print(GAME_RULES)


def build_question_with_answer():
    number = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer


def is_prime(number):
    if number <= 1:
        return False

    for d in range(2, int(sqrt(number) + 1)):
        if number % d == 0:
            return False
            break

    return True
