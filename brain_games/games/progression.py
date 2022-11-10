import random
from brain_games.games.const import HIDDEN_NUM, RANGE, STEP_RANGE, PROG_LEN

DESCRIPTION = 'What number is missing in the progression?'


def set_progression(random_progression):
    random_hidden_num = random.randint(0, PROG_LEN - 1)
    right_answer = random_progression[random_hidden_num]
    random_progression[random_hidden_num] = HIDDEN_NUM
    return random_progression, str(right_answer)


def get_question_and_answer():
    random_progression = []
    random_num = random.randint(RANGE[0], RANGE[1])
    step = random.randint(STEP_RANGE[0], STEP_RANGE[1])
    for _ in range(PROG_LEN):
        random_progression.append(random_num)
        random_num += step
    question, right_answer = set_progression(random_progression)
    return ' '.join(str(i) for i in question), right_answer
