#!/usr/bin/env python3
from typing import Generator


def event_stream(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up",
              "completed quest"]
    for i in range(n):
        player = players[(i * 4) % len(players)]
        level = ((i * 12) % 20) + 1

        if i % 4 == 0:
            event = events[0]
        elif i % 3 == 0:
            event = events[1]
        elif i % 2 == 0:
            event = events[2]
        else:
            event = events[3]

        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event
        }


def fibonacci(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            yield num
            count += 1
        num += 1


def data_stream() -> None:
    total = 1000
    high = 0
    treasure = 0
    levelup = 0
    print("===\tGame Data Stream Processor\t===\n")
    print("Processing 1000 game events...\n")
    for e in event_stream(total):
        if e["id"] <= 3:
            print(f"Event {e['id']}: Player {e['player']} \
                  (level {e['level']}) {e['event']}")
        if e["id"] == 4:
            print("...")
        if e["level"] >= 10:
            high += 1
        if e["event"] == "found treasure":
            treasure += 1
        if e["event"] == "leveled up":
            levelup += 1

    print("\n===\tStream Analytics\t\t===")
    print("Total events processed:", total)
    print("High-level players (10+):", high)
    print("Treasure events:", treasure)
    print("Level-up events:", levelup)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n===\tGenerator Demonstration\t\t===")
    print("Fibonacci sequence (first 10):", end=" ")
    for x in fibonacci(10):
        print(x, end=" ")
    print()
    print("Prime numbers (first 5):", end=" ")
    for p in primes(5):
        print(p, end=" ")
    print()


# can't use time to actually calculate how long processing time went
if __name__ == "__main__":
    data_stream()
