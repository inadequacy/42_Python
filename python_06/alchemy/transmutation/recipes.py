#!/usr/bin/env python3
import sys

sys.path.append('../../alchemy')
import alchemy.elements as ele1
import elements as ele2
from ..potions import strength_potion


def lead_to_gold() -> str:
    ele1.create_air()
    ele2.create_fire()
    strength_potion()
    return "Recipe transmuting Lead to Gold: brew '[created air]' " \
           "and '[created strength potion]' mixed with '[created fire]'"
