#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")
    dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=7,
        health=5
    )
    wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack_power=3,
        health=4
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        info = card.get_rank_info()
        stats = card.get_tournament_stats()
        print(f"{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {stats['interfaces']}")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}\n")

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
