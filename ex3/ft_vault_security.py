"""Secure file operations using the with statement."""


source_file_name: str = "vault_source.txt"
backup_file_name: str = "vault_backup.txt"
entry_1: str = "[CLASSIFIED] Quantum encryption keys recovered"
entry_2: str = "[CLASSIFIED] Archive integrity: 100%"
new_data: str = "[CLASSIFIED] New security protocols archived"

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

with open(source_file_name, "w") as source_file:
    source_file.write(entry_1 + '\n')
    source_file.write(entry_2 + '\n')

print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

print("SECURE EXTRACTION:")
with open(source_file_name, "r") as source_read:
    data: str = source_read.read()
    print(data)

print("SECURE PRESERVATION:")
with open(backup_file_name, "w") as vault_write:
    vault_write.write(new_data + '\n')
    print(new_data)

print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security")
