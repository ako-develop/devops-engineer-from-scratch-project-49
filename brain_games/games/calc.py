import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 50
OPERATIONS = ('+', '-', '*')


def calculate(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case _:
            raise ValueError(f'Unknown operation: {operation}')


def generate_round():
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    second = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)

    question = f'{first} {operation} {second}'
    correct_answer = str(calculate(first, second, operation))
    return question, correct_answer
