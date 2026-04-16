"""Ancient text recovery.

Read and display a file's contents like the cat command.
"""

import sys
from typing import IO


def read_archive(filename: str) -> None:
    """Open and display the contents of an archive file."""
    print(f"Accessing file '{filename}'")
    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    print("--")
    print(f.read(), end="")
    f.close()
    print("--")
    print(f"File '{filename}' closed.")


if (len(sys.argv) != 2):
    print("Usage: ft_ancient_text.py <file>")
else:
    print("=== Cyber Archives Recovery ===")
    read_archive(sys.argv[1])
