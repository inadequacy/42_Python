#!/usr/bin/env python3

def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        (5 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        name = "missing.txt"
        open(name, "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file '{name}'\n")
    try:
        print("Testing KeyError...")
        nursery = {}
        nursery["cactus"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        nursery = {}
        open(nursery["cactus"], "r")
        int(10 / 0)
    except (ValueError, KeyError,
            ZeroDivisionError,
            FileNotFoundError):
        print("Caught an error, but program continues!\n")
    else:
        pass
    finally:
        pass


def test_error_types() -> None:
    print("===\tGarden Error Types Demo\t===\n")
    garden_operations()
    print("All error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
