#!/usr/bin/env python3


def ft_archive_creation(file_name: str, text_data: list[str]) -> None:
    """
    This function creates a new persistent data archive. It iterates through 
    a collection of data entries, writing each to the storage unit and 
    simultaneously broadcasting the inscription progress to the console. 
    It ensures the unit is properly sealed (closed) upon completion.
    
    :param file_name: Description
    :type file_name: str
    
    :param text_data: Description
    :type text_data: list[str]
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file_name}")
    fd = None

    try:
        fd = open(file_name, "wt")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        for line in text_data:
            fd.write(line + "\n")
            print(line)

    except Exception as e:
        print(f"ERROR: An unexpected corruption occurred: {e}")

    finally:
        if fd:
            fd.close()
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{file_name}' ready for long-term preservation.")
    


if __name__ == "__main__":
    text_data: list[str]= [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    ft_archive_creation("new_discovery.txt", text_data)
