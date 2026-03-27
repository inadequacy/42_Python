#!/usr/bin/env python3

def try_except(file: str, rule: str) -> None:
    try:
        with open(file, rule) as f:
            f.read()
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...\n"
                  "SUCCESS: Archive recovered - 'Knowledge preserved'\n"
                  "STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...\n"
              "RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file}'...\n"
              "RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"I don't even know went wrong lol -> {e.__class__.__name__}")


def function() -> None:
    print("Cyber Archives - crisis response system\n")

    try_except("lost_archive.txt", "r")
    try_except("classified_data.txt", "w")
    try_except("standard_archive.txt", "r")

    print("All scenarios tested, archives secure")


if __name__ == "__main__":
    function()
