#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, name: str) -> None:
        try:
            if name is None or name.strip() == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 0, "sun": 0}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, plant_list: list[str]) -> None:
        try:
            print("Opening watering system")
            for name in plant_list:
                if name not in self.plants:
                    raise WaterError("Not enough water in tank")
                self.plants[name]["water"] += 10
                print(f"Watering {name} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water_level: int,
                           sunlight_hours: int) -> None:
        try:
            if name not in self.plants:
                raise PlantError(f"Plant '{name}' not found in garden!")
            if water_level > 10:
                raise ValueError(f"Water level {water_level}"
                                 " is too high (max 10)")
            if water_level < 1:
                raise ValueError(f"Water level {water_level}"
                                 " is too low (min 1)")
            if sunlight_hours < 2:
                raise ValueError(f"Sunlight hours {sunlight_hours}"
                                 " is too low (min 2)")
            if sunlight_hours > 12:
                raise ValueError(f"Sunlight hours {sunlight_hours}"
                                 " is too high (max 12)")
            print(f"{name}: healthy (water: {water_level},"
                  f" sun: {sunlight_hours})")
        except (PlantError, ValueError) as e:
            print(f"Error checking {name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    gm = GardenManager()
    print("\nAdding plants to garden...")
    gm.add_plant("tomato")
    gm.add_plant("lettuce")
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_plants(["tomato", "lettuce"])

    print("\nChecking plant health...")
    gm.check_plant_health("tomato", 5, 8)
    gm.check_plant_health("lettuce", 15, 5)

    print("\nTesting error recovery...")
    gm.water_plants(["unknown_shrub"])
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
