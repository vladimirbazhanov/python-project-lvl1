from random import randint


GAME_RULES = 'What number is missing in the progression?'


def print_game_rules():
    print(GAME_RULES)


def build_question_with_answer():
    question = build_question()

    index = randint(0, len(question) - 1)
    correct_answer = str(question[index])
    question[index] = '..'
    question = ' '.join(question)

    return question, correct_answer


def build_question():
    start = randint(1, 25)
    step = randint(2, 8)
    length = randint(5, 10)

    question = []
    while length > 0:
        question.append(str(start + step))
        start += step
        length -= 1

    return question
