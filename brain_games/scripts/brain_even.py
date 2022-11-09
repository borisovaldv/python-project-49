#!/usr/bin/env python3


from brain_games.games.even import is_even, get_random_number
from brain_games.games.base_logic import launch_game


def main():
    launch_game(get_random_number)


if __name__ == '__main__':
    main()
