#!/usr/bin/env python3
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self._factory: "CardFactory"
        self._strategy: "GameStrategy"
        self._turns_simulated = 0
        self._total_damage = 0
        self._cards_created = 0

    def configure_engine(
        self,
        factory: "CardFactory",
        strategy: "GameStrategy"
    ) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            return {'error': 'Engine not configured'}

        hand = [
            self._factory.create_creature('Fire Dragon'),
            self._factory.create_creature('Goblin Warrior'),
            self._factory.create_spell('Lightning Bolt')
        ]
        self._cards_created += len(hand)

        battlefield: list = []

        hand_str: str = ', '.join(f"{c.name} ({c.cost})" for c in hand)
        print(f"Hand: [{hand_str}]")

        result = self._strategy.execute_turn(hand, battlefield)

        self._turns_simulated += 1
        self._total_damage += result.get('damage_dealt', 0)

        actions = {
            'cards_played': result.get('cards_played', []),
            'mana_used': result.get('mana_used', 0),
            'targets_attacked': result.get('targets_attacked', []),
            'damage_dealt': result.get('damage_dealt', 0)
        }

        return {
            'strategy': result.get('strategy', ''),
            'actions': actions
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': (
                self._strategy.get_strategy_name()
                if self._strategy else None
            ),
            'total_damage': self._total_damage,
            'cards_created': self._cards_created
        }
