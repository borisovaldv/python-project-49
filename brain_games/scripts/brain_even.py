#!/usr/bin/env python3


from brain_games.games.even import get_question_and_answer
from brain_games.games.base_logic import launch_game


def main():
    launch_game(get_question_and_answer)


if __name__ == '__main__':
    main()
