#!/usr/bin/env python3
import math


def calc_3d_dist(point1: tuple[int, int, int],
                 point2: tuple[int, int, int]) -> float:
    (x1, y1, z1) = point1
    (x2, y2, z2) = point2

    dist: float = math.sqrt(((x2 - x1) ** 2)
                            + ((y2 - y1) ** 2)
                            + ((z2 - z1) ** 2))
    print(f"Distance between {point1} and {point2}: {dist:.2f}")
    return dist


def create_point(x: int, y: int, z: int) -> tuple[int, int, int]:
    point: tuple[int, int, int] = (x, y, z)
    print(f"Position created: {point}")
    return point


def parse_point(coord_str: str) -> tuple[int, int, int] | None:
    try:
        parts = coord_str.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        point: tuple[int, int, int] = (x, y, z)
        print(f"Position created: {point}")
        return point
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    p1 = create_point(10, 20, 5)
    calc_3d_dist((0, 0, 0), p1)

    coord_input = "3,4,0"
    print(f"\nParsing coordinates: \"{coord_input}\"")
    p2 = parse_point(coord_input)
    if p2:
        calc_3d_dist((0, 0, 0), p2)

    invalid_input = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_input}\"")
    p3 = parse_point(invalid_input)

    if p2:
        print("\nUnpacking demonstration:")
        (px, py, pz) = p2
        print(f"Player at x={px}, y={py}, z={pz}")
        print(f"Coordinates: X={px}, Y={py}, Z={pz}")
