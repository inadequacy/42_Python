import ex0
import ex1
import ex2
from itertools import combinations


def battle(opponents: list[tuple[ex0.factory, ex2.strategies]]) -> None:
    # test if they are valid
    # make them fight each other (each of them)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    try:
        for left, right in combinations(opponents, 2):

            left_factory, left_strategy = left
            right_factory, right_strategy = right

            left_creature = left_factory.create_base()
            right_creature = right_factory.create_base()

            print("* Battle *")
            print(left_creature.describe())
            print("vs.")
            print(right_creature.describe())
            print("now fight!")

            left_strategy.act(left_creature)
            right_strategy.act(right_creature)
            print()

    except ex2.battle_exception as e:
        print(e)
        print()


if __name__ == "__main__":
    fire = ex0.flame_factory()
    grass = ex1.heal_factory()
    water = ex0.aqua_factory()
    trans = ex1.transform_factory()

    aggressive = ex2.aggressive()
    defensive = ex2.defensive()
    normal = ex2.normal()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(
        [(fire, normal), (grass, defensive)]
        )

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [(fire, aggressive), (grass, defensive)]
        )

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [(water, normal), (grass, defensive), (trans, aggressive)]
        )
