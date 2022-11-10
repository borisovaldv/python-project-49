import random
from brain_games.games.const import RANGE

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def get_question_and_answer():
    random_number = random.randint(RANGE[0], RANGE[1])
    right_answer = is_even(random_number)
    return random_number, right_answer
