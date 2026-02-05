#!/usr/bin/env python3
from typing import Any


def run_dashboard() -> None:
    players_data: list[dict[str, Any]] = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "collector", "hunterxhunter"]},
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["level_10", "boss_slayer", "speed_demon"],
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["first_kill", "level_10", "player_killer"]
        },
    ]
    regions: list[str] = ["north", "east", "north",
                          "central", "east", "central"]

    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [
        str(p["name"]) for p in players_data
        if p["score"] > 2000
    ]
    double_score: list[int] = [
        int(p["score"]) * 2 for p in players_data
    ]
    active_players: list[str] = [
        str(p["name"]) for p in players_data
    ]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    score_map: dict[str, int] = {
        str(p["name"]): int(p["score"])
        for p in players_data
    }
    achieve_map: dict[str, int] = {
        str(p["name"]): len(p["achievements"])
        for p in players_data
    }
    score_categories: dict[str, int] = {
        "high": sum(1 for p in players_data if int(p["score"]) >= 2000),
        "medium": sum(1 for p in players_data
                      if 1000 <= int(p["score"]) < 2000),
        "low": sum(1 for p in players_data if int(p["score"]) < 1000)
    }
    print(f"Player scores: {score_map}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achieve_map}")

    print("\n=== Set Comprehension Examples ===")
    unique_player: set[str] = {p["name"] for p in players_data}
    unique_achieve: set[str] = {
        ach for p in players_data for ach in p["achievements"]}
    active_regions: set[str] = {r for r in regions}
    print(f"Unique players: {unique_player}")
    print(f"Unique achievements: {unique_achieve}")
    print(f"Active regions:  {active_regions}")

    print("\n=== Set Comprehension Examples ===")
    player_count: int = len(players_data)
    total_score: int = sum(score_map.values())
    avg_score: float = total_score / player_count
    top_player: str = sorted(score_map, key=lambda k: score_map[k])[-1]
    print(f"Total players: {player_count}")
    print(f"Total unique achievements: {len(unique_achieve)}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_player} ({score_map[top_player]}"
          f" points, {achieve_map[top_player]} achievements)")


if __name__ == "__main__":
    run_dashboard()
