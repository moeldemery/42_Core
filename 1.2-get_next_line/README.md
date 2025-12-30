*This project has been created as part of the 42 curriculum by meldemir.*

## Description

The **Get Next Line** project is a C function library that reads a file or standard input line by line. The main objective is to implement a function `get_next_line()` that reads and returns one line at a time from a file descriptor, handling dynamic memory allocation and buffer management efficiently.

This project teaches fundamental concepts in C programming including:
- File I/O operations with file descriptors
- Dynamic memory allocation and deallocation
- String manipulation without using the standard C library
- Buffer management strategies
- Handling edge cases (empty files, multiple reads, EOF conditions)

The function is useful for parsing files, processing input streams, and building command-line tools that need to process text line by line.

## Features

- **Line-by-line reading**: Returns one complete line (including the newline character) per call
- **Configurable buffer size**: BUFFER_SIZE can be adjusted at compile time for performance tuning
- **File descriptor support**: Works with any file descriptor (files, stdin, sockets, etc.)
- **Memory efficient**: Manages internal buffers to minimize memory waste
- **Bonus version**: Includes extended functionality for handling multiple file descriptors simultaneously

## Instructions

### Compilation

To compile the project, use the provided Makefile or compile manually:

```bash
# Using gcc directly (default buffer size)
cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c -o get_next_line

# With custom BUFFER_SIZE
cc -Wall -Wextra -Werror -D BUFFER_SIZE=4096 get_next_line.c get_next_line_utils.c -o get_next_line

# Bonus version (multiple file descriptor support)
cc -Wall -Wextra -Werror get_next_line_bonus.c get_next_line_utils_bonus.c -o get_next_line_bonus
```

### Usage

To use `get_next_line()` in your code:

```c
#include "get_next_line.h"

int main(void)
{
    int     fd;
    char    *line;

    fd = open("file.txt", O_RDONLY);
    if (fd == -1)
        return (1);
    
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
```

### Function Signature

```c
char *get_next_line(int fd);
```

**Parameters:**
- `fd`: File descriptor to read from

**Return value:**
- A pointer to the next line (including newline character) on success
- `NULL` when EOF is reached or an error occurs
- The caller must `free()` the returned pointer

## Algorithm Explanation

The Get Next Line project implements a **buffered line reading algorithm** using the following approach:

### Core Strategy: Static Buffer with Persistent State

The algorithm maintains a static buffer that persists between function calls, allowing it to efficiently read chunks of data and extract individual lines:

1. **Static Buffer Persistence**: A static pointer stores leftover data from previous reads. This eliminates redundant re-reading and allows seamless continuation across function calls.

2. **Three-Phase Processing**:
   - **Phase 1 - Check Existing Buffer**: Before performing I/O, the function checks if a complete line (ending with `\n`) exists in the static buffer. If found, it extracts and returns that line.
   - **Phase 2 - Read More Data**: If no complete line exists, the function reads `BUFFER_SIZE` bytes from the file descriptor into a temporary buffer and appends it to the static buffer.
   - **Phase 3 - Extract and Update**: Once a newline is found, the line is extracted (including the newline), and the static buffer is updated to contain only the remaining data for the next call.

3. **Memory Management**:
   - Uses `ft_strlcpy()` and `ft_strlcat()` for safe string operations
   - Creates new allocations for extracted lines
   - Properly frees old buffer pointers when updating
   - Handles edge cases: EOF without newline, empty lines, empty files

### Why This Algorithm?

- **Efficiency**: Reading in chunks (controlled by `BUFFER_SIZE`) reduces system call overhead compared to reading byte-by-byte
- **Simplicity**: Static buffer eliminates the need for complex data structures or external state management
- **Flexibility**: `BUFFER_SIZE` can be tuned for different performance characteristics (larger buffers = fewer system calls, smaller buffers = less memory)
- **Correctness**: The persistent state naturally handles multiple files through file descriptor-specific implementations

### Time and Space Complexity

- **Time**: O(n) where n is the size of the line being read
- **Space**: O(BUFFER_SIZE + line_length) for the internal buffer and returned line

## Project Structure

```
get_next_line/
├── get_next_line.h           # Main header file with function declarations
├── get_next_line.c           # Core implementation
├── get_next_line_utils.c     # Utility functions (ft_strlen, ft_substr, etc.)
├── get_next_line_bonus.h     # Bonus header (multiple FD support)
├── get_next_line_bonus.c     # Bonus implementation
├── get_next_line_utils_bonus.c # Bonus utility functions
├── test.c                    # Test program(Supplied during eval)
├── test2.c                   # Additional test program(Supplied during eval)
└── README.md                 # This file
```

## Testing

Test programs are provided to verify functionality:

```bash
cc -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c test.c -o test
./test
```

## Resources

### Official Documentation
- [man 2 read](https://linux.die.net/man/2/read) - File reading system call
- [man 2 open](https://linux.die.net/man/2/open) - File opening system call
- [man 3 malloc](https://linux.die.net/man/3/malloc) - Dynamic memory allocation

### Learning Materials
- C String Handling Best Practices: https://wiki.sei.cmu.edu/confluence/display/c/STR+Prefix
- Buffer Management in C: https://www.cs.utah.edu/~germain/PPS/Topics/C_Strings/index.html
- File I/O in C: https://www.cprogramming.com/tutorial/file_io.html

### Related Projects
- Learn more about the 42 curriculum: https://www.42.fr/

## AI Usage

AI was used in the following capacities for this project:

- **Algorithm Explanation**: Assisted in articulating and organizing the explanation of the buffered reading algorithm and its design rationale
- **Documentation**: Helped structure and format the README file to meet project requirements
- **Code Comments**: Reviewed and enhanced code comments for clarity (note: actual implementation was done manually)

## Bonus Features

The bonus version (`get_next_line_bonus.c`) extends the functionality to handle multiple file descriptors simultaneously, maintaining separate buffers for each FD to allow interleaved reading from different files.

## Author

- **meldemir** - 42 Berlin

---

*Last updated: December 2025*
