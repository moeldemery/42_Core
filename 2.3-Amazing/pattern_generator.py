
"""
pattern_generator.py

need 2 functions one to generate a fixed size pattern in the middle of the maze
same as following

inputs:
- Maze class (with width and height attributes and a grid attribute which is a
2D list representing the maze)
example input:
large_maze = Maze(width=12, height=8, grid=[
        [9, 5, 5, 3, 9, 5, 1, 1, 1, 1, 1, 3],
        [8, 1, 3, 10, 10, 9, 4, 4, 4, 4, 4, 2],
        [10, 10, 10, 10, 8, 4, 5, 5, 1, 5, 5, 2],
        [10, 8, 4, 4, 2, 9, 5, 3, 10, 9, 3, 10],
        [10, 10, 9, 5, 4, 2, 9, 4, 4, 2, 10, 10],
        [10, 8, 4, 5, 5, 0, 4, 5, 5, 4, 4, 2],
        [10, 12, 5, 1, 1, 4, 5, 5, 1, 1, 1, 2],
        [12, 5, 5, 4, 4, 5, 5, 5, 4, 4, 4, 6]
    ])

outputs:
list of tuples representing the coordinates of the pattern in the maze
example output:
[(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)]

-------------------------------------------------------------------------------

----------------------------- what I got so far -------------------------------

-------------------------------------------------------------------------------
this file generates our '42' pattern as a set of (x, y) cell coordinates
to be placed in the center of our fgiven maze. each pattern cell will have
all four walls closed (value 0xF).

to use it later in our display as a call:
    from pattern_generator import generate_42_pattern

    pattern_cells = generate_42_pattern(maze_width, maze_height)
    if cells is None:
        print("Maze too small for 42 pattern")
    else:
        # cells is a Set[Tuple[int, int]]
        # do we can use it in render_maze(..., pattern_cells=cells, ...)
        # for now i am doing it separately here, with a bitmask of glyphs
        # where minimum dimensions are 11x9.
        # we can chjange that if we don't like how 42 looks in small mazes
        # like 11x9, 11,10 , 11,11 etc...
"""

from typing import Set, Tuple

# our "4" glyph – 5 wide × 7 tall dimensions
_GLYPH_4 = [

    "#..",
    "#..",
    "###",
    "..#",
    "..#",
]

# our "2" glyph – 4 wide × 7 tall dimensions
_GLYPH_2 = [
    "###",
    "..#",
    "###",
    "#..",
    "###",
]

# the gap (in cells) between the "4" and the "2"
_GAP = 1


def _glyph_coords(glyph: list[str]) -> Set[Tuple[int, int]]:
    """this fn converts a glyph string-map into a set of (col, row) offsets.

    args provided:
        glyph: a list of strings where '#' marks a filled cell.

    it returns:
        set of (x, y) tuples relative to top-left of the glyph.
    """
    coords: Set[Tuple[int, int]] = set()
    for row_idx, row in enumerate(glyph):
        for col_idx, ch in enumerate(row):
            if ch == "#":
                coords.add((col_idx, row_idx))
    return coords


def _pattern_dimensions() -> Tuple[int, int]:
    """this fn returns the bounding-box (width, height)
    of the full '42' pattern.

    returns:
        (total_width, total_height) in cells.
    """
    w4 = len(_GLYPH_4[0])
    w2 = len(_GLYPH_2[0])
    h = max(len(_GLYPH_4), len(_GLYPH_2))
    total_w = w4 + _GAP + w2
    return total_w, h


def generate_42_pattern(
    maze_width: int,
    maze_height: int
) -> Set[Tuple[int, int]]:
    """we generate the '42' pattern centered in our maze of the given size.

    our pattern is built from two small bitmap glyphs ("4" and "2"),
    placed side by side with a 1-cell gap, then centered in the maze.

    args given:
        maze_width:  number of columns in our maze.
        maze_height: number of rows in our maze.

    it reeturns:40
        a set of (x, y) cell coordinates forming the pattern,
        or None if our maze is too small to fit the pattern
        (with at least a 1-cell border on every side).
    """
    pat_w, pat_h = _pattern_dimensions()

    # we need at least 1 cell of border around the pattern
    min_w: int = pat_w + 2
    min_h: int = pat_h + 2
    if maze_width < min_w or maze_height < min_h:
        return set()  # too small for pattern, return empty set

    # then must top-left offset to center the pattern
    offset_x = (maze_width - pat_w) // 2
    offset_y = (maze_height - pat_h) // 2

    result: Set[Tuple[int, int]] = set()

    # placing the "4" first
    for gx, gy in _glyph_coords(_GLYPH_4):
        result.add((offset_x + gx, offset_y + gy))

    # placing the "2" shifted right by (width_of_4 + gap)
    shift_x = len(_GLYPH_4[0]) + _GAP
    for gx, gy in _glyph_coords(_GLYPH_2):
        result.add((offset_x + shift_x + gx, offset_y + gy))

    return result


def stamp_pattern_on_grid(
    grid: list[list[int]],
    pattern_cells: Set[Tuple[int, int]],
) -> None:
    """this sets all pattern cells to fully-walled (0xF) in the grid.

    we modify the grid in-place. this should be called AFTER maze
    generation so that the pattern overwrites any carved passages.

    args given:
        grid:          2-D list [row][col] of wall bitmasks.
        pattern_cells: Set of (x, y) coordinates to wall off.
    """
    for x, y in pattern_cells:
        grid[y][x] = 0xF  # NORTH | EAST | SOUTH | WEST = 15


# ── visual test for us to see random mazes outputs - edit w,h ───
    w, h = 15, 15
    # maze = Maze(
    #     width=w, height=h,
    #     grid=[[0 for _ in range(w)] for _ in range(h)],
    #     entry=(0, 0), exit_=(w-1, h-1)
    #     )
    pattern = generate_42_pattern(w, h)
    if pattern is None:
        print(f"Maze {w}x{h} is too small for the 42 pattern.")
    else:
        print(f"42 pattern for {w}x{h} maze  "
              f"({_pattern_dimensions()[0]}x"
              f"{_pattern_dimensions()[1]} glyphs):")
        print(f"  {len(pattern)} cells total\n")

        # drawing a simple text grid for it for now
        for row in range(h):
            line = ""
            for col in range(w):
                if (col, row) in pattern:
                    line += "██"
                else:
                    line += "· "
            print(line)

        print(f"\nCoordinates: {sorted(pattern)}")
