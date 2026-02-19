#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __str__(self) -> str:
        return f"Caught WaterError: {self.message}"


def check_wilting(wilting: bool) -> None:
    if wilting:
        raise PlantError("The tomato plant is wilting!")


def check_watering_can(litres: int) -> None:
    if litres < 6:
        raise WaterError("Not enough water in the tank!")


def error_testing() -> None:
    print("===\tCustom Garden Errors Demo\t\t===\n")
    print("Testing PlantError...")
    try:
        check_wilting(True)
    except PlantError as err:
        print(f"Caught PlantError: {err}\n")
    print("Testing WaterError...")
    try:
        check_watering_can(5)
    except WaterError as err:
        print(f"Caught WaterError: {err}\n")
    print("Testing catching all garden errors...")
    try:
        check_wilting(True)
    except GardenError as err:
        print(f"Caught a garden error: {err}")
    try:
        check_watering_can(5)
    except GardenError as err:
        print(f"Caught a garden error: {err}")
    print("\n===\tAll custom error types work correctly!\t===")


if __name__ == "__main__":
    error_testing()
