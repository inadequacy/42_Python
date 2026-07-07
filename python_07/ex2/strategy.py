from abc import ABC, abstractmethod
from ex0 import creature
from ex1 import heal_ability, transform_ability


class BattleException(Exception):
    def __init__(self):
        super().__init__(self.message)
        self.message = "Battle error, aborting tournament: Invalid Creature" \
                       "strategy combination"

class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature):
        print(creature.attack())

    def is_valid(self, creature):
        if creature:
            return True
        else:
            return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature):
        if creature.__class__ == 'ex1.capabilities.Shiftling' or \
           creature.__class__ == 'ex1.capabilities.Morphagon':
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature):
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature):
        if creature.__class__ == 'ex1.capabilities.Sproutling' or \
           creature.__class__ == 'ex1.capabilities.Bloomelle':
            return True
        else:
            return False
