#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name = "Rose"
    height = "25"
    age = "30"

    print("===\tWelcome to My Garden\t===")
    print(f"Plant: {name}")
    print(f"Height: {height} cm")
    if age == "1":
        print(f"Age: {age} day")
    else:
        print(f"Age: {age} days")
    print("\n===\tEnd of program\t\t===")


if __name__ == "__main__":
    ft_garden_intro()
