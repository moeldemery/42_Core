#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Card(ABC):
    """
    Card is The abstract foundation class for all card
    types in the game. It defines the common attributes
    and methods that all cards must implement.
    """
    card_type: str

    def __init__(self, name: str, cost: int, rarity: str = "Common"):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana


if __name__ == "__main__":
    pass
