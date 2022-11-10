import random
from brain_games.games.const import OPERATIONS, RANGE_FOR_CALC, OPERATORS

DESCRIPTION = 'What is the result of the expression?'


def get_random_expression(first_number, second_number):
    rdm_op = random.choice(OPERATORS)
    operation = OPERATIONS[rdm_op]
    right_answer = operation(first_number, second_number)
    return str(right_answer), rdm_op


def get_question_and_answer():
    first_number = random.randint(RANGE_FOR_CALC[0], RANGE_FOR_CALC[1])
    second_number = random.randint(RANGE_FOR_CALC[0], RANGE_FOR_CALC[1])
    right_answer, rdm_op = get_random_expression(first_number, second_number)
    question = f'{first_number} {rdm_op} {second_number}'
    return question, right_answer
