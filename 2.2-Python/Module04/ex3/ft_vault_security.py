#!/usr/bin/env python3

def ft_vault_security() -> None:
    
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    
    print("SECURE EXTRACTION:")
    with open("demofile.txt", "a") as f:
        f.write("Now the file has more content!")
    
if __name__ == "__main__":
    ft_vault_security()