# Local CLI Password Manager (Python)

A command-line password management application built in Python that stores website credentials locally using secure text-file delimiter parsing and interfaces directly with the native OS clipboard.

This project covers core data handling fundamentals including file appending ('a' mode), structured line string splitting, and external third-party library integrations.


## Features & Technical Highlights

* Persistent Local Storage: Appends and logs credentials directly into a local passwords.txt file without overwriting existing data streams.
* Custom Delimiter Parsing: Implements a unique string pattern (<||>) as a delimiter boundary to separate website indices from passwords during active file reads.
* Automated Clipboard Copying: Integrates the pyperclip module to inject retrieved passwords directly into the system clipboard, optimizing data leakage safety during active lookups.
* Interactive Controller Loop: Designed around an endless while True menu stream offering responsive numeric navigation controls with fallback exception routing.
* Clean String Normalization: Employs specific data-stripping configurations (.strip()) during conditional file scans to handle accidental line trailing spaces or carriage returns safely.


## How To Run Locally

1. Clone the Project:
git clone https://github.com/iaryaguptaa/password-manager-python.git

2. Install Dependencies:
pip install pyperclip

3. Navigate and Run:
cd password-manager-python
python main.py

4. Use: Choose options to save new entries or look up an existing platform. If found, your password is automatically copied to your clipboard so you can paste it anywhere instantly!


## Key Learnings
* Managing local plain-text datasets with explicit dynamic delimiter bounds.
* Working with third-party utility wrappers to interact directly with OS-level processes.
* Designing self-contained CLI menu control streams with input validation matrices.
