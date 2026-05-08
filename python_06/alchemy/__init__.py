#!/usr/bin/env python3
from .elements import create_air
from .potions import strength_potion, healing_potion
from .transmutation import lead_to_gold


air = create_air()
strength = strength_potion()
gold = lead_to_gold()


def heal():
    return healing_potion()


__all__ = ["strength", "air", "gold"]
