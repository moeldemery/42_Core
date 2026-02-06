#!/usr/bin/env python3


def ft_ancient_text(file_name: str) -> None:
    """
    This function attempts to establish a connection to a text-based storage 
    unit, retrieves all preserved data fragments, and displays them to the 
    system console. It handles potential access errors if the vault is 
    missing or corrupted.
    
    :param file_name: Description
    :type file_name: str
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    fd = None

    try:
        fd = open(file_name, "rt")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        for line in fd:
            print(f"{line}", end="")
        print("\n\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print(f"ERROR: An unexpected corruption occurred: {e}")
    finally:
        if fd:
            fd.close()

if __name__ == "__main__":
    ft_ancient_text("ancient_fragment.txt")
