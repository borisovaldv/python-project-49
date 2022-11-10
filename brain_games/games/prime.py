import random
from brain_games.games.const import RANGE

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    for i in range(2, random_number):
        if (random_number % i) == 0:
            return 'no'
    return 'yes'


def get_question_and_answer():
    random_number = random.randint(RANGE[0] + 1, RANGE[1])
    right_answer = is_prime(random_number)
    return random_number, right_answer
