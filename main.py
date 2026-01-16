"""
Password Complexity Analyser
----------------------------
Author: Dan Zolotov
Date: 16/01/2001
Description:
    Primary interface for the password complexity analysis tool.
    Parses command-line arguments to accept a password.
    Carries out a basic and advanced analysis.

Usage:
    python main.py <password>
"""

import argparse
import sys

import analyser
import utilities


def main():
    parser = argparse.ArgumentParser(
        description="Password Complexity Analyser"
    )
    parser.add_argument("password", help="Password to analyse")
    args = parser.parse_args()

    password = args.password

    if not password:
        print("Error: No password entered.")
        sys.exit(1)

    common_passwords = utilities.load_common_passwords()

    # Analysis
    complexity = analyser.check_complexity(password)
    entropy = analyser.calculate_entropy(password)
    is_common = analyser.check_common_passwords(password, common_passwords)
    time_to_crack = utilities.estimate_crack_time(entropy)
    status = (
        "Compromised" if is_common else "Not found in common password list"
    )

    # Report
    print("\nBasic Report")
    print("-" * 30)
    print(f"Password: {password}")
    print(f"Length: {complexity["length"]}")
    print(f"Lower Case: {complexity["has_lower"]}")
    print(f"Upper Case: {complexity["has_upper"]}")
    print(f"Digit: {complexity["has_digit"]}")
    print(f"Special Character: {complexity["has_special"]}")
    print("\nAdvanced Report")
    print("-" * 30)
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Time to Crack: {time_to_crack}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()
