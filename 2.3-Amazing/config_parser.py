from curses import raw
from typing import Optional, Tuple
from const import REQUIRED_KEYS


class Config:
    """this holds validated maze configuration values."""

    width: int
    height: int
    entry: Tuple[int, int]
    exit_: Tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None
    algorithm: str = "backtracker"


def parse_config(path: str) -> dict[str, str | int | bool | Tuple[int, int]]:
    """
    Parse and validate the maze configuration file.
    Args:
        path: The path to the configuration file.
    Returns:
        A dictionary containing the validated configuration values.
    """

    raw: dict[str, str | int | bool | Tuple[int, int]] = {}


    with open(path, "r") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError(
                    f"Invalid config line {line_no}: '{line}'"
                )
            key, value = map(str.strip, line.split("=", 1))
            raw[key.upper()] = value.strip('"')

    """validating mandatory keys and values"""
    missing_keys = REQUIRED_KEYS - raw.keys()
    if missing_keys:
        raise ValueError("Missing required config keys: "
                         f"{', '.join(missing_keys)}")

    """validating width, height"""
    try:
        width = int(raw.get("WIDTH", "0"))
        height = int(raw.get("HEIGHT", "0"))
    except ValueError:
        raise ValueError("WIDTH and HEIGHT must be integers")
    if width < 2 or height < 2:
        raise ValueError(
            f"WIDTH and HEIGHT must be at least 2 "
            f"(got {width}x{height})"
        )
    raw.update({"WIDTH": width, "HEIGHT": height})
    # --- parsing ENTRY, EXIT ---
    entry = _parse_coord(raw.get("ENTRY", ""), "ENTRY")
    exit_ = _parse_coord(raw.get("EXIT", ""), "EXIT")
    if not (0 <= entry[0] < width and 0 <= entry[1] < height):
        raise ValueError("ENTRY point must be within maze bounds")
    if not (0 <= exit_[0] < width and 0 <= exit_[1] < height):
        raise ValueError("EXIT point must be within maze bounds")
    if entry == exit_:
        raise ValueError("ENTRY and EXIT points cannot be the same")
    raw.update({"ENTRY": entry,
                "EXIT": exit_})

    # --- parsing PERFECT ---
    perfect_str = raw.get("PERFECT", "false").lower()
    if perfect_str not in {"true", "false", "1", "0"}:
        raise ValueError("PERFECT must be a boolean value (true/false)")
    perfect = perfect_str in {"true", "1"}
    raw.update({"PERFECT": perfect})
    # --- SEED (optional) ---
    seed: Optional[int] = None
    if "SEED" in raw:
        try:
            seed = int(raw["SEED"])
        except ValueError:
            raise ValueError("SEED must be an integer")
    else:
        seed = 42  # default seed value
    raw.update({"SEED": seed})

    """validating optional algorithm"""
    algorithm = raw.get("ALGORITHM", "backtracker").lower()
    raw.update({"ALGORITHM": algorithm})

    """validating optional display mode"""
    display_mode = raw.get("DISPLAY_MODE", "text").lower()
    raw.update({"DISPLAY_MODE": display_mode})

    """validating output file name"""
    raw.update({"OUTPUT_FILE": raw.get("OUTPUT_FILE", "maze.txt")})

    """validating pattern flag"""
    pattern = raw.get("SHOW_PATTERN", "true").lower()
    if pattern not in {"true", "false", "1", "0"}:
        raise ValueError("SHOW_PATTERN must be a boolean value (true/false)")

    pattern_bool: bool = pattern in {"true", "1"}
    # print(f"Pattern enabled: {pattern_bool}, width: {width}, height: {height}")
    if (pattern_bool is False) or (width < 9 or height < 7):
        raw["SHOW_PATTERN"] = False
        raw["PATTERN_MIN_WIDTH"] = 0
        raw["PATTERN_MIN_HEIGHT"] = 0
    else:
        raw["SHOW_PATTERN"] = pattern_bool
        raw["PATTERN_MIN_WIDTH"] = 9
        raw["PATTERN_MIN_HEIGHT"] = 7

    raw.update({"PATTERN_COLOUR": raw.get("PATTERN_COLOUR", "yellow")})
    raw.update({"FLOW_COLOUR": raw.get("FLOW_COLOUR", "red")})
    raw.update({"WALL_COLOUR": raw.get("WALL_COLOUR", "green")})
    # print(f"Flow colour: {raw['FLOW_COLOUR']}, Wall colour: {raw['WALL_COLOUR']}")
    
    return raw


def _parse_coord(value: str, key: str) -> Tuple[int, int]:
    """parses a 'x,y' coordinate string.
        value is the raw string value.
        key is the key name for error messages.

        returns A (x, y) integer tuple.

        raises ValueError: If the format is invalid.
    """
    if not value:
        raise ValueError(f"{key} is missing or empty")
    parts = value.split(",")
    if len(parts) != 2:
        raise ValueError(f"{key} must be in 'x,y' format, got: {value!r}")
    try:
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        raise ValueError(
            f"{key} coordinates must be integers, got: {value!r}"
        )


if __name__ == "__main__":
    print("=== Config Parser Test ===")
    try:
        config = parse_config("config.txt")
        print("Config loaded successfully:")
        print(config)
    except Exception as e:
        print(f"Error loading config: {e}")
