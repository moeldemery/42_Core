#!/usr/bin/env python3
from ex0.Card import Card


class Magical(Card):
    def cast_spell(self: "Magical", spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
            }

    def channel_mana(self: "Magical", amount: int) -> dict:
        return {"channeled": amount, "amount": self.cost + amount}

    def get_magic_stats(self: "Magical") -> dict:
        return {"mana": 100, "magic_power": 50}


if __name__ == "__main__":
    pass
