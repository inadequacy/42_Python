#!/usr/bin/env python3
import alchemy.grimoire.dark_spellbook as book


if __name__ == "__main__":
    result = book.dark_spell_record(
        "Fantasy", "Earth, wind and fire"
    )

    print(f"Testing record light spell: {result}")
