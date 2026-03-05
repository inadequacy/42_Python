#!/usr/bin/env python3
import sys
import math


def coordinate_system() -> None:
    argc = len(sys.argv)
    if argc != 4 and argc != 2:
        print("No coordinates provided. Usage: "
              "python3 ft_coordinate_system.py \"x,y,z\" or <x> <y> <z>...")
        return

    nbrs = [0] * 3
    if argc == 2:
        print(f"Parsing coordinates: \"{sys.argv[1]}\"")
        nbrs = tuple(sys.argv[1].split(",", 2))
    try:
        if argc == 4:
            nbrs = tuple([sys.argv[1], sys.argv[2], sys.argv[3]])
            for i in range(1, 3):
                int(sys.argv[i])
    except ValueError:
        print("Error parsing coordinates: "
              f"invalid literal for int() with base 10: '{sys.argv[i]}'")
        print("Error details - Type: ValueError, Args: "
              f"(\"invalid literal for int() with base 10: '{sys.argv[i]}'\")")
        return

    coords = f"{nbrs[0]}, {nbrs[1]}, {nbrs[2]}"
    x1: int = 0
    y1: int = 0
    z1: int = 0
    x2 = int(nbrs[0])
    y2 = int(nbrs[1])
    z2 = int(nbrs[2])
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    if argc == 4:
        print(f"Position created: ({coords})")
    else:
        print(f"Parsed position: ({coords})")
    print(f"Distance between (0, 0, 0) and ({coords}): {dist}")


if __name__ == "__main__":
    coordinate_system()
