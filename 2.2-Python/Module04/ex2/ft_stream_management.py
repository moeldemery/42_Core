#!/usr/bin/env python3
import sys

def ft_stream_management() -> None:
    """
    This function demonstrates proper stream routing by:
    1. Receiving data via the Input Stream (stdin).
    2. Broadcasting status updates via the Standard Channel (stdout).
    3. Routing diagnostic alerts via the Alert Channel (stderr).
    
    for testing save outputs in 2 files:
    python3 ft_stream_management.py > output.txt 2> error.txt
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")

if __name__ == "__main__":
    ft_stream_management()
