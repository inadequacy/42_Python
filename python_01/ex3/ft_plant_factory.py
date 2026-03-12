#!/usr/bin/env python3

def plant_created(name: str, height: int, span: int) -> None:
    print(f"Created: {name.capitalize()} ({str(height)}cm, {str(span)} days)")


class Plant:
    def __init__(self, name: str, height: int, span: int) -> None:
        self.name = name
        self.height = height
        self.span = span
        plant_created(name, height, span)

    def grow(self, length: int) -> None:
        self.height += length

    def age(self, days: int) -> None:
        self.span += days

    def get_info(self) -> None:
        return ([self.height, self.span])


def ft_plant_factory() -> None:
    print("===\tPlant Factory Ouput\t===")
    rose = Plant("rose", 25, 30)
    oak = Plant("oak", 200, 365)
    cactus = Plant("cactus", 5, 90)
    sunflower = Plant("sunflower", 80, 45)
    fern = Plant("fern", 15, 120)
    plist = [rose, sunflower, cactus, oak, fern]
    print(f"\nTotal plants created: {len(plist)}")


if __name__ == "__main__":
    ft_plant_factory()
