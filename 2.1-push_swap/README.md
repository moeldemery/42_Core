*This project has been created as part of the 42 curriculum by meldemir*

# Push_Swap - 42 Project

## 📋 Description

The goal of the **Push_Swap** project is to sort a given set of unique integers on a single stack (`a`), using a limited set of operations, and displaying the shortest sequence of instructions possible. This implementation leverages a highly optimized hybrid algorithm combining **Longest Increasing Subsequence (LIS)** and a **Cost-Based Greedy Search** to achieve competitive results for high points validation.

### 🚀 Algorithm Implementation Breakdown

### 1. Identifying the Longest Increasing Subsequence (LIS)

The functions in `lis_calc.c` and `lis_set_mask.c` determine which numbers form the "sorted backbone".

*   **`ft_calculate_lis`**: Uses dynamic programming to compute the length of the LIS ending at each element, stored in `lis_cost`.
*   **`ft_set_max_lis_mask`**: Backtracks from the end of the list to mark the chosen LIS sequence by setting the `lis_mask` flag to `1`.
*   **`ft_push_non_lis`**: Pushes all elements with `lis_mask == 0` to Stack B using `ft_pb`.

### 2. The Cost-Based "Turk" Strategy (Stack B -> Stack A)

The functions in `stack_calculate_cost.c` manage the efficient return of elements to Stack A.

*   **`ft_calculate_costs`**: This function iterates through Stack B and uses `ft_find_insert_position` to find the ideal target spot in Stack A. It assigns signed costs (`cost_a`, `cost_b`) for `ra`/`rra` and `rb`/`rrb` moves.
*   **`ft_get_combined_cost`**: This crucial utility optimizes moves by using `Max()` logic for combined rotations (`rr`/`rrr`) to reduce the total action count.

### 3. Executing the Moves (`stack_execute_cost.c`)

*   **`ft_execute_cheapest_move`**: This function finds the element in Stack B with the minimum total cost (`ft_find_cheapest_index`) and performs the moves.
*   **`ft_apply_double_rotations`**: Prioritizes `rr` or `rrr` instructions to save moves.
*   **`ft_apply_single_a` / `ft_apply_single_b`**: Applies remaining single rotations (`ra`, `rra`, `rb`, `rrb`) to align everything perfectly before a final `pa`.

### 4. The Checker Program (Bonus)

A separate `checker` program reads instructions from standard input, validates them, applies them to the stack, and outputs `OK` or `KO` based on the final sorted state. It handles invalid commands by printing `Error` to `stderr` and exiting with a failure status.

Use code with caution.
AI responses may include mistakes. Learn more
## 🚀 Algorithm Implementation Breakdown

### 1. Identifying the Longest Increasing Subsequence (LIS)

The functions in `lis_calc.c` and `lis_set_mask.c` determine which numbers form the "sorted backbone".

*   **`ft_calculate_lis`**: Uses dynamic programming to compute the length of the LIS ending at each element, stored in `lis_cost`.
*   **`ft_set_max_lis_mask`**: Backtracks from the end of the list to mark the chosen LIS sequence by setting the `lis_mask` flag to `1`.
*   **`ft_push_non_lis`**: Pushes all elements with `lis_mask == 0` to Stack B using `ft_pb`.

### 2. The Cost-Based "Turk" Strategy (Stack B -> Stack A)

The functions in `stack_calculate_cost.c` manage the efficient return of elements to Stack A.

*   **`ft_calculate_costs`**: This function iterates through Stack B and uses `ft_find_insert_position` to find the ideal target spot in Stack A. It assigns signed costs (`cost_a`, `cost_b`) for `ra`/`rra` and `rb`/`rrb` moves.
*   **`ft_get_combined_cost`**: This crucial utility optimizes moves by using `Max()` logic for combined rotations (`rr`/`rrr`) to reduce the total action count.

### 3. Executing the Moves (`stack_execute_cost.c`)

*   **`ft_execute_cheapest_move`**: This function finds the element in Stack B with the minimum total cost (`ft_find_cheapest_index`) and performs the moves.
*   **`ft_apply_double_rotations`**: Prioritizes `rr` or `rrr` instructions to save moves.
*   **`ft_apply_single_a` / `ft_apply_single_b`**: Applies remaining single rotations (`ra`, `rra`, `rb`, `rrb`) to align everything perfectly before a final `pa`.

### 4. The Checker Program (Bonus)

A separate `checker` program reads instructions from standard input, validates them, applies them to the stack, and outputs `OK` or `KO` based on the final sorted state. It handles invalid commands by printing `Error` to `stderr` and exiting with a failure status.


## 📊 Performance

This algorithm consistently achieves scores well within the 5-point validation benchmarks provided in the subject:

| Numbers | Goal (5 Points) | My Average Moves |
| :--- | :--- | :--- |
| 100 | < 700 moves | ~500–600 moves |
| 500 | < 5500 moves | ~4,000–4,800 moves |

## 🛠️ Instructions

My program utilizes the mandatory instruction set to manipulate data between two stacks, `a` and `b`:

| Code | Description |
| :--- | :--- |
| `sa` / `sb` / `ss` | Swap the first 2 elements at the top of the stack. |
| `pa` / `pb` | Push the first element from one stack to the top of the other. |
| `ra` / `rb` / `rr` | Shift up all elements of a stack by 1 (first becomes last). |
| `rra` / `rrb` / `rrr` | Shift down all elements of a stack by 1 (last becomes first). |

## ⚙️ Compilation and Execution

### Compilation

To compile the mandatory `push_swap` program and the bonus `checker` program, use the provided `Makefile`:

```bash
# Compile the main push_swap program
make all

# Compile the bonus checker program
make bonus
```

Standard Makefile rules are also available:
```
    make clean: Removes all object files (.o).
    make fclean: Removes object files and the push_swap and checker executables.
    make re: Performs fclean followed by all.
```
### Execution 
The push_swap program: The program takes a list of unique integers as arguments. The output is a sequence of instructions printed to standard output. 

```bash
./push_swap 2 1 3 6 5 8
# Example output:
sa
pb
pb
pb
sa
pa
pa
pa
```
Use code with caution.The checker program (Bonus): The checker reads the output from push_swap via a pipe (|) to verify the sorting process and memory management. It outputs OK if successful or KO otherwise.

```bash
./push_swap 2 1 3 6 5 8 | ./checker 2 1 3 6 5 8
# Output: OK

./push_swap 0 one 2 3
# Output: Error

```
## 💻 Technical Implementation Details 
### Data Structures 
I used a Doubly Linked List structure (t_d_list from my libft) which provides efficient \(O(1)\) operations for most instructions due to pointers to both the next and prev nodes. 

Each node's content pointer holds a t_element structure, defined in push_swap.h, which stores extra metadata crucial for the cost calculation:

``` c
typedef struct s_element
{
	int		value;      // The actual integer value
	int		lis_cost;   // Length of LIS ending here (used in calc)
	int		lis_mask;   // Flag: 1 if part of final LIS, 0 otherwise
	int		cost;       // Total optimal moves (final result)
	int		cost_a;     // Signed moves needed for Stack A target
	int		cost_b;     // Signed moves needed for Stack B element
}			t_element;
```
### Argument Parsing and Error Handling (arg_support.c) 

The initial stack is built with robust error checking, ensuring no non-numeric inputs, duplicates, or integer overflows are accepted. Errors are printed to standard error (stderr) and the program exits cleanly, freeing all memory with free_stack(). 
### Makefile Structure 
The provided Makefile is configured to manage both the main mandatory project (push_swap) and the bonus checker program separately using specific rules (all and bonus). It automatically compiles my libft submodule first before linking, adhering strictly to the project Norm. 

## 🔗 Resources & AI Usage

### Resources

*   **42 Subject PDF**: The official project guidelines, rules, benchmarks, and instruction set definition.
*   **Longest Increasing Subsequence (LIS)**: Standard dynamic programming concept used for the pre-sorting phase.
    *   [Explanation of LIS Algorithm on GeeksforGeeks](https://www.geeksforgoeks.org)
*   **The "Turk Algorithm" (Cost-Based Search)**: The primary strategy for optimizing the return of elements from Stack B to Stack A.
    *   [Push-Swap Turk Algorithm Explained in 6 Steps](https://pure-forest.medium.com)
    *   [42 Push_swap explained (Psuedocodes & Strategy)](https://medium.com)

### AI Usage Statement

I used AI tools primarily for debugging  issues and correcting implementation details in the bonus `checker` program related to `get_next_line` and error handling. AI also assisted in structuring and generating content for this README file to ensure compliance with project requirements. All AI-generated content was thoroughly tested, reviewed with peers, and modified for full comprehension and responsibility.
