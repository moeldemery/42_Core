

from display import render_maze
from mazegen.maze_generator import MazeGenerator
from pattern_generator import generate_42_pattern


maze = MazeGenerator(width=15, height=10, seed=7, perfect=True).generate()
pattern_cells = generate_42_pattern(maze)
for cell in pattern_cells:
    maze.block_cell(cell)

print(
    render_maze(
        solution= [],
        wall_colour="green",
        pattern_cells=pattern_cells,
        pattern_colour="yellow",
        show_solution=True,
        maze=maze,
    )
)