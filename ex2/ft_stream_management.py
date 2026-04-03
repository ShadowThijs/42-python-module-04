"""Stream management.

Read and write archive files using stdin/stdout/stderr streams.
"""

import sys
from typing import IO


def read_archive(filename: str) -> str | None:
    """Open and return the contents of an archive file."""
    sys.stdout.write(f"Accessing file '{filename}'\n")
    f: IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return None
    content: str = f.read()
    f.close()
    sys.stdout.write("--\n")
    sys.stdout.write(content)
    sys.stdout.write("--\n")
    sys.stdout.write(f"File '{filename}' closed.\n")
    return content


def transform_content(content: str) -> str:
    """Add a # character at the end of each line."""
    lines: list[str] = content.splitlines()
    transformed: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed) + "\n"


def save_archive(filename: str, content: str) -> None:
    """Save content to a file."""
    sys.stdout.write(f"Saving data to '{filename}'\n")
    f: IO[str]
    try:
        f = open(filename, "w")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        sys.stdout.write("Data not saved.\n")
        return
    f.write(content)
    f.close()
    sys.stdout.write(f"Data saved in file '{filename}'.\n")


if (len(sys.argv) != 2):
    sys.stdout.write("Usage: ft_stream_management.py <file>\n")
else:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    data: str | None = read_archive(sys.argv[1])
    if (data is not None):
        new_data: str = transform_content(data)
        sys.stdout.write("Transform data:\n")
        sys.stdout.write("--\n")
        sys.stdout.write(new_data)
        sys.stdout.write("--\n")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_name: str = sys.stdin.readline().rstrip("\n")
        if (new_name == ""):
            sys.stdout.write("Not saving data.\n")
        else:
            save_archive(new_name, new_data)
