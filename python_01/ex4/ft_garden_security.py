#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name.capitalize()}")

    def set_height(self, height: int) -> None:
        if height > 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        return (self.__height)

    def set_age(self, age: int) -> None:
        if age > 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        return (self.__age)


def ft_plant_factory() -> None:
    print("===\tGarden Security System\t===")
    rose = SecurePlant("rose")
    rose.set_height(25)
    rose.set_age(30)
    r_name = rose.name.capitalize()
    r_height = rose.get_height()
    r_age = rose.get_age()
    print("")
    rose.set_height(-5)
    print(f"\nCurrent plant: {r_name} ({r_height}cm, {r_age} days)")


if __name__ == "__main__":
    ft_plant_factory()
