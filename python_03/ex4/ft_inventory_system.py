#!/usr/bin/env python3
import sys


def fill_inventory(argv: list) -> dict:
    inventory = {}
    for item in argv[1:]:
        if ":" not in item:
            print(f"Error: Invalid format for '{item}'.\
                   Expected 'name:quantity'.")
            continue
        try:
            name, quantity_str = item.split(":", 1)
            if not name:
                print(f"Error: Missing item name in '{item}'")
                continue
            quantity = int(quantity_str)
            inventory.update({name: quantity})
        except ValueError:
            print(f"Error: Quantity for '{name}' must be a whole number \
                  (got '{quantity_str}').")
            continue
    return inventory


def inventory() -> None:
    print("===\tInventory System Analysis\t===")
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        return
    inventory = fill_inventory(sys.argv)
    total = 0
    for key in inventory:
        total += inventory.get(key)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n===\tCurrent Inventory\t\t===")
    for key in inventory:
        amount = inventory.get(key)
        unit = "units"
        if amount == 1:
            unit = "unit"
        percentage = (amount / total) * 100
        print(f"{key}: {amount} {unit} ({percentage:.1f}%)")

    print("\n===\tInventory Statistics\t\t===")
    most = None, None
    least = None, None
    for key, value in inventory.items():
        if most[1] is None or most[1] < value:
            most = key, value
        if least[1] is None or least[1] > value:
            least = key, value
    unit_m = "units"
    if most[1] == 1:
        unit_m = "unit"
    unit_l = "units"
    if least[1] == 1:
        unit_l = "unit"
    print(f"Most abundant: {most[0]} ({most[1]} {unit_m})")
    print(f"Least abundant: {least[0]} ({least[1]} {unit_l})")

    print("\n===\tItem Categories\t\t\t===")
    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }
    for item, quantity in inventory.items():
        if quantity > 9:
            categories["Abundant"][item] = quantity
        elif quantity > 4:
            categories["Moderate"][item] = quantity
        else:
            categories["Scarce"][item] = quantity
    for category in categories:
        if not categories.get(category):
            continue
        print(f"{category}: {categories.get(category)}")

    print("\n===\tManagement Suggestions\t\t===")
    restock = ""
    for key, value in inventory.items():
        if value == 1 and restock == "":
            restock = restock + key
        elif value == 1:
            restock = restock + ", " + key
    print(f"Restock needed: {restock}")

    print("\n===\tDictionary Properties Demo\t===")
    keys = ""
    for key in inventory.keys():
        if keys == "":
            keys = key
        else:
            keys = keys + ", " + key
    values = ""
    for value in inventory.values():
        if values == "":
            values = str(value)
        else:
            values = values + ", " + str(value)
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    exists = True if inventory.get("sword") else False
    print(f"Sample lookup - 'sword' is in inventory: {exists}")


if __name__ == "__main__":
    inventory()
