#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, element: str) -> None:
        self.name: name
        self.type: element

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"My name is {self.name} and my type is {self.type}."


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember."


class Pyrodan(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower."


if __name__ == "__main__":
    Creature("Flameling", "Fire", self.attack("Ember"))

