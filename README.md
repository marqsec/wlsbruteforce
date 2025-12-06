perbaiki 
# 💥 WlsBruteforce: Educational Password Generator 🔑

A lightweight, portable Python module designed for **educational purposes** to demonstrate the mechanics of password bruteforcing using Python's built-in `itertools` library and powerful **generators**.

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/marqsec/wlsbruteforce?style=for-the-badge&color=blue)](https://github.com/marqsec/wlsbruteforce/stargazers)

---

## ✨ Features & Purpose

* **Generator-Based:** Uses Python's `yield` keyword for memory efficiency. Combinations are generated on-demand, not stored in memory.
* **Universal Character Set:** Includes all lowercase letters (`a-z`), uppercase letters (`A-Z`), and digits (`0-9`).
* **Cross-Platform:** Works flawlessly on Linux (Kali, Ubuntu, Debian), macOS, Windows, and Termux after `pip` installation.

> ⚠️ **Disclaimer:** This module is strictly intended for **educational and defensive security research**. Use it responsibly and ethically.

## 📥 Installation

Install this package directly from GitHub using `pip`. This method automatically configures the Python path for system-wide access.

### Install via Pip

```bash
pip install "git+https://github.com/marqsec/wlsbruteforce.git"
```

### 🎬 Demo: Live Terminal Interaction

```bash
from wlsbruteforce import WlsBruteforce
import string

# --- Section 1: Initialization with Custom Charset ---
# Calling __init__ with a smaller custom charset (only lowercase letters
# Note: string.ascii_lowercase contains only 'a' through 'z'
CUSTOM_CHARSET = string.ascii_lowercase

print(f"Initializing WlsBruteforce with custom charset ({len(CUSTOM_CHARSET)} characters)...")
with WlsBruteforce(charset=CUSTOM_CHARSET) as custom_generator:
    MIN_L = 3
    MAX_L = 56
    # --- Section 2: Calling Other Functions (Internal Method) ---
    # Explicitly calling _calculate_combinations
    # Although this is an internal method, we can call it for demonstration.
    # Calculate combinations (length 3 + length 4)
    # Total = (26^3) + (26^4) = 17,576 + 456,976 = 474,552
    
    total_estimated = custom_generator._calculate_combinations(MIN_L, MAX_L)
    print("-" * 40)
    print(f"Call: _calculate_combinations({MIN_L}, {MAX_L})")
    print(f"Estimated Total Combinations: {total_estimated:,}")
    print("-" * 40)

    # --- Section 3: Calling the Main 'brute' Function ---
    # Call the brute method
    attempts = custom_generator.brute(min_length=MIN_L, max_length=MIN_L) # Only length 3

    print(f"Total combinations to be attempted (only length {MIN_L}): {custom_generator.total_combinations_estimate:,}")
    print("\n✅ Starting Brute Force (First 1000 Combinations Only):")

    count = 0
    for password in attempts:
        if count < 1000:
            print(f"[{count}] Password: {password}")
            count += 1
        else:
            break

print("\nDone. WlsBruteforce object has exited the 'with' context.")
```

### 🧑‍💻 Contribution & Development

```bash
git clone https://github.com/marqsec/wlsbruteforce.git
cd wlsbruteforce
pip install -e .
