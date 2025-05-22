# Memory Game CLI

A classic Memory (Concentration) game for your command-line interface, built with `rich` for an enhanced user experience.

## Description

This CLI tool brings the timeless card-matching game to your terminal. Players flip cards to find matching pairs of symbols on a grid. The game features a clear, colorful board and tracks attempts.

## Features

- Classic Memory game (Concentration) gameplay.
- Configurable board size (currently supports 2x2 and 4x4).
- Uses `rich` for a visually appealing and interactive board.
- Clear screen updates for better gameplay flow.
- Tracks the number of attempts and matched pairs.
- Interactive prompts for card selection.

## Installation

To install this CLI tool, navigate to the `packages/memory_game_cli` directory and run:

```bash
pip install .
```

Ensure you have `click` and `rich` installed, as they are dependencies. They will be installed automatically if listed in `setup.py`.

Alternatively, if this package is part of a larger collection of CLIs managed by a main `setup.py` or `requirements.txt` at the root, follow the installation instructions for the main project.

## Usage

Once installed, you can start the game by running the following command in your terminal:

```bash
memory_game
```

By default, it starts a 4x4 game. You can specify the board size using the `--size` option (currently 2 or 4):

```bash
memory_game --size 2  # Starts a 2x2 game
memory_game --size 4  # Starts a 4x4 game
```

Follow the on-screen prompts to select cards.

## How to Play

1.  Run the `memory_game` command, optionally specifying the `--size`.
2.  The game board will be displayed with all cards face down (marked as 'X').
3.  Enter the row and column numbers to flip your first card.
4.  Enter the row and column numbers for your second card.
5.  If the symbols on the two cards match, they will remain face up.
6.  If they don't match, they will be flipped back down after a short delay.
7.  Continue until all pairs are matched.
8.  The game will display your total attempts at the end.

Try to match all pairs in the fewest attempts!
