import typing
import sys


def CheckInsideEnv() -> None:
    if sys.prefix == sys.base_prefix:
        print("Not in a virtual environment; use 'python3 -m venv matrix_env\n'" \
              "followed by 'source matriv_env/bin/activate'")
        return
    else:
        print(f"You are in a Virtual Environment. Source: {sys.prefix}")
        return
