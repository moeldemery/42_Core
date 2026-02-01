#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, qty: int, unit: str) -> None:
    if unit.lower() == "packets":
        print(f"{seed_type.capitalize()} seeds: {qty} packets available")
    elif unit.lower() == "grams":
        print(f"{seed_type.capitalize()} seeds: {qty} grams total")
    elif unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: covers {qty} square meters")
    else:
        print("Unknown unit type")
