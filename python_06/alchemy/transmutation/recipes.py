#!/usr/bin/env python3
import sys
sys.path.append('../../alchemy')


def lead_to_gold() -> str:
    import alchemy.elements as ele1
    import elements as ele2
    from ..potions import strength_potion

    ele1.create_air()
    ele2.create_fire()
    strength_potion()
    return "Recipe transmuting Lead to Gold: brew '[created air]' " \
           "and '[created strength potion]' mixed with '[created fire]'"
