"""Vault security.

Provide safe file access using context managers (with statement).
"""


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    """Safely read or write a file using a context manager."""
    if (action == "read"):
        try:
            with open(filename, "r") as f:
                return (True, f.read())
        except OSError as e:
            return (False, str(e))
    else:
        try:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except OSError as e:
            return (False, str(e))


print("=== Cyber Archives Security ===")
print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file"))
print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/shadow"))
print("Using 'secure_archive' to read from a regular file:")
result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
print(result)
print("Using 'secure_archive' to write previous content to a new file:")
print(secure_archive("new_vault_fragment.txt", "write", result[1]))
