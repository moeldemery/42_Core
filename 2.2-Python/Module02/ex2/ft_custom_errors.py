#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def test_custum_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for error in errors_to_test:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custum_error_types()
