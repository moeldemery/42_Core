#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.current_age = age
        self._created_print()

    def _created_print(self) -> None:
        print(f"Created: {self.name} "
              f"({self.height}cm, {self.current_age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print(f"\nTotal plants created: {len(plants)}")
