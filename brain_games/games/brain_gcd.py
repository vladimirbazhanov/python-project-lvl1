from math import gcd
from random import randint
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def build_question_with_answer():
    value1 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    value2 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)

    question = ' '.join([str(value1), str(value2)])
    correct_answer = str(gcd(value1, value2))

    return question, correct_answer
