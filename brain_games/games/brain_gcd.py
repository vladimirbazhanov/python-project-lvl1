from math import gcd
from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def build_question_with_answer(minimum, maximum):
    value1 = randint(minimum, maximum)
    value2 = randint(minimum, maximum)

    question = ' '.join([str(value1), str(value2)])
    correct_answer = str(gcd(value1, value2))

    return question, correct_answer
