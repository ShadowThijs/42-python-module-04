"""Archive creation.

Read a file, transform its content, and optionally save to a new file.
"""

import sys
from typing import IO


def read_archive(filename: str) -> str | None:
    """Open and return the contents of an archive file."""
    print(f"Accessing file '{filename}'")
    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    content: str = f.read()
    f.close()
    print("--")
    print(content, end="")
    print("--")
    print(f"File '{filename}' closed.")
    return content


def transform_content(content: str) -> str:
    """Add a # character at the end of each line."""
    lines: list[str] = content.splitlines()
    transformed: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed) + "\n"


def save_archive(filename: str, content: str) -> None:
    """Save content to a file."""
    print(f"Saving data to '{filename}'")
    f: IO[str]
    try:
        f = open(filename, "w")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    f.write(content)
    f.close()
    print(f"Data saved in file '{filename}'.")


if (len(sys.argv) != 2):
    print("Usage: ft_archive_creation.py <file>")
else:
    print("=== Cyber Archives Recovery & Preservation ===")
    data: str | None = read_archive(sys.argv[1])
    if (data is not None):
        new_data: str = transform_content(data)
        print("Transform data:")
        print("--")
        print(new_data, end="")
        print("--")
        new_name: str = input("Enter new file name (or empty): ")
        if (new_name == ""):
            print("Not saving data.")
        else:
            save_archive(new_name, new_data)
