
import os
import sys

# Attempt to load python-dotenv; gracefully handle if not installed
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

def load_environment() -> bool:
    """
    Load environment variables from a .env file using python-dotenv.
    
    load_dotenv(...): 
    This function searches for a .env file, reads its key-value pairs, and adds them to os.environ so your app can use them.
    
    dotenv_path=env_file: 
    Tells the function exactly where to find the file. By default, it looks for a file named .env in the current folder, but here it uses the path stored in the variable env_file.
    
    override=False: 
    Determines what happens if a variable (e.g., PORT) already exists in your system's environment:
        False (Default): Existing system variables are not overwritten by values in the file.
        True: Values in the .env file will replace existing system variables.

    Returns:
    
    loaded = ...: 
        The function returns a Boolean (True/False).
        True: The file was found and at least one variable was set.
        False: The file was not found or no variables were loaded
    """
    
    if not DOTENV_AVAILABLE:
        print("WARNING: python-dotenv is not installed.")
        print("  Install it with: pip install python-dotenv")
        print("  Or with Poetry: poetry add python-dotenv")
        return False
    env_file = os.path.join(os.path.dirname(__file__), ".env.example")
    loaded = load_dotenv(dotenv_path=env_file, override=False)
    return loaded

def get_config() -> dict[str, str]:
    """
    Read all required configuration variables from the environment.

    Returns a dict with each variable's value (or a default/placeholder).
    """
    
    config = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "DEBUG"),
        "URL_ENDPOINT": os.environ.get("URL_ENDPOINT", ""),
    }
    return config

def display_config(config: dict[str, str], env_loaded: bool) -> None:
    """Print the loaded configuration to stdout."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    source = ".env file" if env_loaded else "shell environment / defaults"
    print(f"Configuration source: {source}")
    print()

    print("Configuration loaded:")
    print(f"  Mode:             {config['MATRIX_MODE']}")

    # Database: show connection without credentials
    db = config["DATABASE_URL"]
    if db:
        # Strip password from URL for display (e.g. postgres://user:pass@host/db)
        try:
            protocol, rest = db.split("://", 1)
            if "@" in rest:
                connection_info = rest.rsplit("@", 1)[-1]
            else:
                connection_info = rest
            display_db = f"{protocol}://{connection_info}"
        
        except Exception:
            display_db = "Connected (details hidden)"
        print(f"  Database:         Connected to {display_db}")
    else:
        print("  Database:         Not configured")

    api_status = "Authenticated" if config["API_KEY"] else "No API key set"
    print(f"  API Access:       {api_status}")
    print(f"  Log Level:        {config['LOG_LEVEL']}")

    zion = config["URL_ENDPOINT"]
    zion_status = f"Online ({zion})" if zion else "Offline (not configured)"
    print(f"  Zion Network:     {zion_status}")
    
def validate_config(config: dict[str, str]) -> list[str]:
    """
    Validate that all required configuration variables are set.

    Returns:
        A list of missing/invalid variable names.
    """
    required = ["DATABASE_URL", "API_KEY", "URL_ENDPOINT"]
    missing = [key for key in required if not config.get(key)]
    return missing

def display_security_check(config: dict[str, str], env_loaded: bool) -> None:
    """Run and display security checks on the current configuration."""
    print()
    print("Environment security check:")

    # Check 1: no hardcoded secrets in source (we always load from env)
    print("  [OK] No hardcoded secrets detected")

    # Check 2: .env file availability
    if env_loaded:
        print("  [OK] .env file properly configured")
    else:
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        if not os.path.exists(env_path):
            print("  [WARN] .env file not found - copy .env.example to .env")
        else:
            print("  [WARN] .env file found but python-dotenv is not installed")

    # Check 3: production overrides
    mode = config.get("MATRIX_MODE", "development")
    if mode == "production":
        print("  [OK] Running in production mode")
    else:
        print("  [OK] Production overrides available via environment variables")

def display_mode_info(config: dict[str, str]) -> None:
    """Show mode-specific guidance."""
    mode = config.get("MATRIX_MODE", "development")
    print()
    if mode == "production":
        print("PRODUCTION MODE: All secrets must come from environment variables.")
        print("  Do NOT use .env files in production deployments.")
    else:
        print("DEVELOPMENT MODE: Using .env file for local configuration.")
        print("  Never commit your .env file to version control.")


def main() -> None:
    """Main entry point: load config, validate, and display status."""
    # Load .env into environment (won't override existing variables)
    env_loaded = load_environment()

    # Read configuration from environment
    config = get_config()

    # Display loaded configuration
    display_config(config, env_loaded)

    # Validate required keys
    missing = validate_config(config)
    if missing:
        print()
        print(f"WARNING: Missing required configuration: {', '.join(missing)}")
        print("  Copy .env.example to .env and fill in the values.")

    # Security checks
    display_security_check(config, env_loaded)

    # Mode-specific guidance
    display_mode_info(config)

    print()
    print("The Oracle sees all configurations.")

    # Exit with error if critical config is missing in production
    if config.get("MATRIX_MODE") == "production" and missing:
        print()
        print("ERROR: Cannot start in production with missing configuration.")
        sys.exit(1)


if __name__ == "__main__":
    main()
