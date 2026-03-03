from collections import deque
from dataclasses import dataclass, field
import random
import sys
import sys
from time import time
from typing import List, Optional, Set, Tuple

"""------------CONSTANTS------------"""
NORTH: int = 1
EAST: int = 2
SOUTH: int = 4
WEST: int = 8

ALL_DIRS: List[int] = [NORTH, EAST, SOUTH, WEST]
DELTA: dict[int, Tuple[int, int]] = {
        NORTH: (0, -1),
        EAST: (1, 0),
        SOUTH: (0, 1),
        WEST: (-1, 0),
}
OPPOSITE = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}


"""------------MAZE class------------"""


_MOVE = {
    NORTH: (0, -1),
    EAST:  (1,  0),
    SOUTH: (0,  1),
    WEST:  (-1, 0),
}

_DIR_LETTER = {
    NORTH: "N",
    EAST:  "E",
    SOUTH: "S",
    WEST:  "W",
}


@dataclass
class Maze:
    """Holds the generated maze grid and metadata."""
    width: int
    height: int
    entry: Tuple[int, int]
    exit_: Tuple[int, int]
    grid: List[List[int]] = field(default_factory=list)  # t:ignore[assignment]

    def is_wall(self, x: int, y: int, direction: int) -> bool:
        """Return True if the wall in *direction*
        from cell (x, y) is closed."""
        return bool(self.grid[y][x] & direction)

    def is_in_bounds(self, x: int, y: int) -> bool:
        """Return True if (x, y) is inside the maze."""
        return (0 <= x < self.width and 0 <= y < self.height)

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int, int]]:
        """returns list of (nx, ny, direction) for all neighbors of (x, y).
            x is our column index.
            y is our row index.
            returned is list of (nx, ny, direction) tuples.
        """
        neighbors: List[Tuple[int, int, int]] = []
        for direction, (dx, dy) in _MOVE.items():
            nx, ny = x + dx, y + dy
            if self.is_in_bounds(nx, ny):
                neighbors.append((nx, ny, direction))
        return neighbors

    def is_outer_wall(self, x: int, y: int, direction: int) -> bool:
        """Return True if the wall in *direction* from cell
        (x, y) is an outer wall."""
        if direction == NORTH and y == 0:
            return True
        if direction == EAST and x == self.width - 1:
            return True
        if direction == SOUTH and y == self.height - 1:
            return True
        if direction == WEST and x == 0:
            return True
        return False

    def block_cell(self, cell: Tuple[int, int]) -> None:
        """sets all walls of the given cell to closed and seal neighbors.
        """
        x, y = cell
        if self.is_in_bounds(x, y):
            self.grid[y][x] = NORTH | EAST | SOUTH | WEST  # 0xF
            for nx, ny, direction in self.get_neighbors(x, y):
                self.grid[ny][nx] |= OPPOSITE[direction]

    def open_wall(self, x: int, y: int, direction: int) -> None:
        """Open the wall in *direction* from cell (x, y)."""
        self.grid[y][x] &= ~direction
        nx = x + (direction == EAST) - (direction == WEST)
        ny = y + (direction == SOUTH) - (direction == NORTH)
        if self.is_in_bounds(nx, ny):
            self.grid[ny][nx] &= ~OPPOSITE[direction]

        # dx, dy = DELTA[direction]
        # nx, ny = x + dx, y + dy
        # maze.grid[y][x] &= ~direction
        # maze.grid[ny][nx] &= ~OPPOSITE[direction]


    def solve(self) -> Optional[List[Tuple[int, int]]]:
        """finding the shortest path from entry to exit using BFS.
           returned is either: a list of (x, y) cells
           from entry to exit (inclusive),or None if no path exists.
        """
        start = self.entry
        goal = self.exit_
        if start == goal:
            return [start]

        queue: deque[Tuple[int, int]] = deque([start])
        came_from: dict[Tuple[int, int], Optional[Tuple[int, int]]] = {
            start: None
        }

        while queue:
            x, y = queue.popleft()
            for nx, ny, direction in self.get_neighbors(x, y):
                if (nx, ny) in came_from:
                    continue
                if not self.is_wall(x, y, direction):
                    came_from[(nx, ny)] = (x, y)
                    if (nx, ny) == goal:
                        path: List[Tuple[int, int]] = []
                        cur: Optional[Tuple[int, int]] = goal
                        while cur is not None:
                            path.append(cur)
                            cur = came_from[cur]
                        path.reverse()
                        return path
                    queue.append((nx, ny))
        return None

    def solution_directions(self) -> Optional[str]:
        """returns the solution as a string of direction letters (N/E/S/W).
         returned is either: a string like 'EESWE', or None if no path exists.
        """
        path = self.solve()
        if path is None:
            return None
        if len(path) < 2:
            return ""

        directions: List[str] = []
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            dx, dy = x2 - x1, y2 - y1
            for direction, (mx, my) in _MOVE.items():
                if (mx, my) == (dx, dy):
                    directions.append(_DIR_LETTER[direction])
                    break
        return "".join(directions)


class MazeGenerator:
    """Generates mazes using various algorithms.
        width is the number of columns (>= 2).
        height is the number of rows (>= 2).
        entry is the (x, y) entry cell coordinates.
        exit_ is the (x, y) exit cell coordinates.
        seed is the optional RNG seed for reproducibility.
        perfect is whether to generate a perfect maze. If False, add loops.
        algorithm: One of 'backtracker', 'prim', 'kruskal'.

    Example::

        gen = MazeGenerator(width=15, height=10, seed=7, perfect=True)
        maze = gen.generate()
        path = maze.solve()
    """

    ALGORITHMS: Tuple[str, ...] = ("backtracker", "prim", "kruskal")

    def __init__(
        self,
        width: int = 20,
        height: int = 15,
        entry: Tuple[int, int] = (0, 0),
        exit_: Tuple[int, int] = (19, 14),
        seed: Optional[int] = None,
        perfect: bool = True,
        algorithm: str = "backtracker",
        pattern: Set[Tuple[int, int]] = set(),
    ) -> None:

        if width < 2 or height < 2:
            raise ValueError(
                f"Maze must be at least 2x2 (got {width}x{height})."
            )
        if algorithm not in self.ALGORITHMS:
            raise ValueError(
                f"Unknown algorithm '{algorithm}'. "
                f"Choose from: {self.ALGORITHMS}"
            )
        self.width = width
        self.height = height
        self.entry = entry
        self.exit_ = exit_
        self.seed = seed
        self.perfect = perfect
        self.algorithm = algorithm
        self._rng = random.Random(seed)
        self.pattern = pattern or set()



    def generate(
        self,
        animate: bool = False,
        frame_delay: float = 0.05,
        wall_colour: str = "dark_gold",
        flow_colour: str = "neon_green",
        blocked_cells: Optional[Set[Tuple[int, int]]] = None,
    ) -> Maze:
        """Generate and return a Maze.
            animatec-> shows the maze being built in the terminal.
            frame_delay-> seconds between animation frames.
            wall_colour-> ANSI colour name for walls during animation.
            flow_colour-> ANSI colour for the active DFS path.
            blocked_cells-> cells the carver must not enter (pattern cells).
            returned is a fully generated Maze instance.
        """

        grid = [
            [NORTH | EAST | SOUTH | WEST for _ in range(self.width)]
            for _ in range(self.height)
        ]
        maze = Maze(
            width=self.width,
            height=self.height,
            entry=self.entry,
            exit_=self.exit_,
            grid=grid
            )
        if self.algorithm == "backtracker":
            self._algo_recursive_backtracker(maze, self.pattern)
        elif self.algorithm == "prim":
            self._algo_prim(maze, self.pattern)

        if not self.perfect:
            self._add_loops(maze, self.pattern)

        # Enforce blocked pattern cells after all carving/looping steps.
        # block_cell also closes the corresponding wall bit on neighbors,
        # so shared walls remain consistent.
        for cell in self.pattern:
            maze.block_cell(cell)

        return maze

    @staticmethod
    def solve(
        maze: Maze,
        start: Tuple[int, int],
        end: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """Solve maze with recursive flood fill and return a cell path.

        The algorithm fills distances starting from *end* and only updates a
        neighbor when there is no wall between the current cell and neighbor.
        """
        (sx , sy) = start
        (ex , ey) = end
        if (not maze.is_in_bounds(sx, sy) or
            
                not maze.is_in_bounds(ex, ey)):
            raise ValueError("Start or end point is outside the maze bounds.")

        grid_cost = [[-1 for _ in range(maze.width)]
                     for _ in range(maze.height)]
        grid_cost[ey][ex] = 0

        def flood_fill(x: int, y: int) -> None:
            current_cost = grid_cost[y][x]

            for direction in ALL_DIRS:
                # Only expand through open passages.
                if maze.is_wall(x, y, direction):
                    continue

                nx = x + (direction == EAST) - (direction == WEST)
                ny = y + (direction == SOUTH) - (direction == NORTH)
                if not maze.is_in_bounds(nx, ny):
                    continue

                next_cost = current_cost + 1
                if grid_cost[ny][nx] == -1 or next_cost < grid_cost[ny][nx]:
                    grid_cost[ny][nx] = next_cost
                    flood_fill(nx, ny)

        flood_fill(end[0], end[1])

        if grid_cost[start[1]][start[0]] == -1:
            raise ValueError("No path from start to end.")

        path: List[Tuple[int, int]] = [start]
        x, y = start

        while (x, y) != end:
            current_cost = grid_cost[y][x]
            next_cell: Optional[Tuple[int, int]] = None

            for direction in ALL_DIRS:
                if maze.is_wall(x, y, direction):
                    continue
                nx = x + (direction == EAST) - (direction == WEST)
                ny = y + (direction == SOUTH) - (direction == NORTH)
                if (maze.is_in_bounds(nx, ny) and
                        grid_cost[ny][nx] == current_cost - 1):
                    next_cell = (nx, ny)
                    break

            if next_cell is None:
                raise ValueError("No path from start to end...")

            x, y = next_cell
            path.append((x, y))

        return path

    def _algo_recursive_backtracker(self, maze: Maze, blocked_cells: Set[Tuple[int, int]]) -> None:
        """Recursive DFS maze carving with optional real-time animation.
        it only renders intermediate frames. the final completed frame
        is handled by generate().
            maze is the Maze to carve.
            animate is whether to show animation frames.
            frame_delay are the seconds between frames.
            wall_colour is the colour for walls.
            flow_colour is the colour for the active path.
            blocked_cells are the cells the carver must skip.
        """

        stack: List[Tuple[int, int]] = [maze.entry]
        visited: Set[Tuple[int, int]] = {maze.entry} | blocked_cells

        while stack:
            x, y = stack[-1]

            neighbors = [
                (nx, ny, direction)
                for nx, ny, direction in maze.get_neighbors(x, y)
                if (nx, ny) not in visited
            ]

            if not neighbors:
                stack.pop()
            else:
                nx, ny, direction = self._rng.choice(neighbors)
                maze.grid[y][x] &= ~direction
                maze.grid[ny][nx] &= ~OPPOSITE[direction]
                visited.add((nx, ny))
                stack.append((nx, ny))
        
    def _algo_prim(
        self,
        maze: Maze,
        pattern: Set[Tuple[int, int]],
    ) -> None:
        """Prim's algorithm maze carving."""

        visited: List[List[bool]] = [
            [False] * self.width for _ in range(self.height)
        ]

        (st_x, st_y) = (self._rng.randint(0, self.width - 1),
                        self._rng.randint(0, self.height - 1))
        while (st_x, st_y) in pattern:
            st_x, st_y = (self._rng.randint(0, self.width - 1),
                          self._rng.randint(0, self.height - 1))

        visited[st_y][st_x] = True
        # node: (x, y, direction_to_unvisited_neighbour)
        unvisited_nodes: List[Tuple[int, int, int]] = []
        self._add_unvisited_nodes(
            maze, st_x, st_y, visited, unvisited_nodes, pattern)

        while unvisited_nodes:
            rdm_node = self._rng.choice(unvisited_nodes)
            unvisited_nodes.remove(rdm_node)

            x, y, direction = rdm_node
            nx = x + (direction == EAST) - (direction == WEST)
            ny = y + (direction == SOUTH) - (direction == NORTH)

            if (not visited[ny][nx]
                    and (x, y) not in pattern
                    and (nx, ny) not in pattern):
                visited[ny][nx] = True
                maze.open_wall(x, y, direction)
                self._add_unvisited_nodes(
                    maze, nx, ny, visited, unvisited_nodes, pattern)

    def _add_unvisited_nodes(
        self,
        maze: Maze,
        x: int,
        y: int,
        visited: List[List[bool]],
        unvisited_nodes: List[Tuple[int, int, int]],
        pattern: Set[Tuple[int, int]]
    ) -> None:
        """Add unvisited neighbours of (x, y) to unvisited_nodes."""
        for d in [NORTH, EAST, SOUTH, WEST]:
            nx = x + (d == EAST) - (d == WEST)
            ny = y + (d == SOUTH) - (d == NORTH)

            if (maze.is_in_bounds(nx, ny)
                    and not visited[ny][nx]
                    and (x, y) not in pattern
                    and (nx, ny) not in pattern):
                unvisited_nodes.append((x, y, d))

    def _add_loops(self, maze: Maze, pattern: Set[Tuple[int, int]]) -> None:
        """Remove ~5 % of internal walls to create loops."""
        candidates: List[Tuple[int, int, int]] = []
        for y in range(self.height):
            for x in range(self.width):
                for d in (EAST, SOUTH):
                    nx = x + (d == EAST) - (d == WEST)
                    ny = y + (d == SOUTH) - (d == NORTH)
                    if (maze.is_in_bounds(nx, ny) and
                            maze.is_wall(x, y, d) and
                            (x, y) not in pattern and
                            (nx, ny) not in pattern):
                        candidates.append((x, y, d))
        n_remove = max(1, len(candidates) // 20)
        self._rng.shuffle(candidates)
        for x, y, d in candidates[:n_remove]:
            maze.open_wall(x, y, d)
