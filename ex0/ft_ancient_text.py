"""Text recovery from a file."""


file_name: str = "ancient_fragment.txt"

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print(f"Accessing Storage Vault: {file_name}")

try:
    with open(file_name, "r") as file:
        data: str = file.read()
        print("Connection established!\n")
        print("Recovered data from storage vault: ")
        print(data)
        print()
        print("Data recovery complete. Storage unit disconnected.")
        file.close()
except FileNotFoundError:
    print(f"Connection failed: {file_name} not found")
except PermissionError:
    print(f"Connection failed: {file_name} needs elevated priveleges")
