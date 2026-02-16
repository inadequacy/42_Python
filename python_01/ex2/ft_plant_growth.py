#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, span):
        self.name = name
        self.height = height
        self.span = span

    def grow(self, length):
        self.height += length

    def age(self, days):
        self.span += days

    def get_info(self):
        return [self.height, self.span]


def ft_plant_growth(time: int) -> None:
    rose = Plant("Rose", 25, 30)
    print("===\tDay 1\t===")
    print(f"{rose.name.capitalize()}: {rose.height}cm, {rose.span} days old")
    rose.grow(time)
    rose.age(time)
    print(f"===\tDay {1 + time}\t===")
    print(f"{rose.name.capitalize()}: {rose.height}cm, {rose.span} days old")
    print(f"Growth this week: +{time}cm")


if __name__ == "__main__":
    ft_plant_growth(6)
