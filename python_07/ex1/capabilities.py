from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(Creature, ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(Creature, ABC):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        super().__init__(cr_name, cr_type)
        self.form = "normal"

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(HealCapability):
    def attack(self) -> str:
        return f"{self.cr_name} uses Vine Whip."

    def heal(self) -> str:
        return f"{self.cr_name} heals itself for a small amount."


class Bloomelle(HealCapability):
    def attack(self) -> str:
        return f"{self.cr_name} uses Petal Dance."

    def heal(self) -> str:
        return f"{self.cr_name} heals itself and others for a large amount."


class Shiftling(TransformCapability):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        super().__init__(cr_name, cr_type)
        self.form = "normal"

    def attack(self) -> str:
        if self.form == "normal":
            return f"{self.cr_name} attacks normally."
        elif self.form == "sharper":
            return f"{self.cr_name} performs a boosted strike!"
        else:
            return "wrong form."

    def transform(self) -> str:
        self.form = "sharper"
        return f"{self.cr_name} shifts into a sharper form!"

    def revert(self) -> str:
        self.form = "normal"
        return f"{self.cr_name} returns to normal."


class Morphagon(TransformCapability):
    def __init__(self, cr_name: str, cr_type: str) -> None:
        super().__init__(cr_name, cr_type)
        self.form = "normal"

    def attack(self) -> str:
        if self.form == "normal":
            return f"{self.cr_name} attacks normally."
        elif self.form == "draconic":
            return f"{self.cr_name} unleashes a devastating morph strike!"
        else:
            return "wrong form."

    def transform(self) -> str:
        self.form = "draconic"
        return f"{self.cr_name} morphs into a draconic battle form!"

    def revert(self) -> str:
        self.form = "normal"
        return f"{self.cr_name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "Normal/Dragon")
