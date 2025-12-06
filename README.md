perbaiki 
# 💥 WlsBruteforce: Educational Password Generator 🔑

A lightweight, portable Python module designed for **educational purposes** to demonstrate the mechanics of password bruteforcing using Python's built-in `itertools` library and powerful **generators**.

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/marqsec/wlsbruteforce?style=for-the-badge&color=blue)](https://github.com/marqsec/wlsbruteforce/stargazers)

---

## âœ¨ Features & Purpose

* **Generator-Based:** Uses Python's `yield` keyword for memory efficiency. Combinations are generated on-demand, not stored in memory.

* **Universal Character Set:** Includes all lowercase letters (aâ€“z), uppercase letters (Aâ€“Z), digits (0â€“9), and special symbols (`$` `!` `@` `#` `%` `^` `&` `*` `(` `)` `-` `_` `+` `=` `[` `]` `{` `}` `|` `;` `:` `'` `"` `,` `.` `<` `>` `/` `?` `~`) for maximum password complexity testing.

* **Progress Visualization with `tqdm`:**
  Integrates the `tqdm` library to display a real-time progress bar during brute-force attempts.
  This helps users monitor speed, track attempts, and visually estimate remaining time â€” essential for educational and debugging purposes.

* **HTTP Support with `requests`:**
  Provides optional compatibility with the `requests` module, allowing developers to:
  - Send guessed passwords to an API endpoint
  - Perform login simulations
  - Test authentication endpoints safely
  All for research, testing, and learning how password systems respond under controlled conditions.

* **Cross-Platform:** Works flawlessly on Linux (Kali, Ubuntu, Debian), macOS, Windows, and Termux after `pip` installation.

> âš ï¸ Disclaimer: This module is strictly intended for educational and defensive security research. Use it responsibly and ethically.

## 📥 Installation

Install this package directly from GitHub using `pip`. This method automatically configures the Python path for system-wide access.

### Install via Pip

```bash
pip install "git+https://github.com/marqsec/wlsbruteforce.git"
```

### 🎬 Demo: Live Terminal Interaction

```bash
from wlsbruteforce import WlsBruteforce
from tqdm import tqdm
import sys
import os

# Clear screen depending on OS
if os.name == "nt":      # Windows
    os.system("cls")
else:                    # Linux / macOS
    os.system("clear")

generator = WlsBruteforce()
attempts = generator.brute(min_length=1, max_length=8)

password_target = "marq"
print(f"[•] Starting Brute Force for password: '{password_target}'")
print("-" * 30)

# --- Begin try block to ensure cursor is restored ---
try:
    # 1. Hide the cursor at the start of the process
    print('\033[?25l', end='')

    # Create a progress bar and force output to sys.stderr for better compatibility
    progress_bar = tqdm(attempts, desc="[>] Trying password", file=sys.stderr, unit=" login")

    for password in progress_bar:
        # Update postfix to show the password currently being attempted
        progress_bar.set_postfix_str(f"password: {password}")
        
        # If the password is found
        if password_target == password:
            progress_bar.close()
            print(f"\n[✓] Password found: {password}")
            break

    # If loop finishes without matching password
    else:
        progress_bar.close()
        print(f"\n[✗] Password not found up to the maximum length.")

# --- finally ALWAYS runs ---
finally:
    # Restore cursor visibility
    sys.stderr.write('\033[?25h')
    sys.stderr.flush()

```

### 🧑‍💻 Contribution & Development

```bash
git clone https://github.com/marqsec/wlsbruteforce.git
cd wlsbruteforce
pip install -e .
```

---

💛 **Thanks for checking out this project!**

If this tool helped you and you'd like to support its development, you can show your appreciation here:

[![Saweria](https://img.shields.io/badge/Saweria-FE8A00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://saweria.co/marqsec)

Your support truly means a lot and helps the project grow! ⭐

---


