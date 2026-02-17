#!/usr/bin/env python3

def ft_circular_curse() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    from alchemy.grimoire.validator import validate_ingredients
    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): " +
          f"{validate_ingredients('fire air')}")
    print("validate_ingredients(\"dragon scales\"): " +
          f"{validate_ingredients('dragon scales')}")

    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): " +
          f"{record_spell('Fireball', 'fire air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"): " +
          f"{record_spell('Dark Magic', 'shadow')}")

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): " +
          f"{record_spell('Lightning', 'air')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
