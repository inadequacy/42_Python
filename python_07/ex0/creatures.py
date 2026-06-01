#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        self.cr_name = cr_name
        self.cr_type = cr_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.cr_name} is a {self.cr_type} type Creature."


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.cr_name} uses Ember."


class Pyrodan(Creature):
    def attack(self) -> str:
        return f"{self.cr_name} uses Flamethrower."


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.cr_name} uses Watergun."


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.cr_name} uses Hydropump."


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> None:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> None:
        return Pyrodan("Pyrodan", "Fire")


class AquaFactory(CreatureFactory):
    def create_base(self) -> None:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> None:
        return Torragon("Torragon", "Water")
