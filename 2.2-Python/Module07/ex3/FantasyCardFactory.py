#!/usr/bin/env python3
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        super().__init__(name="FantasyCardFactory")
        self._supported_types = {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
        self._creature_data = {
                'Fire Dragon': (5, 'Legendary', 7, 5),
                'Goblin Warrior': (2, 'Common', 2, 1),
                'Ice Wizard': (4, 'Rare', 3, 4),
                'Lightning Elemental': (3, 'Uncommon', 4, 2),
                'Stone Golem': (6, 'Rare', 5, 8),
                'Shadow Assassin': (3, 'Uncommon', 5, 2),
                'Healing Angel': (4, 'Rare', 2, 6),
                'Forest Sprite': (1, 'Common', 1, 1),
            }
        self._spell_data = {
            'Lightning Bolt': (3, 'Common', 'damage'),
            'Healing Potion': (2, 'Common', 'heal'),
            'Fireball': (4, 'Uncommon', 'damage'),
            'Shield Spell': (1, 'Common', 'buff'),
            'Meteor': (8, 'Legendary', 'damage'),
            'Ice Shard': (2, 'Common', 'damage'),
            'Divine Light': (5, 'Rare', 'heal'),
            'Magic Missile': (1, 'Common', 'damage'),
        }
        self._artifact_data = {
            'Mana Crystal': (2, 'Common', 5, 'Permanent: +1 mana per turn'),
            'Sword of Power': (3, 'Uncommon', 3,
                               'Permanent: +2 attack to equipped creature'),
            'Ring of Wisdom': (4, 'Rare', 4,
                               'Permanent: Draw an extra card each turn'),
            'Shield of Defense': (5, 'Rare', 6,
                                  'Permanent: +3 health to all \
                                      friendly creatures'),
            'Crown of Kings': (7, 'Legendary', 8,
                               'Permanent: +1 cost reduction to all cards'),
            'Boots of Speed': (2, 'Uncommon', 2,
                               'Permanent: Cards cost 1 less mana'),
            'Cloak of Shadows': (3, 'Uncommon', 3,
                                 'Permanent: Creatures have stealth'),
            'Staff of Elements': (6, 'Legendary', 7,
                                  'Permanent: +1 spell damage'),
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self._creature_data:
                cost, rarity, atk, health = self._creature_data[name_or_power]
                return CreatureCard(
                    name=name_or_power,
                    cost=cost,
                    rarity=rarity,
                    attack=atk, health=health
                )
            return CreatureCard(
                name=name_or_power, cost=3, rarity='Common',
                attack=3, health=3
            )
        elif isinstance(name_or_power, int):
            return CreatureCard(
                name='Fire Dragon', cost=name_or_power, rarity='Legendary',
                attack=name_or_power + 2, health=name_or_power
            )
        return CreatureCard(
            name='Goblin Warrior', cost=2, rarity='Common',
            attack=2, health=1
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self._spell_data:
                cost, rarity, effect_type = self._spell_data[name_or_power]
                return SpellCard(
                    name=name_or_power, cost=cost, rarity=rarity,
                    effect_type=effect_type
                )
            return SpellCard(
                name=name_or_power, cost=3, rarity='Common',
                effect_type='damage'
            )
        elif isinstance(name_or_power, int):
            return SpellCard(
                name='Lightning Bolt', cost=name_or_power, rarity='Common',
                effect_type='damage'
            )
        return SpellCard(
            name='Lightning Bolt', cost=3, rarity='Common',
            effect_type='damage'
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if name_or_power in self._artifact_data:
                cost, rarity, durability, effect = \
                    self._artifact_data[name_or_power]
                return ArtifactCard(
                    name=name_or_power, cost=cost, rarity=rarity,
                    durability=durability, effect=effect
                )
            return ArtifactCard(
                name=name_or_power, cost=2, rarity='Common',
                durability=3, effect='Permanent: generic effect'
            )
        elif isinstance(name_or_power, int):
            return ArtifactCard(
                name='Mana Crystal', cost=name_or_power, rarity='Common',
                durability=5, effect='Permanent: +1 mana per turn'
            )
        return ArtifactCard(
            name='Mana Crystal', cost=2, rarity='Common',
            durability=5, effect='Permanent: +1 mana per turn'
        )

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature())
            elif i % 3 == 1:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {'deck': deck, 'size': len(deck), 'theme': 'Fantasy'}

    def get_supported_types(self) -> dict:
        return self._supported_types
