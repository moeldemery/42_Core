#!/usr/bin/env python3

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory1 = FantasyCardFactory()
    print(f"Factory: {factory1.name}")

    strategy = AggressiveStrategy()
    print(f"Strategy: {strategy.get_strategy_name()}")

    types = factory1.get_supported_types()
    print(f"Available types: {types}")

    engine = GameEngine()
    engine.configure_engine(factory1, strategy)

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()
    print("\nTurn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
