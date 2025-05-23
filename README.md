# A Collection of Python CLI Tools

`cli-tools-python` is a monorepo hosting a variety of useful and fun command-line interface (CLI) tools, each developed as a separate Python package. This project serves as a central hub for managing, discovering, and using these tools.

## Overview

This repository contains multiple independent CLI applications, ranging from utility tools like a BMI calculator and password generator to simple games like Hangman and Word Scramble. Each tool is designed to be easy to install and use directly from your terminal.

A central CLI manager (`main.py`) is provided to help you list all available tools and get detailed usage instructions for each one.

## Features

- **Monorepo Structure:** Manages multiple CLI tools within a single repository.
- **Diverse Toolset:** Includes utilities, games, and helper scripts.
- **Individual Packages:** Each tool is a standalone Python package located in the `packages/` directory.
- **Central CLI Manager:** Use `python main.py` to list tools and view their specific usage.
- **Easy Installation:** Install all tools and their dependencies with a single command.
- **Rich CLI Output:** Some tools leverage the `rich` library for enhanced terminal UIs.

## Available Tools

The following CLI tools are available in this collection:

| Tool Name                 | Command             | Description                                                     |
| ------------------------- | ------------------- | --------------------------------------------------------------- |
| BMI Calculator            | `bmi-calculator`    | Calculates Body Mass Index (BMI).                               |
| Coin Toss Simulator       | `coin_toss`         | Simulates tossing a coin with a rich UI.                        |
| Color to Hex Converter    | `color_to_hex_cli`  | Converts color names to their corresponding hexadecimal codes.  |
| Countdown Timer           | `countdown_timer`   | A simple CLI tool to start a countdown timer.                   |
| Git Helper                | `git_helper`        | A simple CLI tool to quickly get help with common Git commands. |
| Hangman Game              | `hangman_game`      | Plays a classic game of Hangman in the CLI.                     |
| Memory Game               | `memory_game`       | Plays a classic Memory (Concentration) game with a rich UI.     |
| Random Password Generator | `random_password`   | A CLI tool to generate random passwords.                        |
| Simple Calculator         | `simple-calculator` | Performs arithmetic operations (add, sub, mul, div, pow, sqrt). |
| Word Scramble Game        | `word_scramble`     | Plays a word scramble game in the CLI.                          |

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git (for installing packages from the repository, as specified in `requirements.txt`)

### Steps

1.  **Clone the repository (if you haven't already):**

    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL of this project
    cd cli-tools-python
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install all tools and dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This command will install all the necessary dependencies and all the CLI tools listed above, making their commands available in your activated virtual environment.

## Usage

### Central CLI Manager

This project includes a central script (`main.py`) to help you manage and discover the available tools.

1.  **List all available tools:**
    Navigate to the root directory of the project and run:

    ```bash
    python main.py list
    ```

    This will display a table with the names, commands, usage syntax, and descriptions of all tools.

2.  **Get usage for a specific tool:**
    To get detailed usage for a particular tool, use its command:
    ```bash
    python main.py usage <tool_command>
    ```
    For example:
    ```bash
    python main.py usage countdown_timer
    ```

### Using Individual Tools

Once installed (e.g., via `pip install -r requirements.txt`), each tool can be run directly from your terminal using its respective command. For example:

- To calculate BMI:
  ```bash
  bmi-calculator --weight 70 --height 1.75
  ```
- To generate a random password:
  ```bash
  random_password --length 16
  ```
- To play Hangman:
  ```bash
  hangman_game
  ```

Refer to the table above or use `python main.py list` for the specific command and usage pattern of each tool. Most tools also support a `--help` flag for quick usage information (e.g., `bmi-calculator --help`).

## Project Structure

The project is organized as follows:

```
cli-tools-python/
├── main.py                 # Central CLI manager
├── requirements.txt        # Project dependencies, including all tools
├── packages/               # Contains all individual CLI tool packages
│   ├── bmi_calculator_cli/
│   │   ├── bmi_calculator_cli/ # Source code for the tool
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   └── setup.py            # Packaging script for the tool
│   ├── coin_toss_cli/
│   │   └── ... (similar structure for other tools)
│   └── ...
└── README.md               # This file (or PROJECT_README.md if this attempt works)
```

Each tool within the `packages/` directory is a self-contained Python package, typically with its own `setup.py` (for `pip install .` or `-e .` installations) and source code. The root `requirements.txt` file lists all these packages as editable installs along with other common dependencies like `click`, `rich`, and `typer`.

## Contributing

Contributions are welcome! If you have an idea for a new CLI tool, a bug fix, or an improvement to an existing tool, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or fix (`git checkout -b feature/your-feature-name`).
3.  Develop your tool in a new subdirectory under `packages/`. Ensure it has a `setup.py` and follows a similar structure to existing tools.
4.  Add your new package to the root `requirements.txt` as an editable install (e.g., `-e ./packages/your_new_tool_cli`).
5.  If your tool has a `main` function or a `Typer` app, update the `tools_info` list in the root `main.py` to include your tool.
6.  Commit your changes (`git commit -am 'Add some feature'`).
7.  Push to the branch (`git push origin feature/your-feature-name`).
8.  Open a Pull Request.

Please ensure your code is well-documented and, if applicable, includes a `README.md` within its package directory.

## License

This project and its constituent packages are licensed under the MIT License. (It's recommended to add a `LICENSE` file to the root of the project containing the MIT License text if one doesn't already exist.)
