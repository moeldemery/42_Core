#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    my_deck = Deck()
    my_deck.add_card(
        CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5
        )
    )

    my_deck.add_card(
        ArtifactCard(
            name="Mana Crystal",
            cost=2,
            durability=5,
            effect="Permanent: +1 mana per turn",
            rarity="",
        )
    )

    my_deck.add_card(
        SpellCard(
            name="Lightning Bolt",
            cost=3,
            effect_type="Deal 3 damage to target",
            rarity="",
        )
    )

    print(f"Deck stats: {my_deck.get_deck_stats()}")
    my_deck.shuffle()
    game_status: dict = {
        "mana": 12
    }
    print("\nDrawing and playing cards:\n")

    for _ in range(3):
        try:
            card = my_deck.draw_card()
            print(f"Drew: {card.name} ({card.card_type})")
            game_result = card.play(game_status)
            print(f"Play result: {game_result}\n")
        except Exception as e:
            print(f"Error playing card: {e}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
