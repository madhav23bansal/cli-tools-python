# Coin Toss Simulator CLI

A visually appealing command-line interface (CLI) application to simulate coin tosses.

## Description

This CLI tool provides a fun and interactive way to simulate flipping a coin. It displays ASCII art for "Heads" or "Tails" and keeps track of the results over multiple flips. The interface uses `rich` for enhanced text styling and layout.

## Features

- Simulates single or multiple coin tosses.
- Displays ASCII art for Heads and Tails.
- Uses `rich` for a more engaging and "prod-ready" UI feel.
- Shows a summary of results after all tosses.
- Configurable number of flips.

## Installation

To install this CLI tool, navigate to the `packages/coin_toss_cli` directory and run:

```bash
pip install .
```

Ensure you have `click` and `rich` installed, as they are dependencies. They will be installed automatically if listed in `setup.py`.

Alternatively, if this package is part of a larger collection of CLIs managed by a main `setup.py` or `requirements.txt` at the root, follow the installation instructions for the main project.

## Usage

Once installed, you can simulate coin tosses by running the following command in your terminal:

```bash
coin_toss
```

By default, it performs one flip. You can specify the number of flips using the `--flips` option:

```bash
coin_toss --flips 10
```

The game will display the outcome of each toss and a final summary.

## How to Play

1.  Run the `coin_toss` command.
2.  Optionally, specify the number of flips with `--flips <number>`.
3.  Watch the coin flips and see the results!

Enjoy the simulation!
