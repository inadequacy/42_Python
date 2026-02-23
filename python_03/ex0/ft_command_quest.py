#!/usr/bin/env python3
import sys


class TooFew(Exception):
    pass


def command_quest() -> None:
    argc = len(sys.argv)
    print("===\tCommand Quest\t===")
    try:
        if argc == 1:
            raise TooFew
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    except TooFew:
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
    finally:
        print(f"Total arguments: {argc}")


if __name__ == "__main__":
    command_quest()
