"""File creation with data."""


file_name: str = "new_discovery.txt"
entry__1: str = "[ENTRY 001] New quantum algorithm discovered"
entry__2: str = "[ENTRY 002] Efficiency increased by 347%"
entry__3: str = "[ENTRY 003] Archived by Data Archivist trainee"

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
print(f"Initializing new storage unit: {file_name}")

try:
    with open(file_name, "x") as file:
        print("Storage Unit created successfully!\n")
        print("Inscribing preservation data...")
        file.write(entry__1)
        print(entry__1)
        file.write(entry__2)
        print(entry__2)
        file.write(entry__3)
        print(entry__3)
        file.close()
    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")
except FileExistsError:
    print("Storage unit could not be created!")
    print(f"{file_name} already exists, do not overwrite archives!")
