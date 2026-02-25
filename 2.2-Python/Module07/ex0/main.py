#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")

    game_status: dict = {
        "mana": 6
    }

    card1 = CreatureCard(
        name='Fire Dragon',
        cost=5,
        rarity='Legendary',
        attack=7,
        health=5
        )
    print("CreatureCard Info:")
    print(card1.get_card_info())

    print(f"\nPlaying {card1.name} with "
          f"{game_status.get("mana", 0)} mana available:")
    print(f"Playable: {card1.is_playable(game_status.get("mana", 0))}")

    play_result = card1.play(game_status)
    print(f"Play result: {play_result}")

    card2 = CreatureCard(
        name='Goblin Warrior',
        cost=3,
        attack=3,
        health=2
        )

    print(f"\n{card1.name} attacks {card2.name}:")
    attack_result = card1.attack_target(card2)
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana "
          f"({game_status.get("mana", 0)} available):")
    print(f"Playable: {card1.is_playable(game_status.get("mana", 0))}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
