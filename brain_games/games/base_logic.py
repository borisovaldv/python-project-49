import prompt
from brain_games.games.const import ATTEMPTS
from brain_games.games.even import get_question_and_answer, GAME_DESCRIPTION


def welcome():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def launch_game(game):
    counter = 0
    name = welcome()
    print(GAME_DESCRIPTION)

    while counter < ATTEMPTS:
        question, right_answer = get_question_and_answer()
        print(f'Question: {question}')
        users_answer = prompt.string('Your answer: ')

        if users_answer != right_answer:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            break

        print('Correct!')
        counter += 1

    if counter == ATTEMPTS:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
