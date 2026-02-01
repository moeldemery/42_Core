#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if (plant is None or plant.strip() == "" or
               plant.__class__.__name__ != "str"):
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", "", "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
