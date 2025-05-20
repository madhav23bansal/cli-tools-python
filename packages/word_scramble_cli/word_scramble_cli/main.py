import random
import click

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
    """Plays a game of Word Scramble."""
    click.echo("Welcome to Word Scramble!")
    click.echo(f"You will play {rounds} rounds. Try to unscramble the words.")

    score = 0
    for i in range(1, rounds + 1):
        click.echo(f"\n--- Round {i} of {rounds} ---")
        original, scrambled = get_random_word_and_scramble()

        click.echo(f"Scrambled word: {click.style(scrambled, fg='yellow')}")

        attempts = 3
        correct_guess = False
        while attempts > 0:
            guess = click.prompt("Your guess").lower()

            if guess == original:
                click.echo(click.style("Correct!", fg="green"))
                score += 1
                correct_guess = True
                break
            else:
                attempts -= 1
                if attempts > 0:
                    click.echo(
                        click.style(
                            f"Incorrect. You have {attempts} attempts left.", fg="red"
                        )
                    )
                else:
                    click.echo(click.style("Incorrect. No attempts left.", fg="red"))

        if not correct_guess:
            click.echo(f"The word was: {click.style(original, fg='cyan')}")

    click.echo("\n--- Game Over ---")
    click.echo(f"Your final score: {score}/{rounds}")
    if score == rounds:
        click.echo(click.style("Perfect score! Well done!", fg="bright_green"))
    elif score >= rounds / 2:
        click.echo(click.style("Good job!", fg="green"))
    else:
        click.echo(click.style("Better luck next time!", fg="yellow"))


if __name__ == "__main__":
    play()
