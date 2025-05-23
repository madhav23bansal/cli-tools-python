import random
import time  # For pauses
import click
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# List of words for the game
WORDS = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "grape",
    "lemon",
    "mango",
    "strawberry",
    "blueberry",
    "raspberry",
    "watermelon",
    "pineapple",
]


def scramble_word(word):
    """Scrambles the letters of a given word."""
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)


def get_random_word_and_scramble():
    """Selects a random word and returns it along with its scrambled version."""
    original_word = random.choice(WORDS)
    scrambled = scramble_word(original_word)
    # Ensure the scrambled word is different from the original
    while scrambled == original_word:
        scrambled = scramble_word(original_word)
    return original_word, scrambled


@click.command()
@click.option(
    "--rounds", default=5, help="Number of rounds to play.", type=int, show_default=True
)
def play(rounds):
    """Plays a game of Word Scramble with a Rich UI."""
    console.print(
        Panel(
            Text("Welcome to Word Scramble!", justify="center", style="bold green"),
            title="[b]Word Scramble[/b]",
            border_style="green",
        )
    )
    console.print(
        Text(
            f"You will play {rounds} rounds. Try to unscramble the words.",
            justify="center",
            style="italic",
        )
    )

    score = 0
    for i in range(1, rounds + 1):
        round_title = f"Round {i} of {rounds}"
        console.print(
            Panel(
                Text(round_title, justify="center", style="bold blue"),
                title="[b]Current Round[/b]",
                border_style="blue",
                padding=(0, 5),
            )
        )

        original, scrambled = get_random_word_and_scramble()

        console.print(
            Panel(
                Text(scrambled, justify="center", style="bold yellow"),
                title="[b]Scrambled Word[/b]",
                border_style="yellow",
            )
        )

        attempts_left = 3
        correct_guess = False
        while attempts_left > 0:
            console.print(
                Text(f"Attempts left for this word: {attempts_left}", style="magenta")
            )
            guess = Prompt.ask("Your guess").lower()

            if guess == original:
                console.print(Text("Correct!", style="bold green blink"))
                score += 1
                correct_guess = True
                break
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    console.print(Text(f"Incorrect. Try again.", style="bold red"))
                else:
                    console.print(
                        Text(
                            "Incorrect. No attempts left for this word.",
                            style="bold red",
                        )
                    )
            time.sleep(0.5)  # Brief pause

        if not correct_guess:
            console.print(
                Panel(
                    Text(
                        f"The word was: {original}", justify="center", style="bold cyan"
                    ),
                    title="[b]Word Revealed[/b]",
                    border_style="cyan",
                )
            )

        time.sleep(1)  # Pause before next round or game over

    # Game Over
    final_score_text = Text(f"Your final score: {score}/{rounds}", justify="center")
    if score == rounds:
        feedback_text = Text(
            "Perfect score! Well done!", justify="center", style="bold bright_green"
        )
    elif score >= rounds / 2:
        feedback_text = Text("Good job!", justify="center", style="bold green")
    else:
        feedback_text = Text(
            "Better luck next time!", justify="center", style="bold yellow"
        )

    console.print(
        Panel(
            final_score_text + Text("\n") + feedback_text,
            title="[b]Game Over[/b]",
            border_style="green",
            padding=(1, 2),
        )
    )


if __name__ == "__main__":
    play()
