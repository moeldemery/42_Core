#!/usr/bin/env python3

from ex0.Card import Card
from random import shuffle


class Deck:
    card_list: list = []

    def add_card(self, card: Card) -> None:
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.card_list)

    def draw_card(self) -> Card:
        if self.card_list:
            return self.card_list.pop()
        raise Exception("No more cards available")

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.card_list),
            "creatures": sum(
                1 for card in self.card_list
                if card.card_type == "Creature"
            ),
            "spells": sum(1 for card in self.card_list
                          if card.card_type == "Spell"),
            "artifacts": sum(
                1 for card in self.card_list if card.card_type == "Artifact"
            ),
            "avg_cost": (
                round(
                    sum(card.cost for card in self.card_list)
                    / len(self.card_list), 1
                )
                if self.card_list
                else 0
            ),
        }


if __name__ == "__main__":
    pass
