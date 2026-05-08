#!/usr/bin/env python3
from alchemy.grimoire import light_spell_record


if __name__ == "__main__":
    result = light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )

    print(f"Testing record light spell: {result}")
