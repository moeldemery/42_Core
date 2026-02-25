#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.Card import Card


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Card]
    ) -> dict:

        pass

    @abstractmethod
    def get_strategy_name(self: "GameStrategy") -> str:
        pass

    @abstractmethod
    def prioritize_targets(
        self: "GameStrategy",
        available_targets: list
    ) -> list:
        pass
