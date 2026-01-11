import os


# Resolve path to common_passwords.txt safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKLIST_PATH = os.path.join(BASE_DIR, "data", "common_passwords.txt")


def load_blocklist():
    # Loads common and breached passwords from file into a set.
    blocklist = set()

    try:
        with open(BLOCKLIST_PATH, "r", encoding="latin-1",errors="ignore") as file:
            for line in file:
                password = line.strip().lower()
                if password:
                    blocklist.add(password)
    except FileNotFoundError:
        pass

    return blocklist

COMMON_PASSWORDS = load_blocklist()

def is_blocklisted(password):
    if not password:
        return False

    return password.lower() in COMMON_PASSWORDS
