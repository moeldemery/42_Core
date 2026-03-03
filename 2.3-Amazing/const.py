
NORTH: int = 1
EAST: int = 2
SOUTH: int = 4
WEST: int = 8

REQUIRED_KEYS = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}

RESET = "\033[0m"
COLOURS = {
    "white":  "\033[37m",
    "cyan":   "\033[36m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "red":    "\033[31m",
    "blue":   "\033[34m",
    "magenta": "\033[35m",
    "neon_green":  "\033[38;5;46m",
    "neon_purple": "\033[38;5;129m",
    "dark_gold":   "\033[38;5;136m",
}
COLOUR_NAMES = list(COLOURS.keys())

MENU_TEXT = (
    "\n=== A-Maze-ing ===\n"
    "\t[r] Re-generate\n"
    "\t[p] Toggle path\n"
    "\t[w] Cycle colour Walls\n"
    "\t[f] Cycle colour 42-Pattern\n"
    "\t[s] Cycle colour Solution Path\n"
    "\t[a] Animate Solution Path\n"
    "\t[q] Quit....\n"
)

MENU_TEXT_BT = (
    "\n=== A-Maze-ing ===\n"
    "\t[r] Re-generate\n"
    "\t[p] Toggle path\n"
    "\t[w] Cycle colour Walls\n"
    "\t[f] Cycle colour 42-Pattern\n"
    "\t[s] Cycle colour Solution Path\n"
    "\t[a] Animate Solution Path\n"
    "\t[b] Animate Grid Generation (backtracking)\n"
    "\t[q] Quit....\n"
)