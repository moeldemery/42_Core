#!/usr/bin/env python3

from ex0.Card import Card


class CreatureCard(Card):
    """
    CreatureCard is a subclass of Card that represents
    a creature card in the game.
    It includes additional attributes such as attack
    and health, and implements the abstract methods
    defined in the Card class.
    """

    def __init__(
        self: "CreatureCard",
        name: str,
        cost: int = 0,
        rarity: str = "common",
        attack: int = 0,
        health: int = 0
    ):

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")
        super().__init__(name, cost, rarity)
        self.card_type = "Creature"
        self.attack = attack
        self.health = health

    def play(self: "CreatureCard", game_state: dict) -> dict:
        """
        Implement the logic for playing a creature card.
        Subtract the card's mana cost from the game state's
        available mana and return the updated state.
        """
        current_mana: int = game_state.get("mana", 0)
        if current_mana >= self.cost:
            game_state["mana"] = current_mana - self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield",
            }
        raise Exception("No enough mana")

    def get_card_info(self) -> dict:
        base_info = super().get_card_info()
        base_info.update(
            {
                "type": self.card_type,
                "attack": self.attack,
                "health": self.health
            }
        )
        return base_info

    def attack_target(self: "CreatureCard", target: "CreatureCard") -> dict:
        """
        Implement the logic for attacking a target
        This is a placeholder implementation
        """
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }


if __name__ == "__main__":
    pass
