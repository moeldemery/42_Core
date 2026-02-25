#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Rankable, Combatable, Card):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int
    ) -> None:

        RARITY_RATINGS = {
            'Legendary': 1200,
            'Rare': 1150,
            'Uncommon': 1100,
            'Common': 1050,
        }

        if not isinstance(attack_power, int) or attack_power < 0:
            raise ValueError("Attack must be a non-negative integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a non-negative integer")
        super().__init__(name, cost, rarity, "melee")
        self.card_type = "Creature"
        self.attack_power = attack_power
        self.health = health
        self._wins = 0
        self._losses = 0
        self._rating = RARITY_RATINGS.get(rarity, 1000)

    def play(self, game_state: dict) -> dict:
        current_mana = game_state.get('mana', 0)
        if current_mana >= self.cost:
            game_state['mana'] = current_mana - self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Tournament creature summoned'
            }
        return {
            'card_played': self.name,
            'mana_used': 0,
            'effect': 'Not enough mana'
        }

    def attack(self, target) -> dict:
        damage = self.attack_power
        if hasattr(target, 'health'):
            target.health -= damage
        return {
            'attacker': self.name,
            'target': getattr(target, 'name', str(target)),
            'damage': damage,
            'combat_type': 'tournament'
        }

    def calculate_rating(self) -> int:
        return self._rating

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'attack': self.attack_power,
            'health': self.health,
            'interfaces': ['Card', 'Combatable', 'Rankable']
        }

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'record': f"{self._wins}-{self._losses}"
        }

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating -= 16 * losses


if __name__ == "__main__":
    pass
