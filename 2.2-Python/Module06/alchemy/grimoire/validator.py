#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    elements: list[str] = ["fire", "water", "earth", "air"]

    if any(elem in ingredients.lower()
           for elem in elements):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
