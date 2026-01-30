#!/usr/bin/env python3
def check_temperature(temp_str: str):
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
        if temp_int < 0:
            raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
        if temp_int > 40:
            raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
        print(f"Temperature {temp_int}°C is perfect for plants!\n")
        return temp_int

    except ValueError as error:
        error_msg = str(error)
        if "invalid literal" in error_msg:
            print(f"Error: '{temp_str}' is not a valid number\n")
        else:
            print(f"Error: {error_msg}\n")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
