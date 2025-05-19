# Hangman Game CLI

A simple command-line interface (CLI) application to play the classic game of Hangman.

## Description

This CLI tool allows users to play Hangman directly from their terminal. The game randomly selects a word from a predefined list, and the player tries to guess the word by suggesting letters within a certain number of attempts.

## Features

- Classic Hangman gameplay.
- Random word selection.
- Visual representation of the hangman figure.
- Tracks guessed letters and remaining tries.

## Installation

To install this CLI tool, navigate to the `packages/hangman_game_cli` directory and run:

```bash
pip install .
```

Alternatively, if this package is part of a larger collection of CLIs managed by a main `setup.py` or `requirements.txt` at the root, follow the installation instructions for the main project.

## Usage

Once installed, you can play the game by running the following command in your terminal:

```bash
hangman_game
```

The game will start, and you can follow the on-screen prompts to guess letters.

## How to Play

1.  The game will pick a random word.
2.  The word will be displayed as a series of underscores, representing each letter.
3.  Guess a letter by typing it and pressing Enter.
4.  If the letter is in the word, it will be revealed.
5.  If the letter is not in the word, a part of the hangman figure will be drawn.
6.  You have 6 incorrect guesses before the game ends.
7.  Win by guessing all the letters in the word before running out of tries.

Enjoy the game!
