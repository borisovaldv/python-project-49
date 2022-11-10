import random
from brain_games.games.const import OPERATIONS, RANGE_FOR_CALC, OPERATORS

GAME_DESCRIPTION = 'What is the result of the expression?'


def get_random_expression(first_number, second_number):
    random_operator = random.choice(OPERATORS)
    operation = OPERATIONS[random_operator]
    right_answer = operation(first_number, second_number)
    return str(right_answer), random_operator


def get_question_and_answer():
    first_number = random.randint(RANGE_FOR_CALC[0], RANGE_FOR_CALC[1])
    second_number = random.randint(RANGE_FOR_CALC[0], RANGE_FOR_CALC[1])
    right_answer, random_operator = get_random_expression(first_number, second_number)
    question = f'{first_number} {random_operator} {second_number}'
    return question, right_answer
