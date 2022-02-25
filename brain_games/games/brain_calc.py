from random import randint, choice
import operator

GAME_RULES = 'What is the result of the expression?'


def build_question_with_answer(minimum, maximum):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    value1 = randint(minimum, maximum)
    value2 = randint(minimum, maximum)

    chosen_operation = choice(list(operations.keys()))

    question = ' '.join([str(value1), chosen_operation, str(value2)])

    correct_answer = operations[chosen_operation](value1, value2)

    return question, str(correct_answer)
