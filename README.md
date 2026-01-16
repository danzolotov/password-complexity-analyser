# Password Complexity Analyser

CLI tool designed to evaluate the strength and security of passwords. This project demonstrates clean software architecture principles, including separation of concerns and modular design.

## Features

- **Command Line Interface:** Simple and intuitive CLI built with `argparse`, allowing for quick analysis directly from the terminal.
- **Complexity:** Checks password length, usage of uppercase/lowercase letters, digits, and special characters.
- **Entropy:** Calculates the Shannon entropy of the password to measure its unpredictability (in bits).
- **Crack Time Estimation:** Provides a human-readable estimate of how long it would take to brute-force the password using modern hardware benchmarks.
- **Strength Grading:** Assigns descriptive grade based on entropy score.
- **Common Password Detection:** Checks against a database of common passwords. Known passwords effectively have 0 entropy.
- **Visual Feedback:** Uses color-coded output to highlight strengths, weaknesses, \& security risks.
- **Smart Suggestions:** Provides actionable advice to improve password strength.

## Architecture & Design

The project is structured to ensure maintainability and readability through separation of concerns.

- **`main.py`:** Entry point and orchestrator. Handles user input and arguments, formats the final output report. Usage of `argparse` allows for standard CLI behavior.
- **`analyser.py`:** Contains core logic and functions for assessing password strength. Decoupled from I/O operations.
- **`utilities.py`:** Manages side effects and helper functions, such as file operations and formatting data.

### Error Handling

Built to fail gracefully.

- **Missing File:** If the `common_passwords.txt` database is missing or corrupted, the `utilities` module handles the exception by alerting the user without crashing the program.
- **Input Validation:** Enforces maximum password length of 128 characters.

## Usage

Run the tool from the terminal by passing the target password as an argument.

```bash
python main.py "Password123"
```

### Example Output

```text
Basic Report
------------------------------
Password: Password123
Length: 11
Lower Case: True
Upper Case: True
Digit: True
Special Character: False

Advanced Report
------------------------------
Entropy: 65.50 bits
Strength: Moderate
Time to Crack: 16 years, 5 months, 29 days, 18 hours and 6 seconds
Status: Not found in common password list

Suggestions
------------------------------
- Increase password length to at least 12 characters.
- Add at least one special character.
```

## Requirements

- Python
- `humanize` library

```bash
pip install humanize
```
