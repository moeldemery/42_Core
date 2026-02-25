#!/usr/bin/env python3

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._counters: dict[str, int] = {}
        self._matches: list[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        key = card.name.split()[-1].lower()
        self._counters[key] = self._counters.get(key, 0) + 1
        card_id = f"{key}_{self._counters[key]:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._cards:
            return {'error': f"Card '{card1_id}' not registered"}
        if card2_id not in self._cards:
            return {'error': f"Card '{card2_id}' not registered"}

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        if card1.attack_power > card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        elif card2.attack_power > card1.attack_power:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id
        else:
            if card1.health >= card2.health:
                winner, loser = card1, card2
                winner_id, loser_id = card1_id, card2_id
            else:
                winner, loser = card2, card1
                winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True
        )
        board = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            info = card.get_rank_info()
            board.append({
                'rank': rank,
                'card_id': card_id,
                'name': card.name,
                'rating': info['rating'],
                'record': info['record']
            })
        return board

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        played = len(self._matches)
        avg = (
            sum(c.calculate_rating() for c in self._cards.values()) // total
            if total > 0 else 0
        )
        return {
            'total_cards': total,
            'matches_played': played,
            'avg_rating': avg,
            'platform_status': 'active'
        }

    pass
