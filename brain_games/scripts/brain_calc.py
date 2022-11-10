#!/usr/bin/env python3


from brain_games.games.base_logic import launch_game
from brain_games.games import calc


def main():
    launch_game(calc)


if __name__ == '__main__':
    main()
