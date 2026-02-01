#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         " is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    try:
        print("\nTesting good values...")
        check_plant_health("tomato", 5, 5)
    except ValueError as err:
        print(f"Error: {err}")

    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as err:
        print(f"Error: {err}")

    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as err:
        print(f"Error: {err}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
