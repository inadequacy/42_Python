#!/usr/bin/env python3
import sys


def achievement_tracker() -> None:
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob =  {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    players = [alice, bob, charlie]
    player_names = ["alice", "bob", "charlie"]
    print("===\tAchievement Tracker System\t===\n")
    i = 0
    for n in players:
        print(f"Player {player_names[i]} achievements {n}")
        i += 1

if __name__ == "__main__":
    achievement_tracker()
