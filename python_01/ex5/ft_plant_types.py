#!/usr/bin/env python3

def print_plant_info(self, name: str, height: int, age: int, other) -> None:
    p_name = name.capitalize()
    class_name = self.__class__.__name__
    var = ""
    if class_name == 'Flower':
        var = " color"
    elif class_name == 'Tree':
        var = "cm diameter"
    print(f"{p_name} ({class_name}): {height}cm, {age} days, {other}{var}")


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print_plant_info(self, name, height, age, color)

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: str) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print_plant_info(self, name, height, age, trunk_diameter)

    def produce_shade(self) -> None:
        square = int(self.trunk_diameter * 1.56)
        cap_name = self.name.capitalize()
        print(f"{cap_name} provides {square} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, season: str, nutri: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutri
        print_plant_info(self, name, height, age, season)


def ft_plant_types() -> None:
    print("===\tGarden Plant Types\t===\n")
    rose = Flower("rose", 25, 30, "red")
    rose.bloom()
    hibiscus = Flower("hibiscus", 60, 10, "orange")
    hibiscus.bloom()
    print("")
    oak = Tree("oak", 500, 1825, 50)
    oak.produce_shade()
    maple = Tree("maple", 120, 730, 20)
    maple.produce_shade()
    print("")
    tomato = Vegetable("tomato", 80, 90, "summer harvest", "vitamin C")
    brocc = Vegetable("broccoli", 75, 60, "spring harvest", "vitamin K")
    print(f"{tomato.name.capitalize()} is rich in {tomato.nutritional_value}")
    print(f"{brocc.name.capitalize()} is rich in {brocc.nutritional_value}")


if __name__ == "__main__":
    ft_plant_types()
