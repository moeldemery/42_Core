#!/usr/bin/env python3

def garden_operations(test_type: str) -> None:
    if test_type == "multiple":
        try:
            print("Testing multiple errors together...")
            int("xyz")/0
        except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
            print("Caught an error, but program continues!\n")
        return
    try:
        if test_type == "value":
            print("Testing ValueError...")
            int("abc")
        elif test_type == "zero":
            print("Testing ZeroDivisionError...")
            10 / 0
        elif test_type == "file":
            print("Testing FileNotFoundError...")
            f = open("missing.txt", "r")
            f.close()
        elif test_type == "key":
            print("Testing KeyError...")
            garden = {"rose": "red"}
            print(garden["missing_plant"])

    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations("value")
    garden_operations("zero")
    garden_operations("file")
    garden_operations("key")
    garden_operations("multiple")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
