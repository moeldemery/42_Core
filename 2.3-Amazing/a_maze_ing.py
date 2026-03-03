
from random import randint
import sys
from config_parser import parse_config
from const import COLOUR_NAMES
from display import animate_backtrack_maze_generation, animate_solution_flow, draw_ui, render_maze
from maze_output import write_output_file
from mazegen.maze_generator import MazeGenerator
from pattern_generator import generate_42_pattern


def main() -> int:
    """main entry point for our maze generator program.

    it reads the config file, validates it, and then generates
    the maze according to the specified parameters.
    """
    if len(sys.argv) != 2:
        print("Usage: python a_maze_ing.py <config_file>",
              file=sys.stderr)
        return 1
    
    config_file = sys.argv[1]
    
    try:
        config = parse_config(config_file)
    except FileNotFoundError:
        print(f"Error: config file not found: {config_file!r}",
              file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error parsing config: {e}",
              file=sys.stderr)
        return 1

    # generate txt file output

    # printing the maze to the console
    print(config)
    try:
        maze_width = int(config["WIDTH"])
        maze_height = int(config["HEIGHT"])
    except ValueError:
        print("Error: Invalid maze dimensions", file=sys.stderr)
        return 1
    try:
        current_seed = config["SEED"]
        pattern_cells = generate_42_pattern(
            maze_width=maze_width,
            maze_height=maze_height,
            )
        if config["SHOW_PATTERN"] is False:
            pattern_cells = set()
        maze = MazeGenerator(
            width=maze_width,
            height=maze_height,
            seed=current_seed,
            perfect=config["PERFECT"],
            algorithm=config["ALGORITHM"],
            entry= config["ENTRY"],
            exit_= config["EXIT"],
            pattern=pattern_cells,
        ).generate()
        print(f"{maze}")
        solution = MazeGenerator.solve(
            maze=maze, start=maze.entry, end=maze.exit_
            )
    except Exception as e:
        print(f"Error generating maze: {e}", file=sys.stderr)
        return 1
    try:
        write_output_file(maze, config["OUTPUT_FILE"])
    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        return 1
    show_solution = True
    pattern_colour: str = config["PATTERN_COLOUR"]
    flow_colour: str = config["FLOW_COLOUR"]
    wall_colour: str = config["WALL_COLOUR"]
    wall_idx: int = COLOUR_NAMES.index(wall_colour) if wall_colour in COLOUR_NAMES else 0
    flow_idx: int = COLOUR_NAMES.index(flow_colour) if flow_colour in COLOUR_NAMES else 1
    pattern_idx: int = COLOUR_NAMES.index(pattern_colour) if pattern_colour in COLOUR_NAMES else 2
    is_backtracking: bool = (config["ALGORITHM"] == "backtracker")

    try:
        frame = render_maze(
            wall_colour=wall_colour,
            pattern_cells=pattern_cells,
            pattern_colour=pattern_colour,
            show_solution=show_solution,
            solution=solution,
            maze=maze,
            flow_colour=flow_colour,
        )
    except Exception as e:
        print(f"Error rendering maze: {e}", file=sys.stderr)
        return 1

    draw_ui(frame, backtracking=is_backtracking)
    while True:
        ch = sys.stdin.read(1).lower()
        if not ch:
            break
        if ch in {"\n", "\r", " ", "\t"}:
            continue

        if ch == "q":
            break
        elif ch == "p":
            show_solution: bool = not show_solution
            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "w":
            wall_idx = (wall_idx + 1) % len(COLOUR_NAMES)
            wall_colour = COLOUR_NAMES[wall_idx]

            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "f":
            pattern_idx = (pattern_idx + 1) % len(COLOUR_NAMES)
            pattern_colour = COLOUR_NAMES[pattern_idx]
            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "s":
            flow_idx = (flow_idx + 1) % len(COLOUR_NAMES)
            flow_colour = COLOUR_NAMES[flow_idx]

            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "r":
            current_seed = config["SEED"] + randint(1, 1000)
            maze = MazeGenerator(
                width=maze_width,
                height=maze_height,
                seed=current_seed,
                perfect=config["PERFECT"],
                algorithm=config["ALGORITHM"],
                entry= config["ENTRY"],
                exit_= config["EXIT"],
                pattern=pattern_cells,
            ).generate()
            solution = MazeGenerator.solve(
                maze=maze, start=maze.entry, end=maze.exit_
                )
            try:
                write_output_file(maze, config["OUTPUT_FILE"])
            except Exception as e:
                print(f"Error writing output file: {e}", file=sys.stderr)
                return 1
            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "a":
            animate_solution_flow(
                maze=maze,
                solution=solution,
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                flow_colour=flow_colour,
                frame_delay=0.1,
                )
            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)
        elif ch == "b":
            animate_backtrack_maze_generation(
                maze=maze,
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                flow_colour=flow_colour,
                frame_delay=0.05,
                seed=current_seed,
            )
            solution = MazeGenerator.solve(
                maze=maze, start=maze.entry, end=maze.exit_
            )
            frame = render_maze(
                wall_colour=wall_colour,
                pattern_cells=pattern_cells,
                pattern_colour=pattern_colour,
                show_solution=show_solution,
                solution=solution,
                maze=maze,
                flow_colour=flow_colour,
            )
            draw_ui(frame, backtracking=is_backtracking)

        else:
            draw_ui(frame, backtracking=is_backtracking)
            
        
    return 0     
if __name__ == "__main__":
    sys.exit(main())
