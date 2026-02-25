#!/usr/bin/env python3

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy (GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if not hand:
            return {
                'strategy': self.get_strategy_name(),
                'cards_played': [],
                'mana_used': 0,
                'targets_attacked': [],
                'damage_dealt': 0
            }
        sorted_hand = sorted(hand, key=lambda c: c.cost)

        cards_played: list = []
        mana_used: int = 0
        damage_dealt: int = 0
        targets_attacked = ['Enemy Player']

        for card in sorted_hand:
            cards_played.append(card.name)
            mana_used += card.cost
            attack_val = getattr(card, 'attack', None)
            if attack_val is not None:
                damage_dealt += attack_val

        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        player_targets = [t for t in available_targets
                          if 'Player' in str(t)]
        creature_targets = [t for t in available_targets
                            if 'Player' not in str(t)]
        return player_targets + creature_targets
