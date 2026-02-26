#!/usr/bin/env python3
import sys


def score_analysis() -> None:
    print("===\tPlayer Score Analytics\t===")

    argc = len(sys.argv)
    if argc == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    numbers = [0] * (argc - 1)
    try:
        for i in range(1, argc):
            numbers[(i - 1)] = int(sys.argv[i])
    except ValueError:
        print(f"Use numbers only. Invalid input of '{sys.argv[i]}'")
        return

    print(f"Scores processed: {numbers}")
    total = sum(numbers)
    average = total / (argc - 1)
    high = max(numbers)
    low = min(numbers)
    s_range = high - low
    print(f"Total players: {argc - 1}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {s_range}\n")


if __name__ == "__main__":
    score_analysis()
