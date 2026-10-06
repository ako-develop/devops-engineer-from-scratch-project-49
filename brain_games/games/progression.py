import random

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 50
MIN_STEP = 2
MAX_STEP = 10
HIDDEN_SIGN = '..'


def build_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = build_progression(start, step, PROGRESSION_LENGTH)

    hidden_index = random.randrange(PROGRESSION_LENGTH)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = HIDDEN_SIGN

    question = ' '.join(map(str, progression))
    return question, correct_answer
