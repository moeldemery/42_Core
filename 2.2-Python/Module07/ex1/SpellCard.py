#!/usr/bin/env python3
from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str = "Common",
        effect_type: str = ""
    ):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.card_type: str = "Spell"

    def play(self, game_state: dict) -> dict:
        current_mana: int = game_state.get("mana", 0)
        if current_mana >= self.cost:
            game_state["mana"] = current_mana - self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
        raise Exception("No enough mana")

    def resolve_effect(self, targets: list) -> dict:
        return {"resolved": True, "targets": targets}


if __name__ == "__main__":
    pass
