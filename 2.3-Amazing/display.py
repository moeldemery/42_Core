import random
import sys
import time
from typing import List, Optional, Set, Tuple
from mazegen.maze_generator import Maze
from const import *
from pattern_generator import generate_42_pattern


def render_maze(
    maze: Maze,
    solution: Optional[List[Tuple[int, int]]] = None,
    wall_colour: str = "white",
    pattern_cells: Optional[Set[Tuple[int, int]]] = None,
    pattern_colour: str = "cyan",
    flow_colour: str = "cyan",
    show_solution: bool = False,
    flow_phase: int = 0,
    flow_static: bool = True,
) -> str:
    """
    this builds an ASCII art representation of the maze.

    Each cell is 1 character wide.  Walls are drawn as box-drawing chars.

    Args:
        maze:          The :class:`Maze` to render.
        entry:         (x, y) entry cell.
        exit_:         (x, y) exit cell.
        solution:      Direction letters from entry to exit.
        wall_colour:   ANSI colour name for walls.
        pattern_cells: Optional set of (x, y) cells forming the '42' pattern.
        pattern_colour: Colour for pattern cells.
        show_solution: Whether to overlay the solution path.

    Returns:
        Multi-line string ready to print.
    """
    if wall_colour not in COLOURS:
        raise ValueError(f"Invalid wall colour '{wall_colour}'. "
                         f"Choose from: {COLOUR_NAMES}")
    if pattern_colour not in COLOURS:
        raise ValueError(f"Invalid pattern colour '{pattern_colour}'. "
                         f"Choose from: {COLOUR_NAMES}")
    if flow_colour not in COLOURS:
        raise ValueError(f"Invalid flow colour '{flow_colour}'. "
                         f"Choose from: {COLOUR_NAMES}")

    wall_c = COLOURS[wall_colour]
    pattern_c = COLOURS[pattern_colour]
    flow_c = COLOURS[flow_colour]
    reset_c = RESET
    # debug_c = COLOURS["red"]  # for debugging purposes
    lines: List[str] = []
    W = maze.width
    H = maze.height
    chars = " ╹╺┗┳┃┏┣╸┛━┻┓┫┳╋"
    dot = "⠂•◉●◉•⠂"
    normal_dot = "◉"
    solution_index = {
        cell: index for index, cell in enumerate(solution)
    } if show_solution and solution else {}
    for y in range(H+1):
        top_line = ""
        for x in range(W+1):
            up = maze.is_wall(x, y-1, WEST) if y > 0 and x < W else \
                (maze.is_wall(x-1, y-1, EAST) if y > 0 and x > 0 else False)
            down = maze.is_wall(x, y, WEST) if y < H and x < W else \
                (maze.is_wall(x-1, y, EAST) if y < H and x > 0 else False)
            left = maze.is_wall(x-1, y, NORTH) if x > 0 and y < H else \
                (maze.is_wall(x-1, y-1, SOUTH) if x > 0 and y > 0 else False)
            right = maze.is_wall(x, y, NORTH) if x < W and y < H else \
                (maze.is_wall(x, y-1, SOUTH) if x < W and y > 0 else False)

            idx = ((1 if up else 0) | (2 if right else 0) |
                   (4 if down else 0) | (8 if left else 0))
            top_line += wall_c + chars[idx] + reset_c

            if x < W:
                is_h_wall = maze.is_wall(x, y, NORTH) if y < H \
                    else maze.is_wall(x, y-1, SOUTH)
                top_line += (wall_c + "━━" + reset_c) if is_h_wall else "  "

        lines.append(top_line)

        # ── MIDDLE ROW (cell contents) ──
        if y < H:
            mid_line = ""
            for x in range(W + 1):
                is_v_wall = maze.is_wall(x, y, WEST) if x < W else \
                    maze.is_wall(x-1, y, EAST)
                mid_line += (wall_c + "┃" + reset_c) if is_v_wall else " "

                if x < W:
                    cell = (x, y)
                    if cell == maze.entry:
                        mid_line += COLOURS["green"] + "ST" + reset_c
                    elif cell == maze.exit_:
                        mid_line += COLOURS["red"] + "EN" + reset_c
                    elif show_solution and solution and cell in solution_index:
                        if flow_static and show_solution:
                            phase = (solution_index[cell] + flow_phase) % \
                                len(normal_dot)
                            mid_line += (
                                flow_c +
                                normal_dot[phase] + " " +
                                reset_c)
                        else:
                            phase = (solution_index[cell] + flow_phase) % \
                                len(dot)
                            mid_line += flow_c + dot[phase] + " " + reset_c

                    elif pattern_cells and cell in pattern_cells:
                        mid_line += pattern_c + "▓▓" + reset_c
                    else:
                        mid_line += "  "
            lines.append(mid_line)
    return "\n".join(lines)


def animate_solution_flow(
    maze: Maze,
    solution: List[Tuple[int, int]],
    wall_colour: str = "white",
    pattern_cells: Optional[Set[Tuple[int, int]]] = None,
    pattern_colour: str = "cyan",
    flow_colour: str = "cyan",
    frame_delay: float = 0.12,
) -> None:
    interactive_output = sys.stdout.isatty()

    if not solution:
        frame = render_maze(
            maze=maze, solution=[], wall_colour=wall_colour,
            pattern_cells=pattern_cells, pattern_colour=pattern_colour,
            flow_colour=flow_colour, show_solution=False,
        )
        sys.stdout.write(frame + "\n")
        sys.stdout.flush()
        return

    if not interactive_output:
        final_frame = render_maze(
            maze=maze,
            solution=solution,
            wall_colour=wall_colour,
            pattern_cells=pattern_cells,
            pattern_colour=pattern_colour,
            show_solution=True,
            flow_phase=0,
            flow_colour=flow_colour,
            flow_static=True
        )
        sys.stdout.write(final_frame + "\n")
        sys.stdout.flush()
        return

    for step in range(1, len(solution) + 1):
        frame = render_maze(
            maze=maze,
            solution=solution[:step],
            wall_colour=wall_colour,
            pattern_cells=pattern_cells,
            pattern_colour=pattern_colour,
            show_solution=True,
            flow_phase=step,
            flow_colour=flow_colour,
            flow_static=True
        )
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.write(frame + "\n")
        sys.stdout.flush()
        time.sleep(frame_delay)

    for shimmer in range(len("⠂•◉●") * 2):
        frame = render_maze(
            maze=maze,
            solution=solution,
            wall_colour=wall_colour,
            pattern_cells=pattern_cells,
            pattern_colour=pattern_colour,
            show_solution=True,
            flow_phase=shimmer,
            flow_colour=flow_colour,
            flow_static=False
        )
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.write(frame + "\n")
        sys.stdout.flush()
        time.sleep(frame_delay)

    final_frame = render_maze(
        maze=maze,
        solution=solution,
        wall_colour=wall_colour,
        pattern_cells=pattern_cells,
        pattern_colour=pattern_colour,
        show_solution=True,
        flow_phase=0,
        flow_colour=flow_colour,
        flow_static=True
    )
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(final_frame + "\n")
    sys.stdout.flush()

def draw_ui(frame: str, backtracking: bool = False) -> None:
    # Clear and redraw when interactive so the menu stays visible with the frame.
    if sys.stdout.isatty():
        print("\033[2J\033[H", end="")
    print(frame)
    if backtracking:
        print(MENU_TEXT_BT, end="")
    else:
        print(MENU_TEXT, end="")
    print("Choice: ", end="", flush=True)

def animate_backtrack_maze_generation(
    maze: Maze,
    wall_colour: str = "white",
    pattern_cells: Optional[Set[Tuple[int, int]]] = None,
    pattern_colour: str = "cyan",
    flow_colour: str = "cyan",
    frame_delay: float = 0.05,
    seed: Optional[int] = None,
) -> None:
    """Animate DFS maze carving and show every backtrack pop.

    Self-contained in display.py — does not call generator internals.
    Carves a fresh fully-walled grid with iterative DFS, renders a frame
    on each backtrack pop, then writes the result back to maze.grid.
    """

    def unvisited_neighbors(
        x: int,
        y: int,
        visited: Set[Tuple[int, int]],
        blocked: Set[Tuple[int, int]],
    ) -> List[Tuple[int, int, int]]:
        result: List[Tuple[int, int, int]] = []
        for nx, ny, direction in work_maze.get_neighbors(x, y):
            if (nx, ny) not in visited and (nx, ny) not in blocked:
                result.append((nx, ny, direction))
        return result

    # Build a fresh fully-walled grid to carve into.
    fresh_grid = [
        [NORTH | EAST | SOUTH | WEST for _ in range(maze.width)]
        for _ in range(maze.height)
    ]
    work_maze = Maze(
        width=maze.width,
        height=maze.height,
        entry=maze.entry,
        exit_=maze.exit_,
        grid=fresh_grid,
    )

    blocked: Set[Tuple[int, int]] = set(pattern_cells or set())
    blocked.discard(maze.entry)
    blocked.discard(maze.exit_)
    rng = random.Random(seed)

    interactive_output = sys.stdout.isatty()

    traversal_stack: List[Tuple[int, int]] = [work_maze.entry]
    visited: Set[Tuple[int, int]] = {work_maze.entry}

    if interactive_output:
        sys.stdout.write("\033[2J")

    while traversal_stack:
        x, y = traversal_stack[-1]
        neighbors = unvisited_neighbors(x, y, visited, blocked)

        if neighbors:
            nx, ny, direction = rng.choice(neighbors)
            work_maze.open_wall(x, y, direction)
            visited.add((nx, ny))
            traversal_stack.append((nx, ny))
            continue

        # Dead-end — pop and emit a frame showing the current stack.
        traversal_stack.pop()
        if interactive_output:
            frame = render_maze(
                maze=work_maze,
                solution=traversal_stack,
                show_solution=True,
                wall_colour=wall_colour,
                flow_colour=flow_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
            )
            sys.stdout.write("\033[H")
            sys.stdout.write(frame + "\n")
            sys.stdout.flush()
            time.sleep(frame_delay)

    for cell in blocked:
        work_maze.block_cell(cell)

    # Write the newly carved grid back so the caller's maze reflects
    # what was animated.
    maze.grid = [row[:] for row in work_maze.grid]

    if not interactive_output:
        final_frame = render_maze(
            maze=maze,
            solution=[],
            wall_colour=wall_colour,
            pattern_cells=pattern_cells,
            pattern_colour=pattern_colour,
            flow_colour=flow_colour,
            show_solution=False,
        )
        sys.stdout.write(final_frame + "\n")
        sys.stdout.flush()

    

if __name__ == "__main__":
    print("=== Maze TEST Display ===")
    maze = Maze(
        width=4,
        height=4,
        entry=(0, 0),
        exit_=(3, 3),
        grid=[
            [9,  1,  1,  3],
            [12, 8,  2, 10],
            [5,  0,  6, 10],
            [13, 4,  4,  6],
        ]
    )
    solution_path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]
    # pattern_cells = {(1, 1), (2, 1), (1, 2), (2, 2)}
    # pattern_cells = generate_42_pattern(maze.width, maze.height)

    # print(
    #     render_maze(
    #         solution= solution_path,
    #         wall_colour="green",
    #         pattern_cells=pattern_cells,
    #         pattern_colour="yellow",
    #         show_solution=True,
    #         maze=maze,
    #     )
    # )
    # animate_solution_flow(
    #     maze=maze,
    #     solution=solution_path,
    #     wall_colour="green",
    #     pattern_cells=pattern_cells,
    #     pattern_colour="yellow",
    #     frame_delay=0.5,

    # )
    # sys.stdout.flush()
    print("\n=== Maze TEST Display (Large) ===")
    large_maze = Maze(
        width=12,
        height=12,
        entry=(0, 0),
        exit_=(9, 5),
        grid=[
            [9,   5,  5,  3,  9,  5,  1,  1,  1,  1,  1,  3],
            [8,   0,  0, 15, 10, 15, 15, 12,  4,  4,  4,  2],
            [10, 15,  0, 15,  8,  4, 13, 15, 15,  5,  5,  2],
            [10, 15, 15, 15, 15,  9, 15, 15, 15,  9,  3, 10],
            [10, 11,  9,  5,  4,  2,  9,  5,  5,  3, 10, 10],
            [10,  8,  4,  5,  5,  0,  4,  5,  5,  4,  4,  2],
            [10, 12,  5,  1,  1,  4,  5,  5,  1,  1,  1,  2],
            [10, 12,  5,  1,  1,  4,  5,  5,  1,  1,  1,  2],
            [10, 12,  5,  1,  1,  4,  5,  5,  1,  1,  1,  2],
            [10, 12,  5,  1,  1,  4,  5,  5,  1,  1,  1,  2],
            [10, 12,  5,  1,  1,  4,  5,  5,  1,  1,  1,  2],
            [12,  5,  5,  4,  4,  5,  5,  5,  4,  4,  4,  6]
        ])
    pattern_cells = generate_42_pattern(large_maze.width, large_maze.height)

    if pattern_cells is None:
        for cell in pattern_cells:
            large_maze.block_cell(cell)

    # solution=[
    #         (0, 0), (0, 1), (0, 2), (0, 3), (0,4), (0, 5),(0, 6),
    #         (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7),
    #         (6, 7), (7, 7), (8, 7), (9, 7), (10, 7),(11, 7),
    #         (11,6), (11, 5),(10, 5)
    #     ]
    solution: List[Tuple[int, int]] = []
    # pattern_cells={
    #         (1, 1), (2, 1), (3, 1),
    #         (1, 2),         (3, 2),
    #         (1, 3), (2, 3), (3, 3),
    #         (5, 1), (6, 1),
    #         (6, 2), (7, 2),
    #         (7, 3),
    #         (5, 3), (6, 3),(7, 3)
    #     }

    # animate_solution_flow(
    #     maze=large_maze,
    #     solution=solution,
    #     wall_colour="blue",
    #     pattern_cells=pattern_cells,
    #     pattern_colour="magenta",
    #     flow_colour="red",
    #     frame_delay=0.15,
    # )

    print(
        render_maze(
            maze=large_maze,
            solution=solution,
            wall_colour="blue",
            pattern_cells=pattern_cells,
            pattern_colour="magenta",
            show_solution=True,
        )
    )
