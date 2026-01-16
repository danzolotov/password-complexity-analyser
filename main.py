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

    if len(password) > 128:
        print("Error: Password is too long. Maximum Length: 128 characters.")
        sys.exit(1)

    common_passwords = utilities.load_common_passwords()

    # Analysis
    complexity = analyser.check_complexity(password)
    is_common = analyser.check_common_passwords(password, common_passwords)
    entropy = 0.0 if is_common else analyser.calculate_entropy(password)
    strength = analyser.get_password_strength(entropy)
    time_to_crack = utilities.estimate_crack_time(entropy)
    status = (
        "Compromised" if is_common else "Not found in common password list"
    )
    suggestions = analyser.get_password_suggestions(complexity, entropy)

    # Color Mapping
    entropy_color = utilities.get_entropy_color(entropy)
    strength_color = utilities.get_strength_color(strength)
    status_color = (
        utilities.Colors.FAIL if is_common else utilities.Colors.GREEN
    )
    length_color = utilities.get_length_color(complexity["length"])

    # Report
    print(f"\n{utilities.Colors.HEADER}Basic Report{utilities.Colors.ENDC}")
    print("-" * 30)
    print(f"Password: {password}")
    print(
        f"Length: {length_color}{complexity['length']}{utilities.Colors.ENDC}"
    )
    print(f"Lower Case: {utilities.get_bool_colour(complexity['has_lower'])}")
    print(f"Upper Case: {utilities.get_bool_colour(complexity['has_upper'])}")
    print(f"Digit: {utilities.get_bool_colour(complexity['has_digit'])}")
    print(
        f"Special Character: {utilities.get_bool_colour(complexity['has_special'])}"
    )

    print(f"\n{utilities.Colors.HEADER}Advanced Report{utilities.Colors.ENDC}")
    print("-" * 30)
    print(f"Entropy: {entropy_color}{entropy:.2f} bits{utilities.Colors.ENDC}")
    print(f"Strength: {strength_color}{strength}{utilities.Colors.ENDC}")
    print(
        f"Time to Crack: {utilities.Colors.CYAN}{time_to_crack}{utilities.Colors.ENDC}"
    )
    print(f"Status: {status_color}{status}{utilities.Colors.ENDC}")

    if suggestions:
        print(f"\n{utilities.Colors.HEADER}Suggestions{utilities.Colors.ENDC}")
        print("-" * 30)
        for suggestion in suggestions:
            print(f"- {suggestion}")


if __name__ == "__main__":
    main()
