#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"{spell_name}: RECORDED"
    else:
        return f"{spell_name}: REJECTED"
