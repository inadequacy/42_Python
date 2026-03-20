#!/usr/bin/env python3

def function() -> None:
    to_open = "./ancient_fragment.txt"
    try:
        file = open(to_open, "r")
    except (UnboundLocalError, FileNotFoundError, TypeError):
        print("ERROR: Storage vault not found. Run generator first")
        return
    print(f"Storage accessed: {to_open}")
    content = file.read()
    print(f"Recovered Data: \n{content}")
    file.close()
    print("Storage unit closed.")


if __name__ == "__main__":
    function()
