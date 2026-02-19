#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if not plant_name or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level <= 1 or water_level >= 10:
            w = water_level
            if water_level >= 10:
                raise ValueError(f"Water level {w} is too high (max 10)")
            if water_level <= 1:
                raise ValueError(f"Water level {w} is too low (min 2)")
        if sunlight_hours <= 2 or sunlight_hours >= 12:
            s = sunlight_hours
            if sunlight_hours <= 2:
                raise ValueError(f"Sunlight hours {s} is too low (min 2)")
            if sunlight_hours >= 12:
                raise ValueError(f"Sunlight hours {s} is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("===\tGarden Plant Health Checker\t===\n")
    print("Testing good values...")
    check_plant_health("tomato", 5, 8)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 8)
    print("\nTesting bad water level...")
    check_plant_health("rose", 15, 8)
    print("\nTesting bad sunlight hours...")
    check_plant_health("daisy", 5, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
