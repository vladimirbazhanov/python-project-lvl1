from random import randint, choice
from brain_games.settings import MIN_ASKED_NUMBER, MAX_ASKED_NUMBER

GAME_RULES = 'What is the result of the expression?'


def print_game_rules():
    print(GAME_RULES)


def build_question_with_answer():
    operations = ['+', '-', '*']
    value1 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)
    value2 = randint(MIN_ASKED_NUMBER, MAX_ASKED_NUMBER)

    question = ' '.join([str(value1), choice(operations), str(value2)])
    correct_answer = str(eval(question))

    return question, correct_answer
