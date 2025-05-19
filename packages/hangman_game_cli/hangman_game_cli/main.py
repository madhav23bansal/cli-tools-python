import random
import click

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
    return stages[tries]


@click.command()
def play():
    """Plays a game of Hangman."""
    word_to_guess = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_tries = 6  # Corresponds to the number of stages in display_hangman

    click.echo("Welcome to Hangman!")
    click.echo(display_hangman(incorrect_guesses))

    word_display = ["_" for _ in word_to_guess]
    click.echo(" ".join(word_display))
    click.echo(f"You have {max_tries - incorrect_guesses} tries left.")

    while incorrect_guesses < max_tries:
        guess = click.prompt("Guess a letter", type=str).lower()

        if not guess.isalpha() or len(guess) != 1:
            click.echo("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            click.echo(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            click.echo(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display[i] = guess
        else:
            click.echo(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        click.echo(display_hangman(incorrect_guesses))
        click.echo(" ".join(word_display))
        click.echo(f"Guessed letters: {', '.join(sorted(list(guessed_letters)))}")
        click.echo(f"You have {max_tries - incorrect_guesses} tries left.")

        if "_" not in word_display:
            click.echo("\nCongratulations! You guessed the word correctly!")
            click.echo(f"The word was: {word_to_guess}")
            break
    else:  # This else clause executes if the while loop finishes without a 'break'
        click.echo("\nGame Over! You ran out of tries.")
        click.echo(f"The word was: {word_to_guess}")


if __name__ == "__main__":
    play()
