from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.form = "normal"

    @abstractmethod
    def transform(self) -> str:
        return

    @abstractmethod
    def revert(self) -> str:
        return


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.cr_name} uses Vine Whip."

    def heal(self, target) -> str:
        return f"{self.cr_name} heals itself for a small amount."


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.cr_name} uses Petal Dance."

    def heal(self, target) -> str:
        return f"{self.cr_name} heals itself and others for a large amount."


class Shiftling(Creature, TransformCapability):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        super().__init__(cr_name, cr_type)
        self.form = "normal"

    def attack(self) -> str:
        if self.form == "normal":
            return f"{self.cr_name} attacks normally."
        elif self.form == "sharper":
            return f"{self.cr_name} performs a boosted strike!"

    def transform(self) -> str:
        self.form = "sharper"
        return f"{self.cr_name} shifts into a sharper form!"

    def revert(self) -> str:
        self.form = "normal"
        return f"{self.cr_name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        super().__init__(cr_name, cr_type)
        self.form = "normal"

    def attack(self) -> str:
        if self.form == "normal":
            return f"{self.cr_name} attacks normally."
        elif self.form == "draconic":
            return f"{self.cr_name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.form = "draconic"
        return f"{self.cr_name} morphs into a draconic battle form!"

    def revert(self) -> str:
        self.form = "normal"
        return f"{self.cr_name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self):
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self):
        return Morphagon("Morphagon", "Normal/Dragon")
