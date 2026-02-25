#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Legendary",
        attack=5,
        health=8,
        combat_type="melee",
        defence=3,
    )

    card_methods = [
        method
        for method in dir(Card)
        if not method.startswith("_") and callable(getattr(Card, method))
    ]
    print(f"- Card: {card_methods}")

    combatable_methods = [
        method
        for method in dir(Combatable)
        if not method.startswith("_") and callable(getattr(Combatable, method))
    ]
    print(f"- Combatable: {combatable_methods}")

    magical_methods = [
        method
        for method in dir(Magical)
        if not method.startswith("_") and callable(getattr(Magical, method))
    ]
    print(f"- Magical: {magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    enemy = Combatable(
        name="Enemy",
        cost=3,
        rarity="Common",
        combat_type="Melee",
        attack=15,
        health=50
    )
    print(f"Attack result: {elite.attack(target=enemy)}")
    print(f"Defense result: {elite.defend(incoming_damage=5)}")

    print("\nMagic phase:")
    print(
        f"Spell cast: {elite.cast_spell(
            spell_name='Fireball',
            targets=['Enemy1', 'Enemy2']
            )}"
    )
    print(f"Mana channel: {elite.channel_mana(amount=3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
