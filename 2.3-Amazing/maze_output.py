
from mazegen.maze_generator import Maze


def write_output_file(maze: Maze, path: str) -> None:
    """writing the maze to the output file in hexadecimal format.
    """
    with open(path, "w") as f:
        for row in maze.grid:
            f.write("".join(f"{cell:x}" for cell in row) + "\n")
        f.write("\n")
        f.write(f"{maze.entry[0]},{maze.entry[1]}\n")
        f.write(f"{maze.exit_[0]},{maze.exit_[1]}\n")
        directions = maze.solution_directions()
        f.write((directions if directions else "") + "\n")