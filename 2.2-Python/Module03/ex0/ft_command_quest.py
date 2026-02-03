#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    arg_len: int = len(sys.argv)

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")

    if arg_len > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {arg_len - 1}")
        i: int = 1
        while i < arg_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {arg_len}\n")
