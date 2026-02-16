def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        text = f"seeds: {quantity} {unit} available"
        print(f"{seed_type.capitalize()} {text}")
    elif unit == "grams":
        text = f"seeds: {quantity} {unit} total"
        print(f"{seed_type.capitalize()} {text}")
    elif unit == "area":
        text = f"seeds: covers {quantity} square meters"
        print(f"{seed_type.capitalize()} {text}")
    else:
        print("Unknown unit type")
