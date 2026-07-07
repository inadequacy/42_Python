import sys
import site

def CheckInsideEnv() -> None:
    if sys.prefix == sys.base_prefix:
        print(f"Current Python: {sys.version}\n" \
              "Not in a virtual environment; use 'python -m venv matrix_env\n'" \
              "followed by 'source matriv_env/bin/activate' # On Unix or\n" \
              "followed by 'matriv_env\Scripts\activate' # On Windows")
        return
    else:
        print(f"You are in a Virtual Environment. Source: {sys.prefix}\n" \
              f"Current Python: {sys.version}" \
              f"{site.getsitepackages()}")
        return
