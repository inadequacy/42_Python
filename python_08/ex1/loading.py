import pandas
import matplotlib
import numpy
import sys
import importlib


def Program() -> None:
    try:
        version = importlib.metadata.version("pandas")
        print(f"[OK] {version}")
        version = importlib.metadata.version("numpy")
        print(f"[OK] {version}")
        version = importlib.metadata.version("matplotlib")
        print(f"[OK] {version}")
    except ModuleNotFoundError:
        print(
            "Missing dependencies.\n"
            "Install with pip:\n"
            "pip install -r requirements.txt\n\n"
            ""
            )
    pass


if __name__ == "__main__":
    Program()

###
# Mission Briefing
# Create a data analysis program called loading.py that:
# • Uses pandas for data manipulation
# • Uses numpy for numerical computations and to generate your simulated Matrix
# data. It must be the source of your dataset — not hardcoded lists or range().
# • Uses matplotlib for visualization
# • Demonstrates the difference between pip and Poetry dependency management
# • Includes proper dependency files for both approaches
# Your program should analyze "Matrix data" (you can simulate this with sample data)
# and generate a simple visualization.
# By default, simulate your Matrix data using numpy. If you choose to fetch real data from
# an external API, you are allowed to use requests — but it is not required.
# Requirements
# • Create both requirements.txt (for pip) and pyproject.toml (for Poetry)
# • Your program must handle missing dependencies gracefully
# • Include a comparison function that shows installed package versions
# • Show the differences between pip and Poetry through your program’s output
###
