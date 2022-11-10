import random
import math
from brain_games.games.const import RANGE

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_answer(first_number, second_number):
    return str(math.gcd(first_number, second_number))


def get_question_and_answer():
    first_number = random.randint(RANGE[0], RANGE[1])
    second_number = random.randint(RANGE[0], RANGE[1])
    question = f'{first_number} {second_number}'
    right_answer = get_answer(first_number, second_number)
    return question, right_answer
