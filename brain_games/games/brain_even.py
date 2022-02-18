from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def build_question_with_answer(minimum, maximum):
    question = randint(minimum, maximum)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer
