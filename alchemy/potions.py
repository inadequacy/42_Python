#!/usr/bin/env python3
import sys

sys.path.append('../alchemy')
import alchemy.elements as ele2
import elements as ele1


def healing_potion() -> str:
    ele2.create_earth()
    ele2.create_air()
    return "Healing potion brewed with '[created earth element]'" \
           " and '[created air element]'"


def strength_potion() -> str:
    ele1.create_fire()
    ele1.create_water()
    return "Strength potion brewed with '[created fire element]'" \
           " and '[created water element]'"
