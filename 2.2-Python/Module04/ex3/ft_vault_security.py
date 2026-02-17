#!/usr/bin/env python3


def ft_vault_security(
    file_read_name: str,
    file_write_name: str,
    write_content: str
) -> None:
    """
    Docstring for ft_vault_security
    Implements secure file operations using the 'with' statement protocols.
    This function demonstrates safe extraction (reading) and preservation
    (writing) of classified archive data, ensuring automatic resource cleanup.

    Flag, Name,      R, W, File Ptr Start, If File Exists,     If File Missing
    r,    Read,      Y, N, Beginning,      Opens for reading,  Error
    w,    Write,     N, Y, Beginning,      Overwrites (wipes), Creates New
    a,    Append,    N, Y, End,            Adds to end,        Creates New
    x,    Exclusive, N, Y, Beginning,      Error,              Creates New

    Flag	Name		    Pointer Behavior
    r+	    Read/Update		Starts at Beginning + Read old.
    w+	    Write/Update	Starts at Beginning (Overwrites) + Read new.
    a+	    Append/Update	Starts at End for writing + Read old.

    :param file_read_name: Description
    :type file_read_name: str
    :param file_write_name: Description
    :type file_write_name: str
    :param write_content: Description
    :type write_content: str
    """

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    read_content: str = ""
    try:
        with open(file_read_name, "r") as vault:
            read_content = vault.read()
            print(read_content)
    except FileNotFoundError:
        print("FAILED TO FIND THE VAULT")

    print("\nSECURE PRESERVATION:")
    with open(file_write_name, "w") as vault:
        vault.write(write_content + "\n")
        print(write_content)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security(
        "classified_data.txt",
        "security_protocols.txt",
        "[CLASSIFIED] New security protocols archived",
    )
