#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp_no = int(temp_str)
        if temp_no < 0 or temp_no > 40:
            raise ArithmeticError
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    except ArithmeticError:
        if temp_no < 0:
            print(f"Error: {temp_no} is too cold for plants (min 0°C)\n")
        if temp_no > 40:
            print(f"Error: {temp_no} is too hot for plants (max 40°C)\n")
    else:
        print(f"Temperature {temp_str} is perfect for plants!\n")
    finally:
        pass


def test_temperature_input():
    print("===\tGarden Temperature Checker\t\t\t===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("===\tAll tests completed - program didn't crash\t===")

if __name__ == "__main__":
    #check_temperature(input("Testing temperature: "))
    test_temperature_input()
