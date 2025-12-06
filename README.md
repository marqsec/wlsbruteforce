perbaiki 
# 💥 WlsBruteforce: Educational Password Generator 🔑

A lightweight, portable Python module designed for **educational purposes** to demonstrate the mechanics of password bruteforcing using Python's built-in `itertools` library and powerful **generators**.

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/YourUsername/wlsbruteforce?style=for-the-badge&color=blue)](https://github.com/YourUsername/wlsbruteforce/stargazers)

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
# Start the Python interpreter from any directory
$ python3
Python 3.10.6 (...) on linux
Type "help", "copyright", "credits" or "license" for more information.

# 1. Import the class
>>> from wlsbruteforce import WlsBruteforce

# 2. Initialize the generator (using default character set)
>>> generator = WlsBruteforce()

# 3. Get the attempts (length 1 to 2)
# NOTE: The number of combinations grows very fast!
>>> attempts = generator.brute(min_length=1, max_length=2)

# 4. Print the first 10 attempts
>>> print("First 10 attempts (Length 1):")
>>> for i in range(10):
...     print(next(attempts), end=' ')
...
a b c d e f g h i j 

# 5. Check the total estimation attribute (calculated after calling brute)
>>> print(f"\n\nTotal estimated attempts for lengths 1-2: {generator.total_combinations_estimate}")
Total estimated attempts for lengths 1-2: 3906 
# (62 characters ^ 1 length) + (62 characters ^ 2 length) = 62 + 3844 = 3906

# Exit Python
>>> exit()
$
```

### 🧑‍💻 Contribution & Development

```bash
git clone https://github.com/marqsec/wlsbruteforce.git
cd wlsbruteforce
pip install -e .
