#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lowercase = ingredients.lower()

    is_valid = any(
        ingredient.lower() in lowercase
        for ingredient in allowed
    )

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
