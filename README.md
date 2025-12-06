perbaiki 
# 💥 WlsBruteforce: Educational Password Generator 🔑

A lightweight, portable Python module designed for **educational purposes** to demonstrate the mechanics of password bruteforcing using Python's built-in `itertools` library and powerful **generators**.

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/marqsec/wlsbruteforce?style=for-the-badge&color=blue)](https://github.com/marqsec/wlsbruteforce/stargazers)

---

## ✨ Features & Purpose

* **Generator-Based:** Uses Python's `yield` keyword for memory efficiency. Combinations are generated on-demand, not stored in memory.
* **Universal Character Set: Includes all lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and special symbols ($`! @ # $ \% \wedge \& * ( ) - _ + = [ ] \{ \} | \ ; : ' " , . < > / ? \text{\textasciitilde} `$) for maximum password complexity testing.
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

# --- INITIALIZATION SECTION ---
# 1. Creates an instance of the WlsBruteforce class.
# This sets up the object with the DEFAULT_CHARSET (letters, numbers, symbols).
generator = WlsBruteforce()

# 2. Calls the 'brute' method to get the password generator.
# This generator will yield all combinations from length 1 up to length 2.
attempts = generator.brute(min_length=1, max_length=2)

print("✅ Starting Brute Force (Length 1 and 2):")
print("-" * 30)

# --- EXECUTION SECTION ---
count = 0
# The loop requests one password from the generator on each iteration.
for password in attempts:
    count += 1
    
    # Prints the loop counter (count) and the generated password.
    # The 'count' variable replaces the problematic 'length' variable here.
    print(f"[{count}] password : {password}")

    # Limit: Stops the output after 1000 combinations for demonstration purposes.
    if count >= 1000: 
        break

print("-" * 30)
print(f"Done (Displayed the first {count} combinations).")
```

### 🧑‍💻 Contribution & Development

```bash
git clone https://github.com/marqsec/wlsbruteforce.git
cd wlsbruteforce
pip install -e .
