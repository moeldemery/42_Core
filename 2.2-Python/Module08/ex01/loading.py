
import sys
import importlib

def check_dependency(package_name: str, import_name: str = "") -> tuple[bool, str]:
    """
    Check if a package is installed and return its version.

    Args:
        package_name: The pip package name (e.g. 'matplotlib').
        import_name: The import name if different from package name.

    Returns:
        A tuple of (is_available: bool, version: str).
    """
    name = import_name if import_name else package_name
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""

def check_all_dependencies() -> dict[str, tuple[bool, str]]:
    """Check all required dependencies and return their status."""
    dependencies = {
        "pandas": "pandas",
        "numpy": "numpy",
        "matplotlib": "matplotlib",
    }
    results = {}
    for pkg, imp in dependencies.items():
        available, version = check_dependency(pkg, imp)
        results[pkg] = (available, version)
    return results

def display_dependency_status(results: dict[str, tuple[bool, str]]) -> bool:
    """
    Print dependency check results.

    Returns:
        True if all dependencies are available, False otherwise.
    """
    print("Checking dependencies:")
    all_ok = True
    for pkg, (available, version) in results.items():
        if available:
            description = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready",
            }.get(pkg, "Ready")
            print(f"  [OK] {pkg} ({version}) - {description}")
        else:
            print(f"  [MISSING] {pkg} - NOT installed")
            all_ok = False

    if not all_ok:
        print()
        print("Some dependencies are missing. Install them with:")
        print()
        print("  Using pip:")
        print("    pip install -r requirements.txt")
        print()
        print("  Using Poetry:")
        print("    poetry install")
        print("    poetry run python loading.py")

    return all_ok


def generate_matrix_data() -> "pandas.DataFrame":  # type: ignore[name-defined]
    """Generate simulated Matrix resistance data using numpy and pandas."""
    import numpy as np
    import pandas as pd

    np.random.seed(42)
    n = 1000

    # Simulate Matrix signal data: time series of "signal strength" by agent
    time_steps = np.arange(n)
    # signal_a =  np.random.normal(0, 5, n) + 100
    # signal_b =  np.random.normal(0, 8, n) + 80
    signal_a = np.sin(time_steps * 0.05) * 50 + np.random.normal(0, 5, n) + 100
    signal_b = np.cos(time_steps * 0.03) * 30 + np.random.normal(0, 8, n) + 80
    anomaly = np.where(
        (time_steps > 400) & (time_steps < 500), signal_a * 1.5, signal_a
    )

    df = pd.DataFrame(
        {
            "time": time_steps,
            "signal_sender": signal_a,
            "signal_machines": signal_b,
            "anomaly_detected": anomaly,
        }
    )
    return df

def analyze_data(df: "pandas.DataFrame") -> dict:  # type: ignore[name-defined]
    """Compute basic statistics on the Matrix data."""
    import numpy as np

    stats = {
        "signal_sender": float(np.mean(df["signal_sender"])),
        "mean_machines": float(np.mean(df["signal_machines"])),
        "max_anomaly": float(df["anomaly_detected"].max()),
        "anomaly_count": int((df["anomaly_detected"] > 140).sum()),
    }
    return stats

def generate_visualization(df: "pandas.DataFrame", output_path: str) -> None:  # type: ignore[name-defined]
    """Create and save a visualization of the Matrix data."""
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(nrows= 2, ncols=1, figsize=(12, 8))
    fig.suptitle("Matrix Signal Analysis - sender Resistance Report", fontsize=14)

    # Top plot: signals over time
    axes[0].plot(
        df["time"], df["signal_sender"],
        label="sender Signal", color="#00fd22", linewidth=0.5
    )
    axes[0].plot(
        df["time"], df["signal_machines"],
        label="Machine Signal", color="#fa0000", linewidth=0.5,
    )
    axes[0].set_title("Signal Strength Over Time")
    axes[0].set_xlabel("Time Step")
    axes[0].set_ylabel("Signal Strength")
    axes[0].legend()
    axes[0].set_facecolor("#000000")
    axes[0].grid(color="#333333", linewidth=0.5)

    # Bottom plot: anomaly detection
    axes[1].plot(
        df["time"], df["anomaly_detected"],
        color="#fcf700", linewidth=0.8, label="Anomaly Signal"
    )
    axes[1].axhspan(140, df["anomaly_detected"].max() + 5,
                    alpha=0.2, color="red", label="Anomaly Zone")
    axes[1].set_title("Anomaly Detection")
    axes[1].set_xlabel("Time Step")
    axes[1].set_ylabel("Signal Strength")
    axes[1].legend()
    axes[1].set_facecolor("#0a0a0a")
    axes[1].grid(color="#333333", linewidth=0.5)

    fig.patch.set_facecolor("#111111")
    for ax in axes:
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333333")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close()


def show_pip_vs_poetry_comparison() -> None:
    """Explain the difference between pip and Poetry dependency management."""
    print()
    print("=" * 55)
    print("  pip vs Poetry - Dependency Management Comparison")
    print("=" * 55)
    print()
    print("  pip (requirements.txt):")
    print("    - Simple, flat list of packages + versions")
    print("    - No lock file by default (use pip freeze)")
    print("    - Install: pip install -r requirements.txt")
    print("    - No built-in virtual env management")
    print()
    print("  Poetry (pyproject.toml):")
    print("    - Declares dependencies with version constraints")
    print("    - Generates poetry.lock for reproducible installs")
    print("    - Install: poetry install")
    print("    - Manages its own virtual environment automatically")
    print("    - Also handles packaging and publishing")
    print("=" * 55)

def main() -> None:
    """Main entry point: check dependencies, analyze data, generate chart."""
    print("LOADING STATUS: Loading programs...")
    print()

    results = check_all_dependencies()
    all_ok = display_dependency_status(results)

    if not all_ok:
        sys.exit(1)

    print()
    print("Analyzing Matrix data...")
    df = generate_matrix_data()
    print(f"Processing {len(df)} data points...")
    print(df)

    stats = analyze_data(df)
    print(f"  Mean Sender signal:    {stats['signal_sender']:.2f}")
    print(f"  Mean Machine signal: {stats['mean_machines']:.2f}")
    print(f"  Anomalies MAX detected:  {stats['max_anomaly']}")
    print(f"  Anomalies detected:  {stats['anomaly_count']}")

    output_path = "matrix_analysis.png"
    print("Generating visualization...")
    try:
        generate_visualization(df, output_path)
        print()
        print("Analysis complete!")
        print(f"Results saved to: {output_path}")
    except Exception as e:
        print(f"Visualization error: {e}")
        sys.exit(1)
    
    show_pip_vs_poetry_comparison()

    
if __name__ == "__main__":
    main()
