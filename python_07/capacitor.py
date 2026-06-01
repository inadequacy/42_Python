import ex1


def test_factory(factory, fact_type: str):
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if fact_type == "healing":
        print(base.heal("someone else"))
    if fact_type == "transform":
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if fact_type == "healing":
        print(evolved.heal("someone else"))
    if fact_type == "transform":
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    heal_fact = ex1.heal_factory()
    trans_fact = ex1.transform_factory()

    print("Testing Creature with healing capabilities")
    test_factory(heal_fact, "healing")

    print("\nTesting Creature with transform capabilities")
    test_factory(trans_fact, "transform")
