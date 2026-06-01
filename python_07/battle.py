#!/usr/bin/env python3
import ex0


def test_factory(factory):
    print("Test factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

    print()


def battle(factory1, factory2):
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print(" vs")
    print(creature2.describe())

    print("\n fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    aqua_fact = ex0.aqua_factory()
    fire_factory = ex0.flame_factory()

    test_factory(aqua_fact)
    test_factory(fire_factory)

    battle(aqua_fact, fire_factory)
