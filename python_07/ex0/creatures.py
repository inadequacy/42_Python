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


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, base: class) -> None:
        pass
    
    @abstractmethod
    def create_evolved(self, evolved: class) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, base: class) -> None:
        self.base = base

    def create_evolved(self, evolved: class) -> None:
        self.evolved = evolved


class AquaFactory(CreatureFactory):
    def create_base(self, base: class) -> None:
        self.base = base

    def create_evolved(self, evolved: class) -> None:
        self.evolved = evolved


if __name__ == "__main__":
    Creature("Flameling", "Fire", self.attack("Ember"))

