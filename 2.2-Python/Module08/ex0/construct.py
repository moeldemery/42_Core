#!/usr/bin/env python3
import sys
import os
import site

def is_virtual_env() -> bool:
    """Check if the script is running inside a virtual environment."""
    # sys.prefix != sys.base_prefix is the standard check for venv
    return sys.prefix != sys.base_prefix



def display_outside_venv() -> None:
    """Display information and instructions when not in a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")


def get_virtual_env_name() -> str:
    """Return the name of the active virtual environment, if any."""
    venv_path = os.environ.get("VIRTUAL_ENV", "")
    if venv_path:
        return os.path.basename(venv_path)
    return ""

def get_virtual_env_path() -> str:
    """Return the full path to the virtual environment."""
    return os.environ.get("VIRTUAL_ENV", "")

def get_site_packages_path() -> str:
    """Return the site-packages directory for the current environment."""
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        return site.getusersitepackages()

def display_inside_venv() -> None:
    """Display information when running inside a virtual environment."""
    
    env_name = get_virtual_env_name()
    env_path = get_virtual_env_path()
    site_packages = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"  {site_packages}")


def main() -> None:
    """Main entry point: detect environment and display appropriate output."""
    if is_virtual_env():
        display_inside_venv()
    else:
        display_outside_venv()

if __name__ == "__main__":
    main()
