#!/usr/bin/env python3
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str = "Common",
        durability: int = 0,
        effect: str = "",
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.card_type: str = "Artifact"

    def play(self, game_state: dict) -> dict:
        current_mana: int = game_state.get("mana", 0)
        if current_mana >= self.cost:
            game_state["mana"] = current_mana - self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect,
            }
        raise Exception("No enough mana")

    def activate_ability(self) -> dict:
        return {"activated": True, "effect": self.effect}


if __name__ == "__main__":
    pass
