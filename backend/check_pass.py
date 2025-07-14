import hashlib
import json
import getpass

# Read stored password hash
try:
    with open("password.json") as f:
        stored_hash = json.load(f)["password"]
except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
    print(f"Error reading password file: {e}")
    exit(1)

# Prompt for password
password_try = getpass.getpass("nbk$uk_369")
entered_hash = hashlib.sha256(password_try.encode()).hexdigest()

# Compare hashes
if entered_hash == stored_hash:
    print("Password correct.")
else:
    print("Password incorrect.")