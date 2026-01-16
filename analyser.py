"""
Password Analysis Logic
-----------------------
Author: Dan Zolotov
Date: 16/01/2001
Description:
    Module containing core algorithms for evaluating password strength.
    Includes functions that check adherence to basic rules & calculate Shannon entropy.
"""

import math
import string


def check_complexity(password: str) -> dict:
    """
    Checks for presence of upper, lower, digits, and special characters.
    Returns a dictionary of length and booleans.
    """
    return {
        "length": len(password),
        "has_lower": any(char.islower() for char in password),
        "has_upper": any(char.isupper() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "has_special": any(char in string.punctuation for char in password),
    }


def calculate_entropy(password: str) -> float:
    """
    Calculates Shannon entropy score as a float.
    """
    pool_size = 0

    report = check_complexity(password)

    if report["has_lower"]:
        pool_size += 26
    if report["has_upper"]:
        pool_size += 26
    if report["has_digit"]:
        pool_size += 10
    if report["has_special"]:
        pool_size += 32

    # Entropy equation
    return len(password) * math.log2(pool_size)


def check_common_passwords(password: str, file: set) -> bool:
    """
    Checks if password appears in list of common passwords.
    """
    return password.lower() in file


def get_password_strength(entropy: float) -> str:
    """
    Returns a descriptive strength grade based on entropy score.
    """
    if entropy <= 40:
        return "Very Weak"
    elif entropy <= 60:
        return "Weak"
    elif entropy <= 80:
        return "Moderate"
    elif entropy <= 100:
        return "Strong"
    else:
        return "Very Strong"
