#!/usr/bin/env python3
import sys
sys.path.append('../alchemy')


def healing_potion() -> str:
    import alchemy.elements as ele2

    ele2.create_earth()
    ele2.create_air()
    return "Healing potion brewed with '[created earth element]'" \
           " and '[created air element]'"


def strength_potion() -> str:
    import elements as ele1

    ele1.create_fire()
    ele1.create_water()
    return "Strength potion brewed with '[created fire element]'" \
           " and '[created water element]'"
