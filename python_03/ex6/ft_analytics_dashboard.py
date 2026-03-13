#!/usr/bin/env python3

def analytics_dashboard():
    print("===\tGame Analytics Dashboard\t===")

    # Sample gaming data
    players = [
        {"name": "alice", "score": 2300, "achievements": ["first_kill", "level_10", "boss_slayer"], "region": "north", "active": True},
        {"name": "bob", "score": 1800, "achievements": ["first_kill", "level_5"], "region": "east", "active": True},
        {"name": "charlie", "score": 2150, "achievements": ["boss_slayer", "level_10", "treasure_hunter"], "region": "central", "active": False},
        {"name": "diana", "score": 2050, "achievements": ["first_kill", "treasure_hunter"], "region": "north", "active": True},
    ]

    print("\n===\tList Comprehension Examples\t===")

    # High scorers
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print("High scorers (>2000):", high_scorers)

    # Scores doubled
    doubled_scores = [p["score"] * 2 for p in players]
    print("Scores doubled:", doubled_scores)

    # Active players
    active_players = [p["name"] for p in players if p["active"]]
    print("Active players:", active_players)

    print("\n===\tDict Comprehension Examples\t===")

    # Player -> score mapping
    player_scores = {p["name"]: p["score"] for p in players}
    print("Player scores:", player_scores)

    # Score categories
    score_categories = {
        "high": len([p for p in players if p["score"] >= 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] < 2000]),
        "low": len([p for p in players if p["score"] < 1500]),
    }
    print("Score categories:", score_categories)

    # Achievement count per player
    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print("Achievement counts:", achievement_counts)

    print("\n===\tSet Comprehension Examples\t===")

    # Unique players
    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)

    # Unique achievements
    unique_achievements = {a for p in players for a in p["achievements"]}
    print("Unique achievements:", unique_achievements)

    # Active regions
    active_regions = {p["region"] for p in players if p["active"]}
    print("Active regions:", active_regions)

    print("\n===\tCombined Analysis\t\t===")

    total_players = len(players)
    print("Total players:", total_players)

    total_unique_achievements = len(unique_achievements)
    print("Total unique achievements:", total_unique_achievements)

    avg_score = sum([p["score"] for p in players]) / len(players)
    print("Average score:", avg_score)

    top_player = max(players, key=lambda p: p["score"])
    print(
        "Top performer:",
        top_player["name"],
        "(" + str(top_player["score"]) + " points,",
        len(top_player["achievements"]),
        "achievements)"
    )


if __name__ == "__main__":
    analytics_dashboard()
