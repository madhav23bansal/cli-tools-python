import random
import time
import click
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# List of words for the game
WORDS = [
    "python",
    "hangman",
    "developer",
    "programming",
    "computer",
    "keyboard",
    "software",
    "internet",
    "algorithm",
    "database",
    "interface",
    "network",
]


def get_random_word():
    """Selects a random word from the WORDS list."""
    return random.choice(WORDS)


def display_hangman(tries):
    """Displays the hangman figure based on the number of incorrect tries."""
    stages = [  # Final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # Head, torso, both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # Head, torso, one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """,
    ]
    # Style the hangman figure based on tries
    style = "bold red" if tries > 3 else "bold yellow" if tries > 0 else "dim"
    return Text(stages[tries], style=style)


@click.command()
def play():
    """Plays a game of Hangman with a Rich UI."""
    word_to_guess = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_tries = 6  # Corresponds to the number of stages in display_hangman

    console.print(
        Panel(
            Text("Welcome to Hangman!", justify="center", style="bold green"),
            title="[b]Hangman Game[/b]",
            border_style="green",
        )
    )

    word_display_list = ["_" for _ in word_to_guess]

    while incorrect_guesses < max_tries:
        console.print(display_hangman(incorrect_guesses))

        word_display_text = Text(" ".join(word_display_list), style="bold cyan")
        guessed_letters_text = Text(
            f"Guessed: {', '.join(sorted(list(guessed_letters)))}",
            style="italic yellow",
        )
        tries_left_text = Text(
            f"Tries left: {max_tries - incorrect_guesses}", style="bold magenta"
        )

        status_panel_content = (
            word_display_text
            + Text("\n")
            + guessed_letters_text
            + Text("\n")
            + tries_left_text
        )
        console.print(
            Panel(
                status_panel_content,
                title="[b]Game Status[/b]",
                border_style="blue",
                padding=(1, 2),
            )
        )

        guess = Prompt.ask("Guess a letter").lower()

        if not guess.isalpha() or len(guess) != 1:
            console.print(
                Text("Invalid input. Please enter a single letter.", style="bold red")
            )
            time.sleep(1)
            continue

        if guess in guessed_letters:
            console.print(
                Text(
                    f"You've already guessed '{guess}'. Try another letter.",
                    style="bold yellow",
                )
            )
            time.sleep(1)
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            console.print(
                Text(f"Good guess! '{guess}' is in the word.", style="bold green")
            )
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display_list[i] = guess
        else:
            console.print(
                Text(f"Sorry, '{guess}' is not in the word.", style="bold red")
            )
            incorrect_guesses += 1

        time.sleep(0.5)  # Brief pause

        if "_" not in word_display_list:
            console.print(
                display_hangman(incorrect_guesses)
            )  # Show final hangman state
            console.print(
                Panel(
                    Text(
                        f"The word was: {word_to_guess}",
                        justify="center",
                        style="bold cyan",
                    ),
                    title="[b]Word Revealed[/b]",
                    border_style="blue",
                )
            )
            console.print(
                Panel(
                    Text(
                        "Congratulations! You guessed the word correctly!",
                        justify="center",
                        style="bold bright_green blink",
                    ),
                    title="[b]Victory![/b]",
                    border_style="green",
                )
            )
            break
    else:  # This else clause executes if the while loop finishes without a 'break' (ran out of tries)
        console.print(display_hangman(incorrect_guesses))  # Show final hangman state
        console.print(
            Panel(
                Text(
                    f"The word was: {word_to_guess}",
                    justify="center",
                    style="bold cyan",
                ),
                title="[b]Word Revealed[/b]",
                border_style="blue",
            )
        )
        console.print(
            Panel(
                Text(
                    "Game Over! You ran out of tries.",
                    justify="center",
                    style="bold red",
                ),
                title="[b]Defeat[/b]",
                border_style="red",
            )
        )


if __name__ == "__main__":
    play()
