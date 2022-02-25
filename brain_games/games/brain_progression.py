from random import randint
GAME_RULES = 'What number is missing in the progression?'


def build_question_with_answer(minimum, maximum):
    progression = build_progression(minimum, maximum)

    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'

    question = ' '.join(progression)

    return question, correct_answer


def build_progression(minimum, maximum):
    start = randint(minimum, maximum)
    step = randint(2, 8)
    length = randint(5, 10)

    progression = list(range(start, (start + length * step), step))
    progression = [str(i) for i in progression]

    return progression
