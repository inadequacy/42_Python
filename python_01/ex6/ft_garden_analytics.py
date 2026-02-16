#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_description(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str, blooming=True) -> None:
        super().__init__(name, height)
        self.flower_color = color
        self.blooming = blooming

    def get_description(self) -> str:
        bloom_status = "blooming" if self.blooming else "not blooming"
        name = self.name
        height = self.height
        color = self.flower_color
        return f"- {name}: {height}cm, {color} flowers ({bloom_status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_description(self) -> str:
        base_desc = super().get_description()
        return f"{base_desc}, Prize points: {self.prize_points}"


class GardenManager:

    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0

        def record_addition(self) -> None:
            self.plants_added += 1

        def record_growth(self, amount: int) -> None:
            self.total_growth += amount

        def summary(self) -> str:
            added = self.plants_added
            growth = self.total_growth
            return f"Plants added: {added}, Total growth: {growth}cm"

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: str) -> None:
        self.plants.append(plant)
        self.stats.record_addition()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_garden_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth(1)

    def generate_report(self) -> int:
        print(f"===\t{self.owner}'s Garden Report\t===")
        print("Plants in garden:")
        regular = flowering = prize = 0
        total_score = 0

        for plant in self.plants:
            print(plant.get_description())
            total_score += plant.height

            if isinstance(plant, PrizeFlower):
                prize += 1
                total_score += plant.prize_points
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            else:
                regular += 1

        print("")
        print(self.stats.summary())
        r = regular
        f = flowering
        p = prize
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers\n")
        return total_score

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @classmethod
    def get_total_gardens(cls) -> int:
        return cls.total_gardens


# I've seen this be called a Demo (demonstrates what the program does)
if __name__ == "__main__":
    print("===\tGarden Management System Demo\t===\n")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print("")
    alice_garden.help_garden_grow()
    print("")
    alice_score = alice_garden.generate_report()
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    bob_garden.add_plant(Plant("Cactus", 92))
    bob_score = bob_garden.generate_report()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
