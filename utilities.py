"""
Utility Functions
-----------------
Author: Dan Zolotov
Date: 16/01/2001
Description:
    Module providing helper functions to support password analysis tool.
    Includes functions for loading common password lists & estimating cracking times based on entropy calculations.
"""

import os

import humanize


def load_common_passwords(filename="common_passwords.txt"):
    """
    Loads common passwords from a text file into a set for fast lookup.
    """
    if not os.path.exists(filename):
        print(f"File {filename} not found. Skipping dictionary check.")
        return set()

    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            return {line.strip().lower() for line in f}
    except IOError as e:
        print(f"Could not read file: {e}")
        return set()


def estimate_crack_time(entropy: float) -> str:
    """
    Estimates time to crack based on entropy and hardware power.

    Assumptions:
    - Attacker uses single modern GPU: 100 billion guesses per second.
    - MD5 Hashing Algorithm.
    """
    GUESSES_PER_SECOND = 100_000_000_000
    GPU_CLUSTER = 1  # How many GPUs running in parallel
    total_combinations = 2**entropy
    seconds_to_crack = total_combinations // GUESSES_PER_SECOND * GPU_CLUSTER

    try:
        return humanize.precisedelta(seconds_to_crack)
    except OverflowError:
        return "Infinity"
