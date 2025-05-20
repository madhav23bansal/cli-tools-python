# Word Scramble CLI Game

A fun command-line interface (CLI) application to play Word Scramble.

## Description

This CLI tool challenges users to unscramble words. The game presents a scrambled word, and the player must guess the original word within a limited number of attempts per round.

## Features

- Engaging word scramble gameplay.
- Random word selection from a predefined list.
- Configurable number of rounds.
- Score tracking.
- Limited attempts per word.

## Installation

To install this CLI tool, navigate to the `packages/word_scramble_cli` directory and run:

```bash
pip install .
```

Alternatively, if this package is part of a larger collection of CLIs managed by a main `setup.py` or `requirements.txt` at the root, follow the installation instructions for the main project.

## Usage

Once installed, you can play the game by running the following command in your terminal:

```bash
word_scramble
```

You can also specify the number of rounds you want to play:

```bash
word_scramble --rounds 10
```

The game will start, and you can follow the on-screen prompts to guess the words.

## How to Play

1.  The game will present a scrambled word.
2.  You have 3 attempts to guess the original word.
3.  Type your guess and press Enter.
4.  If your guess is correct, you score a point.
5.  If your guess is incorrect, you lose an attempt.
6.  The game continues for the specified number of rounds (default is 5).
7.  Your final score will be displayed at the end.

Have fun unscrambling!
