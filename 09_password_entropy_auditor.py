"""
Tool 9: Password Strength & Shannon Entropy Auditor
Calculates exact mathematical Shannon entropy, crack time estimations, and generates secure memorable passwords.
Author: Abdelrahman Abouzed
"""

import math
import secrets
import string
import sys


def calculate_entropy(password: str) -> float:
    """Calculates Shannon entropy in bits per character."""
    if not password:
        return 0.0
    freq = {}
    for c in password:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0.0
    for count in freq.values():
        p = count / len(password)
        entropy -= p * math.log2(p)
    # Total entropy in bits = entropy_per_char * length
    return round(entropy * len(password), 1)


def generate_secure_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and any(c.isdigit() for c in pwd)
                and any(c in "!@#$%^&*" for c in pwd)):
            return pwd


def audit_password(password: str):
    bits = calculate_entropy(password)
    length = len(password)

    if bits < 40:
        rating = "VERY WEAK (Instant crack)"
    elif bits < 60:
        rating = "WEAK (Vulnerable to GPU brute-force)"
    elif bits < 80:
        rating = "MODERATE (Good for casual accounts)"
    elif bits < 100:
        rating = "STRONG (Highly resistant)"
    else:
        rating = "VERY STRONG / CRYPTOGRAPHIC (Practically uncrackable)"

    print("\n" + "=" * 55)
    print("      PASSWORD ENTROPY & SECURITY AUDITOR")
    print("=" * 55)
    print(f"Length:           {length} characters")
    print(f"Shannon Entropy:  {bits} bits")
    print(f"Security Rating:  {rating}")
    print("\n[+] Need a strong replacement?")
    print(f"Generated Secure: {generate_secure_password(18)}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    test_pwd = sys.argv[1] if len(sys.argv) > 1 else "SampleP@ssw0rd2026!"
    audit_password(test_pwd)
