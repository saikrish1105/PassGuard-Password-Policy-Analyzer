"""
Defines OWASP-aligned password policy controls and remediation guidance.
"""


POLICY_CONTROLS = [

    # Password Length
    {
        "id": "min_length",
        "category": "Password Length",
        "question": "Does the policy enforce a minimum password length of at least 12 characters?",
        "weight": 10,
        "osi_suggestion": "Enforce a minimum password length of at least 12 characters to improve resistance against brute-force and offline cracking attacks."
    },
    {
        "id": "max_length",
        "category": "Password Length",
        "question": "Does the system support a maximum password length of at least 64 characters without truncation?",
        "weight": 8,
        "osi_suggestion": "Ensure authentication systems support passwords of at least 64 characters and do not silently truncate input."
    },

    # Passphrases
    {
        "id": "passphrases",
        "category": "Passphrase",
        "question": "Does the policy explicitly support long passwords and passphrases?",
        "weight": 8,
        "osi_suggestion": "Allow and encourage the use of long passwords and multi-word passphrases without additional restrictions."
    },

    # Character Handling
    {
        "id": "all_characters_allowed",
        "category": "Character Handling",
        "question": "Are all characters allowed in passwords, including whitespace?",
        "weight": 6,
        "osi_suggestion": "Permit all characters, including whitespace, to maximize password entropy and passphrase usability."
    },
    {
        "id": "unicode_allowed",
        "category": "Character Handling",
        "question": "Are Unicode characters permitted in passwords?",
        "weight": 6,
        "osi_suggestion": "Support Unicode characters in passwords to enable greater character diversity and internationalization."
    },
    {
        "id": "no_truncation",
        "category": "Character Handling",
        "question": "Are passwords processed and stored without silent truncation?",
        "weight": 8,
        "osi_suggestion": "Ensure passwords are processed and stored in full without truncation, particularly when exceeding legacy length limits."
    },

    # Composition Rules
    {
        "id": "no_composition_rules",
        "category": "Composition Rules",
        "question": "Does the policy not forcefully enforce composition rules (e.g., forced symbols, numbers, uppercase)?",
        "weight": 10,
        "osi_suggestion": "Remove mandatory composition rules and rely on password length, passphrases, and blocklists for security."
    },

    # Blocklists
    {
        "id": "common_password_blocklist",
        "category": "Blocklists",
        "question": "Are commonly used passwords blocked during password creation?",
        "weight": 10,
        "osi_suggestion": "Implement blocklists to prevent the use of commonly used and easily guessable passwords."
    },
    {
        "id": "breached_password_blocklist",
        "category": "Blocklists",
        "question": "Are previously breached passwords blocked during password creation?",
        "weight": 10,
        "osi_suggestion": "Screen passwords against known breach datasets and prevent the reuse of compromised credentials."
    },
    {
        "id": "contextual_password_blocklist",
        "category": "Blocklists",
        "question": "Are contextual passwords related to the user or organization blocked?",
        "weight": 6,
        "osi_suggestion": "Block passwords containing user-specific or organization-related information such as usernames, company names, or email addresses."
    },

    # Password Validity & Change
    {
        "id": "no_periodic_expiry",
        "category": "Password Validity",
        "question": "Are passwords not subject to arbitrary periodic expiration?",
        "weight": 8,
        "osi_suggestion": "Disable arbitrary periodic password expiration and require changes only when there is evidence of compromise."
    },
    {
        "id": "change_on_compromise",
        "category": "Password Validity",
        "question": "Are password changes required only when there is evidence of compromise?",
        "weight": 8,
        "osi_suggestion": "Trigger password changes based on compromise indicators such as breach exposure or suspicious activity."
    },

    # Password Storage
    {
        "id": "secure_hashing",
        "category": "Password Storage",
        "question": "Are passwords stored using strong, salted, one-way hashing algorithms?",
        "weight": 12,
        "osi_suggestion": "Store passwords using strong, salted, adaptive hashing algorithms such as Argon2, bcrypt, or PBKDF2."
    },
    {
        "id": "no_plaintext_storage",
        "category": "Password Storage",
        "question": "Are plaintext or reversibly encrypted passwords strictly prohibited?",
        "weight": 12,
        "osi_suggestion": "Eliminate plaintext and reversible password storage entirely to prevent credential disclosure."
    },

    # Authentication Protection
    {
        "id": "rate_limiting",
        "category": "Authentication Protection",
        "question": "Is rate limiting or throttling applied to authentication attempts?",
        "weight": 10,
        "osi_suggestion": "Apply rate limiting or throttling to authentication endpoints to reduce the effectiveness of brute-force attacks."
    },
    {
        "id": "bruteforce_protection",
        "category": "Authentication Protection",
        "question": "Are protections in place against brute-force and credential-stuffing attacks?",
        "weight": 10,
        "osi_suggestion": "Implement defenses such as account lockout thresholds, anomaly detection, and monitoring to mitigate brute-force and credential-stuffing attacks."
    }
]


def run_policy_check():
    # Collects yes/no responses for each password policy control.
    responses = {}

    print("\nPassword Policy Compliance Assessment")
    print("------------------------------------")

    for control in POLICY_CONTROLS:
        answer = input(f"{control['question']} (y/n): ").strip().lower()
        responses[control["id"]] = (answer == "y")

    return responses
