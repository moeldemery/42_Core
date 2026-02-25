#!/usr/bin/env python3

from ex0.Card import Card


class Combatable(Card):
    def __init__(
        self: "Combatable",
        name: str,
        cost: int,
        rarity: str,
        combat_type: str,
        attack: int = 0,
        health: int = 0,
        defence: int = 0,
    ):
        super().__init__(name, cost, rarity)
        self.card_type = "Combatable"
        self.combat_type = combat_type
        self.attack_power = attack
        self.health = health
        self.defence = defence

    def attack(self: "Combatable", target: "Combatable") -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": self.combat_type,
        }

    def defend(self: "Combatable", incoming_damage: int) -> dict:
        damage_blocked = min(self.defence, incoming_damage)
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - damage_blocked,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > (incoming_damage - damage_blocked),
        }

    def get_combat_stats(self: "Combatable") -> dict:
        return {"health": self.health, "attack_power": self.attack_power}

    def play(self: "Combatable", game_state: dict[str, object]) -> dict:
        return {"action": "play_combatable_card", "game_state": game_state}


if __name__ == "__main__":
    pass
