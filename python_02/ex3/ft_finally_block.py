#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("===\tGarden Watering System\t===\n")
    print("Testing normal watering...")
    plants_1 = ["tomato", "lettuce", "carrots"]
    water_plants(plants_1)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plants_2 = ["tomato", None]
    water_plants(plants_2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
