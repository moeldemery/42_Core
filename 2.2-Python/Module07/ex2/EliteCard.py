#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Combatable, Magical, Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        combat_type: str = "Elite",
        defence: int = 0
    ):
        Card.__init__(self, name, cost, rarity)
        self.card_type = "Elite"
        self.combat_type = combat_type
        self.attack_power = attack
        self.health = health
        self.defence = defence

    def play(self, game_state: dict) -> dict:
        return {"action": "play_elite_card", "game_state": game_state}

    def attack(self, target: Combatable) -> dict:
        return Combatable.attack(self, target)

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return Magical.cast_spell(self, spell_name, targets)


if __name__ == "__main__":
    pass
