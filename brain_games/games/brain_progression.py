from random import randint


GAME_RULES = 'What number is missing in the progression?'


def print_game_rules():
    print(GAME_RULES)


def build_questions_and_correct_answer():
    start = randint(1, 25)
    step = randint(2, 8)
    length = randint(5, 10)

    question = []
    while length > 0:
        question.append(start + step)
        start += step
        length -= 1

    index = randint(0, len(question) - 1)
    correct_answer = str(question[index])
    question[index] = '..'

    return question, correct_answer
