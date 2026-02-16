#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    rose = Plant("Rose", "25", "30")
    sunflower = Plant("Sunflower", "80", "45")
    cactus = Plant("Cactus", "15", "120")
    plist = [rose, sunflower, cactus]

    print("===\tGarden Plant Registry\t===")
    for p in plist:
        days = "days"
        if p.age == "1":
            days = "day"
        print(f"{p.name.capitalize()}: {p.height}cm, {p.age} {days} old")


if __name__ == "__main__":
    ft_garden_data()
