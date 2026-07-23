from abc import ABC, abstractmethod
from typing import Any
from ex0 import creature
from ex1 import heal_ability, transform_ability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: creature) -> bool:
        pass


class BattleException(Exception):
    def __init__(self, creature: creature, strategy: BattleStrategy) -> None:
        self.message = "Battle error, aborting tournament:"
        self.creature = creature
        self.strategy = strategy

    def __str__(self) -> str:
        return f"{self.message} Invalid Creature '{self.creature.cr_name}' " \
               f"for this {self.strategy}"


class NormalStrategy(BattleStrategy):
    def act(self, creature: creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise BattleException(creature, self)

    def is_valid(self, creature: creature) -> bool:
        return bool(creature)

    def __str__(self):
        return "normal strategy"


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: transform_ability) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise BattleException(creature, self)

    def is_valid(self, creature: creature) -> bool:
        return isinstance(creature, transform_ability)

    def __str__(self):
        return "aggressive strategy"


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: heal_ability) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise BattleException(creature, self)

    def is_valid(self, creature: creature) -> bool:
        return isinstance(creature, heal_ability)

    def __str__(self):
        return "defensive strategy"
