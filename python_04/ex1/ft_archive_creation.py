#!/usr/bin/env python3


def function() -> None:
    file_name = "new_discovery.txt"
    file = open(file_name, "w")
    print(f"New file created: {file_name}")
    print("Adding following lines:")
    entries = ("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee")
    file.write(entries)
    print(entries)
    print("Lines added, saved for future use.")
    file.close()


if __name__ == "__main__":
    function()
