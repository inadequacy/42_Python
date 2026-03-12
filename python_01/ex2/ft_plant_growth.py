#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, span: int) -> None:
        self.name = name
        self.height = height
        self.span = span

    def grow(self, length: int) -> None:
        self.height += length

    def age(self, days: int) -> None:
        self.span += days

    def get_info(self) -> None:
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
