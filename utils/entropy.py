# Entropy ≈ log2(character_space) × password_length
# This module estimates password entropy to approximate resistance against offline brute-force attacks, following OWASP guidance.

import math


def estimate_entropy(password):
    
    if not password:
        return 0.0

    char_space = 0

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_lower:
        char_space += 26
    if has_upper:
        char_space += 26
    if has_digit:
        char_space += 10
    if has_symbol:
        char_space += 32

    # Fallback in case of unexpected input
    if char_space == 0:
        char_space = 100

    entropy = math.log2(char_space) * len(password)
    return round(entropy, 2)
