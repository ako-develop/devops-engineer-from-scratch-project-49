import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    second = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{first} {second}'
    correct_answer = str(math.gcd(first, second))
    return question, correct_answer
