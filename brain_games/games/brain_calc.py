from random import randint, choice
from operator import add, sub, mul

GAME_RULES = 'What is the result of the expression?'


def build_question_with_answer(minimum, maximum):
    operations = ['+', '-', '*']
    value1 = randint(minimum, maximum)
    value2 = randint(minimum, maximum)

    chosen_operation = choice(operations)

    question = ' '.join([str(value1), chosen_operation, str(value2)])

    if chosen_operation == '+':
        correct_answer = add(value1, value2)
    elif chosen_operation == '-':
        correct_answer = sub(value1, value2)
    elif chosen_operation == '*':
        correct_answer = mul(value1, value2)

    return question, str(correct_answer)
