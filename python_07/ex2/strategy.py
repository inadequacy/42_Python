from abc import ABC, abstractmethod
from ex0 import creature
from ex1 import heal_ability, transform_ability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature):
        creature.attack()

    def is_valid(self, creature):
        if creature:
            return True
        else:
            return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature):
        return super().act(creature)

    def is_valid(self, creature):
        if creature.__class__ == 'ex1.capabilities.Shiftling' or \
           creature.__class__ == 'ex1.capabilities.Morphagon':
            return True
        else:
            return False
