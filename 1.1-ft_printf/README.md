*This project has been created as part of the 42 curriculum by meldemir.*

# ft_printf

## Description

`ft_printf` is a recreation of the standard C library's `printf()` function. This project implements a variadic function that formats and prints output according to format specifiers, making it a core component of C programming education.

### Goal

The primary goal of this project is to:
- Understand how variadic functions work in C using `<stdarg.h>`
- Implement format string parsing and character conversion
- Handle multiple data types and output formats
- Create a fundamental I/O library function from scratch

### Overview

The implementation provides support for the most commonly used format specifiers:
- `%c` - Character
- `%s` - String
- `%d` - Decimal integer
- `%i` - Integer
- `%u` - Unsigned integer
- `%x` - Hexadecimal (lowercase)
- `%X` - Hexadecimal (uppercase)
- `%p` - Pointer address
- `%%` - Literal percent sign

The function returns the number of characters printed, matching the behavior of the standard `printf()`.

## Instructions

### Compilation

To compile the project, use the provided Makefile:

```bash
make
```

This will:
1. Compile the libft library (dependency)
2. Compile `ft_printf.c` and `ft_putnbr_base.c`
3. Create a static library `libftprintf.a`

### Available Make Commands

- `make` - Compile and create the static library
- `make clean` - Remove object files
- `make fclean` - Remove object files and the library
- `make re` - Clean and recompile

### Usage

To use `ft_printf` in your code:

```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hello, %s!\n", "World");
    ft_printf("Number: %d, Hex: %x\n", 42, 42);
    return (0);
}
```

Compile with linking:
```bash
cc -Wall -Wextra -Werror main.c libftprintf.a -o program
./program
```

### Testing

A test file (`test.c`) is included with example usage cases. Uncomment the test cases in `ft_printf.c` to run basic functionality tests.

## Algorithm and Data Structure Explanation

### Architecture

The implementation follows a three-tier parsing approach:

1. **Main Loop** (`ft_printf` function)
   - Iterates through the format string character by character
   - Detects the `%` character which signals a format specifier
   - Delegates processing to the classifier function

2. **Format Specifier Classification** (`ft_print_clasifier` function)
   - Takes the character immediately following `%`
   - Routes to appropriate handler based on the specifier type
   - Returns the number of characters printed

3. **Conversion Functions**
   - `ft_print_address` - Handles pointer format (`%p`)
   - `ft_putnbr_base` - Generic number-to-base conversion
   - Library functions for string/character output

### Data Flow Diagram

```
ft_printf(format, ...)
    ↓
va_start() - Initialize variadic argument list
    ↓
Loop through format string
    ├─ Regular character → write(1, char, 1)
    └─ '%' found → ft_print_clasifier()
        ├─ %c → va_arg() → putchar
        ├─ %s → va_arg() → ft_putstr_fd
        ├─ %d/%i → va_arg() → ft_putnbr_base(DEC)
        ├─ %u → va_arg(unsigned) → ft_putnbr_base(DEC)
        ├─ %x → va_arg() → ft_putnbr_base(HEXS)
        ├─ %X → va_arg() → ft_putnbr_base(HEX)
        ├─ %p → va_arg() → ft_print_address()
        └─ %% → write '%' literal
    ↓
va_end() - Clean up argument list
    ↓
return counter (total characters printed)
```

### Key Implementation Details

#### 1. **Variadic Arguments (`va_list`)**
```c
va_list args;
va_start(args, str);           // Initialize after last known parameter
va_arg(args, type);            // Extract arguments in order
va_end(args);                  // Cleanup
```
The variadic mechanism requires careful type handling. Each `va_arg()` call must know the type being extracted, as there's no automatic type checking. Arguments are consumed in the order they appear in the format string.

#### 2. **Base Conversion (`ft_putnbr_base`)**
The project uses a generic base conversion function instead of separate functions for decimal, hex, etc. This demonstrates:
- **Polymorphism through function parameters** - The `base` parameter string defines the digit set
- **Efficient digit extraction** - Using modulo operator to isolate rightmost digit
- **Recursive approach** - Naturally handles multi-digit numbers

Example bases:
- `DEC = "0123456789"` - Decimal (base 10)
- `HEXS = "0123456789abcdef"` - Hexadecimal lowercase (base 16)
- `HEX = "0123456789ABCDEF"` - Hexadecimal uppercase (base 16)

#### 3. **Pointer Handling**
```c
static int ft_print_address(unsigned long addr)
{
    if (!addr)
        return (write(1, "(nil)", 5));  // NULL pointer special case
    write(1, "0x", 2);                  // Prefix
    return (ft_putnbr_base(addr, HEXS) + 2);
}
```
Pointers require special handling:
- NULL pointers print as `(nil)` instead of `0x0`
- Cast to `unsigned long` for proper bit representation
- Prefix with `0x` to indicate hexadecimal

#### 4. **Character Counting**
The function maintains a `counter` variable tracking all printed characters. Each branch returns the number of characters it printed, which is accumulated. This matches `printf()`'s return value specification.

### Why This Design?

**Advantages:**
- **Simplicity** - Linear parsing without complex state machines
- **Efficiency** - Single pass through format string, O(n) complexity
- **Reusability** - Generic `ft_putnbr_base` handles multiple number formats
- **Portability** - Uses only standard C library functions

**Trade-offs:**
- No support for width specifiers (e.g., `%5d`) or precision (e.g., `%.2f`)
- No floating-point support
- Limited format specifier set
These are intentional constraints of the 42 curriculum project scope.

## Resources

### Documentation
- [C Standard Library - printf](https://en.cppreference.com/w/c/io/printf) - CPP Reference documentation
- [stdarg.h - Variable Argument Lists](https://en.cppreference.com/w/c/variadic) - How variadic functions work
- [unistd.h - write() system call](https://man7.org/linux/man-pages/man2/write.2.html) - Low-level output

### Articles & Tutorials
- [Number Base Conversion](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/a/intro-to-logarithms) - Understanding base systems
- [Function Pointers in C](https://www.tutorialspoint.com/cprogramming/c_function_pointers.htm) - Alternative design pattern

### Related 42 Projects
- `libft` - Foundation library providing helper functions used by ft_printf

## Technical Choices

### Why `write()` instead of `putchar()`?
Using the `write()` system call provides:
- Direct control over the file descriptor (stderr, stdout, etc.)
- Better performance for bulk operations
- Consistency with low-level I/O operations

### Why a single `ft_putnbr_base()` function?
Rather than implementing separate functions for decimal, hex, and octal conversion, a generic base conversion function:
- Reduces code duplication
- Makes the codebase more maintainable
- Demonstrates generic programming in C

## AI Usage

AI assistance was utilized for the following aspects of this project:

### Tasks Using AI:
1. **README Documentation Structure** - AI helped organize and format the README.md according to the 42 curriculum requirements, including the proper markdown syntax and section organization.

2. **Algorithm Explanation** - AI assisted in articulating the technical implementation details and creating clear data flow diagrams to illustrate how the components interact.

3. **Code Review and Comments** - AI provided feedback on code clarity and helped ensure consistent documentation practices throughout the codebase.

### Parts of the Project Using AI:
- **This README.md file** - Entirely structured and written with AI assistance for clarity and completeness
- **Documentation comments** - AI helped verify the accuracy of inline documentation
- **Testing methodology** - AI suggested test cases and validation approaches

### Parts Developed Independently:
- Core algorithm implementation (`ft_printf.c`, `ft_putnbr_base.c`)
- Makefile creation
- Integration with libft library
- Debugging and optimization

## Project Structure

```
.
├── ft_printf.c          # Main implementation with variadic function
├── ft_printf.h          # Header file with function declarations
├── ft_putnbr_base.c     # Generic base conversion utility
├── Makefile             # Build configuration
├── test.c               # Test cases (reference)
├── libft/               # Dependency: 42 standard library
└── README.md            # This file
```

## Compilation Requirements

- GCC or compatible C compiler
- POSIX-compliant system (Linux, macOS, etc.)
- Standard C library headers (`stdarg.h`, `unistd.h`, `stdlib.h`)
- libft static library (included as dependency)

## License

This project is part of the 42 curriculum and is provided as educational material.
