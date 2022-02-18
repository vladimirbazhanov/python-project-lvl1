from random import randint, choice
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER
from operator import add, sub, mul

GAME_RULES = 'What is the result of the expression?'


def build_question_with_answer():
    operations = ['+', '-', '*']
    value1 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    value2 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)

    chosen_operation = choice(operations)

    question = ' '.join([str(value1), chosen_operation, str(value2)])

    if chosen_operation == '+':
        correct_answer = add(value1, value2)
    elif chosen_operation == '-':
        correct_answer = sub(value1, value2)
    elif chosen_operation == '*':
        correct_answer = mul(value1, value2)

    return question, str(correct_answer)
