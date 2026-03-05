#!/usr/bin/env python3


def achievement_tracker() -> None:
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    players = [alice, bob, charlie]
    player_names = ["alice", "bob", "charlie"]
    print("===\tAchievement Tracker System\t===\n")
    i = 0
    for n in players:
        print(f"Player {player_names[i]} achievements {n}")
        i += 1
    print("\n===\tAchievement Analytics\t===\n")
    unique = alice.union(bob, charlie)
    common = alice.intersection(bob, charlie)
    alice_unique = alice - (bob | charlie)
    bob_unique = bob - (alice | charlie)
    charlie_unique = charlie - (alice | bob)
    rare = alice_unique | bob_unique | charlie_unique
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    achievement_tracker()
